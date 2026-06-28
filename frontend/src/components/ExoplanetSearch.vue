<script setup>
import { ref, watch } from 'vue'
import PlanetDetails from './PlanetDetails.vue'
import ExoplanetChart from './ExoplanetChart.vue'
import { authState, logout } from '../state.js'

const searchFilters = ref({
  method: '',
  maxDistance: 2000,
  minMass: 0.1
})

const showModal = ref(false)
const modalMessage = ref('')
const isError = ref(false)

// Debounced auto-search for real-time updates
let searchTimeout
watch(searchFilters, () => {
  clearTimeout(searchTimeout)
  searchTimeout = setTimeout(() => {
    handleSearch(true) // Pass a flag to avoid showing success modals on every slider tick
  }, 300)
}, { deep: true })


const searchResults = ref([])
const selectedPlanetId = ref(null)

const handleSearch = async (isSilent = false) => {
  try {
    const response = await fetch('http://localhost:8000/api/exoplanets/search', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authState.value.token}`
      },
      body: JSON.stringify(searchFilters.value)
    })

    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)

    const data = await response.json()
    searchResults.value = data.results
    
    isError.value = false
    modalMessage.value = data.message
    if (!isSilent) {
      showModal.value = true
    }

  } catch (error) {
    if (error.message.includes('401')) {
      logout(); 
      window.location.reload(); 
    }
    console.error(error)
    isError.value = true
    modalMessage.value = "Failed to connect to the backend. Is FastAPI running?"
    if (!isSilent) {
      showModal.value = true
    }
    searchResults.value = []
  }
}

const toggleFavorite = async (planet) => {

  planet.is_favorite = !planet.is_favorite

  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${planet.id}/favorite`, {
      method: 'PATCH',
      headers: { 'Authorization': `Bearer ${authState.value.token}` }
    })
    
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)
    
  } catch (error) {
    if (error.message.includes('401')) {
      logout(); 
      window.location.reload(); 
    }
    console.error("Favorite toggle failed:", error)
    planet.is_favorite = !planet.is_favorite
    alert("Communication failure: Could not save favorite status.")
  }
}
</script>

<template>
  <div class="pb-12">
    <div class="bg-[#222222] p-6 rounded-xl max-w-2xl mx-auto shadow-lg">
      <h2 class="text-2xl font-bold text-white mb-6">Cosmic Database Query</h2>
      
      <form @submit.prevent="handleSearch" class="space-y-6">
        <div>
          <label class="block text-sm font-semibold text-gray-300 mb-2">Discovery Method</label>
          <select v-model="searchFilters.method" class="w-full bg-[#333333] border border-gray-600 rounded-lg p-2.5 text-gray-100 focus:outline-none focus:border-[#00bfff]">
            <option value="">All Methods</option>
            <option value="Transit">Transit</option>
            <option value="Radial Velocity">Radial Velocity</option>
            <option value="Direct Imaging">Direct Imaging</option>
          </select>
        </div>

        <div>
          <div class="flex justify-between text-sm mb-2">
            <label class="font-semibold text-gray-300">Maximum Distance</label>
            <span class="text-[#00bfff] font-mono">{{ searchFilters.maxDistance }} light-years</span>
          </div>
          <input type="range" min="0" max="5000" step="10" v-model.number="searchFilters.maxDistance" class="w-full h-2 bg-[#444444] rounded-lg appearance-none cursor-pointer accent-[#00bfff]"/>
        </div>

        <div>
          <div class="flex justify-between text-sm mb-2">
            <label class="font-semibold text-gray-300">Minimum Planet Mass</label>
            <span class="text-[#00bfff] font-mono">{{ searchFilters.minMass }} M⊕</span>
          </div>
          <input type="range" min="0.1" max="30" step="0.1" v-model.number="searchFilters.minMass" class="w-full h-2 bg-[#444444] rounded-lg appearance-none cursor-pointer accent-[#00bfff]"/>
        </div>

        <button type="submit" class="w-full bg-[#00bfff] hover:bg-[#0099cc] text-white font-bold py-3 px-4 rounded-lg transition shadow-md">
          Scan Deep Space
        </button>
      </form>
    </div>

    <div v-if="searchResults.length > 0" class="mt-12 max-w-4xl mx-auto animate-in fade-in slide-in-from-bottom-4 duration-700">
      <h3 class="text-xl font-bold text-gray-100 mb-6 border-b border-gray-700 pb-2">
        Discovered Worlds ({{ searchResults.length }})
      </h3>
      
      <ExoplanetChart :planets="searchResults" class="mb-10" />

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div v-for="planet in searchResults" :key="planet.id" @click="selectedPlanetId = planet.id" class="bg-[#2d2d2d] hover:bg-[#333333] p-5 rounded-xl transition-all shadow-md group cursor-pointer border border-transparent hover:border-[#00bfff]">
          
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center gap-3">
              <button @click.stop="toggleFavorite(planet)" class="focus:outline-none transform hover:scale-110 transition-transform">
                <svg xmlns="http://www.w3.org/2000/svg" 
                     :class="planet.is_favorite ? 'text-yellow-400 fill-yellow-400' : 'text-gray-500 fill-transparent hover:text-yellow-400/50'" 
                     class="w-7 h-7 transition-colors duration-300" 
                     viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                </svg>
              </button>
              <h4 class="text-xl font-bold text-[#00bfff]">{{ planet.name }}</h4>
            </div>
            <span class="bg-[#1a1a1a] text-gray-300 text-xs px-2.5 py-1 rounded-md border border-gray-600">
              {{ planet.discovery_method }}
            </span>
          </div>
          
          <div class="space-y-2 text-sm text-gray-400">
            <div class="flex justify-between items-center">
              <span>Distance:</span>
              <span class="text-gray-200 font-mono">{{ planet.distance_ly }} LY</span>
            </div>
            <div class="flex justify-between items-center">
              <span>Mass:</span>
              <span class="text-gray-200 font-mono">{{ planet.mass_earth }} M⊕</span>
            </div>
            <div class="flex justify-between items-center">
              <span>Period:</span>
              <span class="text-gray-200 font-mono">{{ planet.orbital_period_days }} Days</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 transition-opacity">
      <div class="bg-[#2d2d2d] rounded-xl p-8 max-w-sm w-full shadow-2xl">
        <h3 :class="isError ? 'text-red-400' : 'text-[#00bfff]'" class="text-xl font-bold mb-3">
          {{ isError ? 'Error' : 'Success' }}
        </h3>
        <p class="text-gray-300 mb-6 text-sm">
          {{ modalMessage }}
        </p>
        <button @click="showModal = false" class="w-full bg-[#444444] hover:bg-[#555555] text-white font-semibold py-2 px-4 rounded-lg transition">
          Close
        </button>
      </div>
    </div>

    <PlanetDetails 
      v-if="selectedPlanetId !== null" 
      :planetId="selectedPlanetId" 
      @close="selectedPlanetId = null" 
    />
  </div>
</template>