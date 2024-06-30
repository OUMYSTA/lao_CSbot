<template>
    <div
      id="chat"
      class="overflow-auto h-100 flex flex-col justify-end bg-slate-400 h-96 mx-32 my-4 rounded-lg"
    >
      <div class="px-8" v-for="(msg, index) in messages" :key="index">
        <div :class="msg.isUser ? 'chat chat-end' : 'chat chat-start'">
          <div class="chat-bubble">{{ msg.text }}</div>
        </div>
      </div>
      <div class="flex justify-center mx-4 my-2 gap-4">
        <input
          v-model="inputText"
          @keyup.enter="sendMessage"
          type="text"
          placeholder="ພິມຄຳຖາມຂອງທ່ານ..."
          class="input input-bordered w-full text-center rounded-full"
        />
        <button class="btn btn-primary btn-circle" @click="sendMessage">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            fill="currentColor"
            class="bi bi-send"
            viewBox="0 0 16 16"
          >
            <path
              d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"
            />
          </svg>
        </button>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  
  const inputText = ref('');
  const messages = ref<{ text: string, isUser: boolean }[]>([]);
  
  const sendMessage = async () => {
    if (inputText.value.trim() === '') return;
    const message = inputText.value;
    messages.value.push({ text: message, isUser: true });
    inputText.value = '';
    try {
      const response = await fetch('/api', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input_text: message }),
      });
      const data = await response.json();
      messages.value.push({ text: data.answer, isUser: false });
      console.log(messages.value);
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };
  </script>
  