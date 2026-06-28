<script setup>
import ExoplanetSearch from './components/ExoplanetSearch.vue'
import AuthModal from './components/AuthModal.vue'
import Dashboard from './components/Dashboard.vue'
import LandingPage from './components/LandingPage.vue'
import Lecture from './components/Lecture.vue'
import { authState, logout } from './state.js'
import { ref, watch } from 'vue'

const showAuth = ref(false)
const currentView = ref('home')

watch(() => authState.value.isAuthenticated, (isAuth) => {
  if (!isAuth && currentView.value === 'dashboard') {
    currentView.value = 'search'
  }
})
</script>

<template>
  <div class="min-h-screen bg-transparent text-gray-200 font-sans p-4 md:p-8 overflow-x-hidden">
    <header class="flex flex-col md:flex-row justify-between items-center mb-12 gap-6">
      <h1 class="text-4xl font-extrabold text-white tracking-tight">Exoplanet Explorer</h1>
      <nav class="flex gap-6 items-center bg-black/60 backdrop-blur-xl px-6 py-3 rounded-full border border-white/20 shadow-lg">
        <button 
          @click="currentView = 'home'" 
          :class="currentView === 'home' ? 'text-[#00bfff]' : 'text-gray-300 hover:text-white'"
          class="font-semibold transition flex items-center gap-2"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z" /></svg>
          Home
        </button>
        <button 
          @click="currentView = 'lecture'" 
          :class="currentView === 'lecture' ? 'text-[#00bfff]' : 'text-gray-300 hover:text-white'"
          class="font-semibold transition"
        >
          Learn
        </button>
        <button 
          @click="currentView = 'search'" 
          :class="currentView === 'search' ? 'text-[#00bfff]' : 'text-gray-300 hover:text-white'"
          class="font-semibold transition"
        >
          Search
        </button>
        <button 
          v-if="authState.isAuthenticated"
          @click="currentView = 'dashboard'" 
          :class="currentView === 'dashboard' ? 'text-[#00bfff]' : 'text-gray-300 hover:text-white'"
          class="font-semibold transition"
        >
          My Observatory
        </button>
        <div class="w-px h-6 bg-gray-600 mx-2"></div>
        <button v-if="!authState.isAuthenticated" @click="showAuth = true" class="text-gray-300 hover:text-[#00bfff] font-semibold">Login</button>
        <button v-else @click="logout" class="text-gray-300 hover:text-red-400 font-semibold">Logout</button>
      </nav>
    </header>
    <main class="w-full max-w-[1920px] mx-auto">
      <LandingPage v-if="currentView === 'home'" @start="currentView = 'search'" />
      <Lecture v-if="currentView === 'lecture'" />
      <ExoplanetSearch v-if="currentView === 'search'" />
      <Dashboard v-if="currentView === 'dashboard'" />
      <AuthModal v-if="showAuth" @close="showAuth = false" />
    </main>
  </div>
</template>