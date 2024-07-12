from flask import Flask, request, jsonify
from laonlp import word_tokenize
import re
from keras.models import load_model
from keras.utils import pad_sequences
import numpy as np
import pickle

app = Flask(__name__)

# Load models and vocabularies
enc_model = load_model('model/encoder_model.h5', compile=False)
dec_model = load_model('model/decoder_model.h5', compile=False)
inv_vocab = pickle.load(open("model/vocabulary.pkl", "rb"))
vocab = {w: v for v, w in inv_vocab.items()}
keyword_list = pickle.load(open("model/keyword.pkl", "rb"))
enc_in = pickle.load(open("model/question.pkl", "rb"))

def decode_sequence(input_seq):
    for sentence in enc_in:
        if np.array_equal(input_seq, [sentence]):
            states_value = enc_model.predict(input_seq)

            target_seq = np.zeros((1,1))
            target_seq[0,0] = vocab['<SOS>']

            stop_condition = False
            decoded_sentence = ''
            while not stop_condition:
                output_tokens, h, c = dec_model.predict([target_seq] + states_value)
                sampled_token_index = np.argmax(output_tokens[0, -1, :])
                sampled_word = inv_vocab[sampled_token_index]
                decoded_sentence += '' + sampled_word

                if(sampled_word == '<EOS>' or len(word_tokenize(decoded_sentence)) > 100):
                    stop_condition = True

                target_seq = np.zeros((1,1))
                target_seq[0,0] = sampled_token_index
                
                states_value = [h,c]

            return decoded_sentence
    return "ຂໍອະໄພ, ບໍ່ສາມາດຕອບຄຳຖາມນີ້ໄດ້"   

def remove_special_character(text):
    return re.sub(r'[^0-9a-zA-Zກຂຄງຈສຊຍດຕຖທນບປຜຝພຟມຢລຫຼຣວຫອຮໜໝໆຽະາິີຶືໂໍເແຸູຳໄໃັົ່້໌+]', '', text)

def remove_spaces(text):
    return text.replace(" ", "")

@app.route('/', methods=['POST'])
def chat():
    input_text = request.json.get('input_text')
    input_seq = remove_special_character(input_text)
    input_seq = remove_spaces(input_seq)
    txt = []
    lst = []
    input_seq = word_tokenize(input_seq)
    words = [word for word in input_seq if word in keyword_list]
    for x in words:
        try:
            lst.append(vocab[x])
        except:
            lst.append(vocab['<OUT>'])
    txt.append(lst)
    input_padded_seq = pad_sequences(txt, 15, padding='post', truncating='post')
    response = decode_sequence(input_padded_seq)
    # Remove <OUT> and <PAD> tokens from the response
    answer = response.replace("<OUT>", "").replace("<PAD>", "").replace('<EOS>', '')
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
