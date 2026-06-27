<script setup>
import ExoplanetSearch from './components/ExoplanetSearch.vue'
</script>

<template>
  <div class="min-h-screen bg-slate-900 text-slate-100 font-sans p-8">
    <header class="text-center mb-12">
      <h1 class="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-teal-300 mb-2">
        Exoplanet Explorer
      </h1>
      <p class="text-slate-400">The Exoplanet Analyst AI is standing by...</p>
    </header>

    <main class="container mx-auto px-4">
      <ExoplanetSearch />
    </main>
  </div>
</template>