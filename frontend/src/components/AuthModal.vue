<script setup>
import { ref } from 'vue'
import { login } from '../state.js'

const emit = defineEmits(['close'])
const isRegistering = ref(false)
const username = ref('')
const password = ref('')
const errorMessage = ref('')

const handleSubmit = async () => {
  errorMessage.value = ''
  
  const isReg = isRegistering.value
  const endpoint = isReg ? '/api/auth/register' : '/api/auth/login'
  
  let body, headers;
  if (isReg) {
    headers = { 'Content-Type': 'application/json' }
    body = JSON.stringify({ username: username.value, password: password.value })
  } else {
    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
    body = new URLSearchParams({ username: username.value, password: password.value })
  }

  try {
    const response = await fetch(`http://localhost:8000${endpoint}`, {
      method: 'POST',
      headers: headers,
      body: body
    })

    if (response.ok) {
      const data = await response.json()
      login(data.access_token)
      emit('close')
      window.location.reload() 
    } else {
      const errorData = await response.json()
      errorMessage.value = errorData.detail || "Authentication failed."
    }
  } catch (error) {
    errorMessage.value = "Could not reach the server."
  }
}
</script>

<template>
  <div class="fixed inset-0 z-[100] flex items-center justify-center bg-black/80 p-4">
    <div class="bg-[#2d2d2d] p-8 rounded-xl w-full max-w-sm border border-gray-700 shadow-2xl">
      <h2 class="text-2xl font-bold text-[#00bfff] mb-6">{{ isRegistering ? 'Register' : 'Login' }}</h2>
      
      <div v-if="errorMessage" class="mb-4 p-3 bg-red-900/30 border border-red-500 text-red-200 text-sm rounded">
        {{ errorMessage }}
      </div>
      
      <form @submit.prevent="handleSubmit" class="space-y-4">
        <input v-model="username" placeholder="Username" class="w-full p-3 bg-[#1a1a1a] border border-gray-600 rounded-lg text-white" required />
        <input v-model="password" type="password" placeholder="Password" class="w-full p-3 bg-[#1a1a1a] border border-gray-600 rounded-lg text-white" required />
        
        <button class="w-full bg-[#00bfff] text-white py-3 rounded-lg font-bold hover:bg-[#0099cc] transition">
          {{ isRegistering ? 'Create Account' : 'Sign In' }}
        </button>
      </form>
      
      <button @click="isRegistering = !isRegistering" class="w-full mt-4 text-gray-400 text-sm hover:underline">
        {{ isRegistering ? 'Already have an account? Login' : 'Need an account? Register' }}
      </button>
    </div>
  </div>
</template>