<script setup>
import { ref } from 'vue'
import PlanetDetails from './PlanetDetails.vue'

const searchFilters = ref({
  method: '',
  maxDistance: 2000,
  minMass: 0.1
})

const showModal = ref(false)
const modalMessage = ref('')
const isError = ref(false)

const searchResults = ref([])
const selectedPlanetId = ref(null)

const handleSearch = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/exoplanets/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(searchFilters.value)
    })

    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)

    const data = await response.json()
    searchResults.value = data.results
    
    isError.value = false
    modalMessage.value = data.message
    showModal.value = true

  } catch (error) {
    console.error(error)
    isError.value = true
    modalMessage.value = "Failed to connect to the backend. Is FastAPI running?"
    showModal.value = true
    searchResults.value = []
  }
}

const toggleFavorite = async (planet) => {

  planet.is_favorite = !planet.is_favorite

  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${planet.id}/favorite`, {
      method: 'PATCH'
    })
    
    if (!response.ok) throw new Error("Failed to update database")
    
  } catch (error) {
    console.error("Favorite toggle failed:", error)
    planet.is_favorite = !planet.is_favorite
    alert("Communication failure: Could not save favorite status.")
  }
}
</script>

<template>
  <div class="pb-12">
    <div class="bg-slate-800/50 border border-slate-700/60 p-6 rounded-xl backdrop-blur-md max-w-2xl mx-auto shadow-xl">
      <h2 class="text-2xl font-bold text-blue-400 mb-6">Cosmic Database Query</h2>
      
      <form @submit.prevent="handleSearch" class="space-y-6">
        <div>
          <label class="block text-sm font-semibold text-slate-300 mb-2">Discovery Method</label>
          <select v-model="searchFilters.method" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-slate-200 focus:outline-none focus:border-blue-500">
            <option value="">All Methods</option>
            <option value="Transit">Transit</option>
            <option value="Radial Velocity">Radial Velocity</option>
            <option value="Direct Imaging">Direct Imaging</option>
          </select>
        </div>

        <div>
          <div class="flex justify-between text-sm mb-2">
            <label class="font-semibold text-slate-300">Maximum Distance</label>
            <span class="text-blue-400 font-mono">{{ searchFilters.maxDistance }} light-years</span>
          </div>
          <input type="range" min="0" max="5000" step="10" v-model.number="searchFilters.maxDistance" class="w-full h-2 bg-slate-900 rounded-lg appearance-none cursor-pointer accent-blue-500"/>
        </div>

        <div>
          <div class="flex justify-between text-sm mb-2">
            <label class="font-semibold text-slate-300">Minimum Planet Mass</label>
            <span class="text-blue-400 font-mono">{{ searchFilters.minMass }} M⊕ (Earth Masses)</span>
          </div>
          <input type="range" min="0.1" max="30" step="0.1" v-model.number="searchFilters.minMass" class="w-full h-2 bg-slate-900 rounded-lg appearance-none cursor-pointer accent-blue-500"/>
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-blue-500 to-indigo-600 hover:from-blue-600 hover:to-indigo-700 text-white font-bold py-3 px-4 rounded-lg transition shadow-md hover:shadow-indigo-500/20">
          Scan Deep Space
        </button>
      </form>
    </div>

    <div v-if="searchResults.length > 0" class="mt-12 max-w-4xl mx-auto animate-in fade-in slide-in-from-bottom-4 duration-700">
      <h3 class="text-xl font-bold text-slate-200 mb-6 border-b border-slate-700 pb-2">
        Discovered Worlds ({{ searchResults.length }})
      </h3>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div v-for="planet in searchResults" :key="planet.id" @click="selectedPlanetId = planet.id" class="bg-slate-800 border border-slate-700 hover:border-blue-500/50 p-5 rounded-xl transition-all shadow-lg hover:shadow-blue-900/20 group relative overflow-hidden cursor-pointer">
          
          <div class="absolute top-0 right-0 w-32 h-32 bg-blue-500/5 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"></div>

          <div class="flex items-center justify-between mb-4 relative z-10">
            <div class="flex items-center gap-3">
              <button @click.stop="toggleFavorite(planet)" class="focus:outline-none transform hover:scale-110 transition-transform">
                <svg xmlns="http://www.w3.org/2000/svg" 
                     :class="planet.is_favorite ? 'text-yellow-400 fill-yellow-400' : 'text-slate-600 fill-transparent hover:text-yellow-400/50'" 
                     class="w-7 h-7 transition-colors duration-300" 
                     viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                </svg>
              </button>
              <h4 class="text-xl font-bold text-teal-300 group-hover:text-teal-200 transition-colors">{{ planet.name }}</h4>
            </div>
            
            <span class="bg-blue-900/50 text-blue-300 text-xs px-2.5 py-1 rounded-md border border-blue-700/50 shadow-sm">
              {{ planet.discovery_method }}
            </span>
          </div>
          
          <div class="space-y-3 text-sm text-slate-400 relative z-10">
            <div class="flex justify-between items-center bg-slate-900/50 p-2 rounded-lg">
              <span>Distance from Earth:</span>
              <span class="text-slate-200 font-mono font-medium">{{ planet.distance_ly }} LY</span>
            </div>
            <div class="flex justify-between items-center bg-slate-900/50 p-2 rounded-lg">
              <span>Planet Mass:</span>
              <span class="text-slate-200 font-mono font-medium">{{ planet.mass_earth }} M⊕</span>
            </div>
            <div class="flex justify-between items-center bg-slate-900/50 p-2 rounded-lg">
              <span>Orbital Period:</span>
              <span class="text-slate-200 font-mono font-medium">{{ planet.orbital_period_days }} Days</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm transition-opacity">
      <div class="bg-slate-800 border border-slate-700 rounded-2xl p-8 max-w-sm w-full shadow-2xl">
        <h3 :class="isError ? 'text-red-400' : 'text-emerald-400'" class="text-2xl font-bold mb-3">
          {{ isError ? 'Transmission Failed' : 'Connection Successful!' }}
        </h3>
        <p class="text-slate-300 mb-6 font-mono text-sm border-l-2 border-slate-600 pl-3">
          {{ modalMessage }}
        </p>
        <button @click="showModal = false" class="w-full bg-slate-700 hover:bg-slate-600 text-white font-semibold py-2 px-4 rounded-lg transition">
          Acknowledge
        </button>
      </div>
    </div>

    <PlanetDetails v-if="selectedPlanetId" :planetId="selectedPlanetId" @close="selectedPlanetId = null" />
  </div>
</template>