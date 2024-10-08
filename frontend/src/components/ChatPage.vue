<template>
  <div id="chat" class="flex flex-col justify-end bg-gray-50 h-[27rem] mx-4 my-4 rounded-lg shadow-lg relative">
    <div ref="chatContainer" class="carousel carousel-vertical overflow-y-auto">
      <div class="px-8" v-for="(msg, index) in messages" :key="index">
        <div :class="msg.isUser ? 'chat chat-end' : 'chat chat-start'" class="carousel-item">
          <div :class="msg.isUser ? 'hidden' : 'chat-image avatar'">
            <div class="w-10 rounded-full mb-4">
              <img alt="Tailwind CSS chat bubble component" src="https://cdn-icons-png.flaticon.com/128/6819/6819742.png" />
            </div>
          </div>
          <div :class="msg.isUser ? 'chat-image avatar' : 'hidden'">
            <div class="w-10 rounded-full mb-4">
              <img src="https://cdn-icons-png.flaticon.com/128/16683/16683419.png" alt="user" id="user" />
            </div>
          </div>
          <div class="chat-bubble text-gray-900 mb-4 text-lg p-4 drop-shadow shadow-md" :class="msg.isUser ? 'bg-[#FFC107] text-black' : 'bg-gray-200'">
            {{ msg.text }}
          </div>
        </div>
      </div>
      <div v-if="loading" class="px-8 chat chat-start">
        <div class="chat-image avatar">
          <div class="w-10 rounded-full mb-4">
            <img alt="Tailwind CSS chat bubble component" src="https://cdn-icons-png.flaticon.com/128/6819/6819742.png" />
          </div>
        </div>
        <div class="chat-bubble bg-gray-200 mb-4">
          <div class="loading loading-dots loading-md text-gray-700"></div>
        </div>
      </div>
    </div>
    <div v-if="alertMessage" class="text-error flex justify-center">
      <div class="p-2 rounded-lg shadow-lg">
        {{ alertMessage }}
      </div>
    </div>
    <div class="flex items-center justify-center w-full px-4 py-2 rounded-b-lg bg-gray-600 relative">
      <input
        v-model.trim="inputText"
        @input="updateSearchResults"
        @keyup.enter="sendMessage"
        type="text"
        class="input w-full rounded-full py-2 px-4 text-center text-gray-900"
        placeholder="ພິມຄຳຖາມຂອງທ່ານ..."
      />
      <ul v-if="searchResults.length" class="w-full rounded bg-gray-200 border border-gray-300 px-4 py-2 space-y-1 absolute z-10 bottom-full mt-2">
        <li
          v-for="(question, idx) in searchResults"
          :key="idx"
          class="cursor-pointer hover:bg-gray-100 p-1"
          @click="selectResult(question.name)"
        >
          {{ question.name }}
        </li>
      </ul>
      <button @click="sendMessage" class="ml-2 btn bg-[#FFC107] btn-circle border-0">
        <img src="https://img.icons8.com/?size=100&id=7874&format=png&color=FFFFFF" alt="share" width="22px" height="22px" />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick } from 'vue'
import jsonfile from '../assets/question.json'

interface Message {
  text: string
  isUser: boolean
}

interface Question {
  name: string
}

const inputText = ref<string>('')
const messages = ref<Message[]>([])
const alertMessage = ref<string | null>(null)
const inputError = ref<boolean>(false)
const loading = ref<boolean>(false)
const chatContainer = ref<HTMLElement | null>(null)
const searchResults = ref<Question[]>([])

const scrollToBottom = () => {
  if (chatContainer.value) {
    nextTick(() => {
      chatContainer.value!.scrollTop = chatContainer.value!.scrollHeight
    })
  }
}

const updateSearchResults = () => {
  if (inputText.value.trim() === '') {
    searchResults.value = []
    return
  }

  const results = jsonfile.filter(question =>
    question.name.toLowerCase().includes(inputText.value.toLowerCase())
  )
  searchResults.value = results.slice(0, 5)
}

const selectResult = (question: string) => {
  inputText.value = question
  searchResults.value = []
  sendMessage()
}

const sendMessage = async () => {
  if (inputText.value.trim() === '') {
    showAlert('ກະລຸນາປ້ອນຄຳຖາມ!')
    inputError.value = true
    return
  }

  inputError.value = false
  loading.value = true

  const message = inputText.value
  messages.value.push({ text: message, isUser: true })
  inputText.value = ''
  searchResults.value = []
  scrollToBottom()

  try {
    const response = await fetch('/api', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ input_text: message })
    })
    const data = await response.json()
    messages.value.push({ text: data.answer, isUser: false })
    scrollToBottom()
  } catch (error) {
    console.error('Error sending message:', error)
    showAlert('Error sending message')
  } finally {
    loading.value = false
    scrollToBottom()
  }
}

const showAlert = (message: string) => {
  alertMessage.value = message
  setTimeout(() => {
    alertMessage.value = null
  }, 3000)
}
</script>