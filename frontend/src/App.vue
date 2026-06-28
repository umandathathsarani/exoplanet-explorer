<script setup>
import ExoplanetSearch from './components/ExoplanetSearch.vue'
import AuthModal from './components/AuthModal.vue'
import { authState, logout } from './state.js'
import { ref } from 'vue'

const showAuth = ref(false)
</script>

<template>
  <div class="min-h-screen bg-[#1a1a1a] text-gray-200 font-sans p-8">
    <header class="flex justify-between items-center mb-12">
      <div>
        <h1 class="text-4xl font-extrabold text-[#00bfff]">Exoplanet Explorer</h1>
      </div>
      <div class="flex gap-4">
        <button v-if="!authState.isAuthenticated" @click="showAuth = true" class="text-gray-300 hover:text-[#00bfff]">Login</button>
        <button v-else @click="logout" class="text-gray-300 hover:text-red-400">Logout</button>
      </div>
    </header>

    <main class="container mx-auto">
      <ExoplanetSearch />
      <AuthModal v-if="showAuth" @close="showAuth = false" />
    </main>
  </div>
</template>