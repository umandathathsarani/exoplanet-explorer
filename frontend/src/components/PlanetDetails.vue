<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  planetId: Number
})

const emit = defineEmits(['close'])

const planetData = ref(null)
const loading = ref(true)

onMounted(async () => {
  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${props.planetId}`)
    if (!response.ok) throw new Error("Failed to fetch details")
    planetData.value = await response.json()
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="fixed inset-0 z-50 flex justify-end bg-black/60 backdrop-blur-sm transition-all">
    <div class="w-full max-w-lg h-full bg-slate-900 border-l border-slate-700 p-8 shadow-2xl overflow-y-auto animate-in slide-in-from-right duration-300">
      
      <button @click="emit('close')" class="mb-6 text-slate-400 hover:text-white flex items-center gap-2 transition">
        ← Return to Database
      </button>

      <div v-if="loading" class="text-blue-400 font-mono animate-pulse mt-12">
        Accessing planetary archives...
      </div>

      <div v-else-if="planetData" class="space-y-8">
        <div>
          <h2 class="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-teal-300 to-blue-500 mb-2">
            {{ planetData.name }}
          </h2>
          <span class="inline-block bg-blue-900/50 text-blue-300 text-sm px-3 py-1 rounded-full border border-blue-700/50">
            Detected via {{ planetData.discovery_method }}
          </span>
        </div>

        <div class="bg-slate-800 rounded-xl p-5 border border-slate-700">
          <h3 class="text-lg font-bold text-slate-200 mb-4 border-b border-slate-700 pb-2">Planetary Profile</h3>
          <div class="space-y-3 font-mono text-sm">
            <div class="flex justify-between"><span class="text-slate-400">Mass:</span> <span class="text-teal-300">{{ planetData.mass_earth }} Earths</span></div>
            <div class="flex justify-between"><span class="text-slate-400">Year Length:</span> <span class="text-teal-300">{{ planetData.orbital_period_days }} Days</span></div>
            <div class="flex justify-between"><span class="text-slate-400">Distance:</span> <span class="text-teal-300">{{ planetData.distance_ly }} Light Years</span></div>
          </div>
        </div>

        <div class="bg-indigo-950/30 rounded-xl p-5 border border-indigo-900/50">
          <h3 class="text-lg font-bold text-indigo-300 mb-4 border-b border-indigo-900/50 pb-2">Host Star: {{ planetData.host_star.name }}</h3>
          <div class="space-y-3 font-mono text-sm">
            <div class="flex justify-between"><span class="text-slate-400">Temperature:</span> <span class="text-indigo-200">{{ planetData.host_star.temperature_k }} K</span></div>
            <div class="flex justify-between"><span class="text-slate-400">Luminosity:</span> <span class="text-indigo-200">{{ planetData.host_star.luminosity }} (vs Sun)</span></div>
          </div>
        </div>

        <button class="w-full bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-300 py-3 rounded-lg transition-colors mt-8">
          Request AI Analysis (Coming Soon)
        </button>
      </div>
    </div>
  </div>
</template>