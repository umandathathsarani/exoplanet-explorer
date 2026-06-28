<script setup>
import ExoplanetSearch from './components/ExoplanetSearch.vue'
</script>

<template>
  <div class="min-h-screen bg-[#1a1a1a] text-gray-200 font-sans p-8">
    <header class="text-center mb-12">
      <h1 class="text-4xl font-extrabold text-[#00bfff] mb-2">
        Exoplanet Explorer
      </h1>
      <p class="text-gray-400">The Exoplanet Analyst AI is standing by...</p>
    </header>

    <main class="container mx-auto px-4">
      <ExoplanetSearch />
    </main>
  </div>
</template>