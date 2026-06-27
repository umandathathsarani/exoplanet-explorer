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

const toggleFavorite = async () => {
  planetData.value.is_favorite = !planetData.value.is_favorite

  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/favorite`, {
      method: 'PATCH'
    })
    
    if (!response.ok) throw new Error("Failed to update database")
    
  } catch (error) {
    console.error("Favorite toggle failed:", error)
    planetData.value.is_favorite = !planetData.value.is_favorite
    alert("Communication failure: Could not save favorite status.")
  }
}
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
        <div class="flex items-start justify-between">
          <div>
            <h2 class="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-teal-300 to-blue-500 mb-2">
              {{ planetData.name }}
            </h2>
            <span class="inline-block bg-blue-900/50 text-blue-300 text-sm px-3 py-1 rounded-full border border-blue-700/50">
              Detected via {{ planetData.discovery_method }}
            </span>
          </div>
          
          <button @click="toggleFavorite" class="focus:outline-none transform hover:scale-110 transition-transform mt-1">
            <svg xmlns="http://www.w3.org/2000/svg" 
                 :class="planetData.is_favorite ? 'text-yellow-400 fill-yellow-400' : 'text-slate-600 fill-transparent hover:text-yellow-400/50'" 
                 class="w-10 h-10 transition-colors duration-300" 
                 viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
            </svg>
          </button>
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