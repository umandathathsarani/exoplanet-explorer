<script setup>
import ExoplanetSearch from './components/ExoplanetSearch.vue'
import AuthModal from './components/AuthModal.vue'
import Dashboard from './components/Dashboard.vue'
import { authState, logout } from './state.js'
import { ref, watch } from 'vue'

const showAuth = ref(false)
const currentView = ref('search')

watch(() => authState.value.isAuthenticated, (isAuth) => {
  if (!isAuth && currentView.value === 'dashboard') {
    currentView.value = 'search'
  }
})
</script>

<template>
  <div class="min-h-screen bg-[#1a1a1a] text-gray-200 font-sans p-8">
    <header class="flex flex-col md:flex-row justify-between items-center mb-12 gap-6">
      <h1 class="text-4xl font-extrabold text-[#00bfff]">Exoplanet Explorer</h1>
      <nav class="flex gap-6 items-center">
        <button 
          @click="currentView = 'search'" 
          :class="currentView === 'search' ? 'text-[#00bfff] border-b-2 border-[#00bfff]' : 'text-gray-400 hover:text-gray-200'"
          class="pb-1 font-semibold transition"
        >
          Search
        </button>
        <button 
          v-if="authState.isAuthenticated"
          @click="currentView = 'dashboard'" 
          :class="currentView === 'dashboard' ? 'text-[#00bfff] border-b-2 border-[#00bfff]' : 'text-gray-400 hover:text-gray-200'"
          class="pb-1 font-semibold transition"
        >
          My Observatory
        </button>
        <div class="w-px h-6 bg-gray-600 mx-2"></div>
        <button v-if="!authState.isAuthenticated" @click="showAuth = true" class="text-gray-300 hover:text-[#00bfff] font-semibold">Login</button>
        <button v-else @click="logout" class="text-gray-300 hover:text-red-400 font-semibold">Logout</button>
      </nav>
    </header>
    <main class="container mx-auto">
      <ExoplanetSearch v-if="currentView === 'search'" />
      <Dashboard v-if="currentView === 'dashboard'" />
      <AuthModal v-if="showAuth" @close="showAuth = false" />
    </main>
  </div>
</template>