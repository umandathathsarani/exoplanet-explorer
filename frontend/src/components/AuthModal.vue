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
  
  let body = JSON.stringify({ username: username.value, password: password.value })
  let headers = { 'Content-Type': 'application/json' }

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
  <div class="fixed inset-0 z-[100] flex items-center justify-center bg-black/80 backdrop-blur-sm p-4">
    <div class="bg-black/60 backdrop-blur-2xl p-8 rounded-2xl w-full max-w-sm border border-white/20 shadow-2xl relative">
      <button @click="emit('close')" class="absolute top-4 right-4 text-gray-400 hover:text-white transition">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
      </button>
      <h2 class="text-2xl font-bold text-white mb-6">{{ isRegistering ? 'Register' : 'Login' }}</h2>
      
      <div v-if="errorMessage" class="mb-4 p-3 bg-red-900/30 border border-red-500 text-red-200 text-sm rounded">
        {{ errorMessage }}
      </div>
      
      <form @submit.prevent="handleSubmit" class="space-y-5 mt-4">
        <div class="relative">
          <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20" fill="currentColor">
              <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
              <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
            </svg>
          </div>
          <input v-model="username" type="email" placeholder="Email" class="w-full py-3 pl-12 pr-4 bg-white/20 border border-transparent rounded-lg text-white placeholder-gray-400 focus:outline-none focus:bg-white/30 focus:border-white/50 transition-all" required />
        </div>
        
        <div class="relative">
          <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
            </svg>
          </div>
          <input v-model="password" type="password" placeholder="Password" class="w-full py-3 pl-12 pr-4 bg-white/20 border border-transparent rounded-lg text-white placeholder-gray-400 focus:outline-none focus:bg-white/30 focus:border-white/50 transition-all" required />
        </div>
        
        <button class="w-full bg-black text-white py-3 rounded-lg text-lg font-medium hover:bg-gray-900 border border-gray-800 transition-colors shadow-lg">
          {{ isRegistering ? 'Register' : 'Login' }}
        </button>
      </form>
      
      <div class="flex items-center my-6">
        <div class="flex-grow border-t border-white/30"></div>
        <span class="mx-4 text-white/50 text-sm">OR</span>
        <div class="flex-grow border-t border-white/30"></div>
      </div>
      
      <button @click="isRegistering = !isRegistering" class="w-full bg-transparent text-white py-3 rounded-lg text-lg font-medium border border-white/30 hover:bg-white/10 transition-colors">
        {{ isRegistering ? 'Login Instead' : 'Create An Account' }}
      </button>
    </div>
  </div>
</template>