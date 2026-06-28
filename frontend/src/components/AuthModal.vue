<script setup>
import { ref } from 'vue'
import { login } from '../state.js'

const emit = defineEmits(['close'])
const isRegistering = ref(false)
const username = ref('')
const password = ref('')

const handleSubmit = async () => {
  const endpoint = isRegistering.value ? '/api/auth/register' : '/api/auth/login'
  
  const response = await fetch(`http://localhost:8000${endpoint}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ username: username.value, password: password.value })
  })

  if (response.ok) {
    const data = await response.json()
    login(data.access_token)
    emit('close')
  } else {
    alert("Authentication failed. Please check your credentials.")
  }
}
</script>

<template>
  <div class="fixed inset-0 z-[100] flex items-center justify-center bg-black/80 p-4">
    <div class="bg-[#2d2d2d] p-8 rounded-xl w-full max-w-sm border border-gray-700">
      <h2 class="text-2xl font-bold text-[#00bfff] mb-6">{{ isRegistering ? 'Register' : 'Login' }}</h2>
      
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