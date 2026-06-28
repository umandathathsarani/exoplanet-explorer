<script setup>
import { ref, watch, computed } from 'vue'
import PlanetDetails from './PlanetDetails.vue'
import ExoplanetChart from './ExoplanetChart.vue'
import { authState, logout } from '../state.js'

const searchFilters = ref({
  method: '',
  maxDistance: 2000,
  minMass: 0.1,
  page: 1,
  page_size: 20
})

const showModal = ref(false)
const modalMessage = ref('')
const isError = ref(false)

// Debounced auto-search for real-time updates
let searchTimeout
watch([() => searchFilters.value.maxDistance, () => searchFilters.value.minMass, () => searchFilters.value.method], () => {
  clearTimeout(searchTimeout)
  searchTimeout = setTimeout(() => {
    searchFilters.value.page = 1 // Reset to first page on filter change
    handleSearch(true) 
  }, 300)
})


const searchResults = ref([])
const selectedPlanetId = ref(null)
const totalPlanets = ref(0)
const totalPages = computed(() => Math.ceil(totalPlanets.value / searchFilters.value.page_size))

const nextPage = () => {
  if (searchFilters.value.page < totalPages.value) {
    searchFilters.value.page++
    handleSearch(true)
  }
}

const prevPage = () => {
  if (searchFilters.value.page > 1) {
    searchFilters.value.page--
    handleSearch(true)
  }
}

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
    totalPlanets.value = data.total || 0
    
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
    <!-- Desktop: Side by Side, Mobile: Stacked -->
    <div class="flex flex-col lg:flex-row gap-8">
      
      <!-- Left Sidebar: Search Form -->
      <div class="w-full lg:w-1/4">
        <div class="bg-black/60 backdrop-blur-xl p-6 rounded-2xl border border-white/20 shadow-2xl sticky top-8">
          <h2 class="text-2xl font-bold text-white mb-6">Cosmic Query</h2>
          
          <form @submit.prevent="handleSearch" class="space-y-6">
            <div>
              <label class="block text-sm font-semibold text-gray-300 mb-2">Discovery Method</label>
              <select v-model="searchFilters.method" class="w-full bg-black/40 border border-white/10 rounded-lg p-2.5 text-gray-100 focus:outline-none focus:border-[#00bfff] transition-colors">
                <option value="">All Methods</option>
                <option value="Transit">Transit</option>
                <option value="Radial Velocity">Radial Velocity</option>
                <option value="Direct Imaging">Direct Imaging</option>
              </select>
            </div>

            <div>
              <div class="flex justify-between text-sm mb-2">
                <label class="font-semibold text-gray-300">Max Distance</label>
                <span class="text-[#00bfff] font-mono">{{ searchFilters.maxDistance }} LY</span>
              </div>
              <input type="range" min="0" max="5000" step="10" v-model.number="searchFilters.maxDistance" class="w-full h-2 bg-white/20 rounded-lg appearance-none cursor-pointer accent-[#00bfff]"/>
            </div>

            <div>
              <div class="flex justify-between text-sm mb-2">
                <label class="font-semibold text-gray-300">Min Mass</label>
                <span class="text-[#00bfff] font-mono">{{ searchFilters.minMass }} M⊕</span>
              </div>
              <input type="range" min="0.1" max="30" step="0.1" v-model.number="searchFilters.minMass" class="w-full h-2 bg-white/20 rounded-lg appearance-none cursor-pointer accent-[#00bfff]"/>
            </div>

            <button type="submit" class="w-full bg-gradient-to-r from-[#00bfff] to-blue-600 hover:to-blue-500 text-white font-bold py-3 px-4 rounded-lg transition-all shadow-lg transform hover:-translate-y-1">
              Scan Deep Space
            </button>
          </form>
        </div>
      </div>

      <!-- Right Main Content: Chart & Results Grid -->
      <div class="w-full lg:w-3/4 flex flex-col">
        <div v-if="searchResults.length > 0" class="animate-in fade-in slide-in-from-bottom-4 duration-700">
          
          <ExoplanetChart :planets="searchResults" class="mb-10 w-full" />

          <h3 class="text-xl font-bold text-gray-100 mb-6 border-b border-white/10 pb-2 flex items-center gap-3">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Discovered Worlds ({{ searchResults.length }})
          </h3>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <div v-for="planet in searchResults" :key="planet.id" @click="selectedPlanetId = planet.id" class="bg-black/60 backdrop-blur-xl p-5 rounded-xl transition-all shadow-lg group cursor-pointer border border-white/20 hover:border-[#00bfff] hover:bg-black/80 relative overflow-hidden">
              <div class="absolute -right-10 -top-10 w-24 h-24 bg-[#00bfff]/20 rounded-full blur-2xl group-hover:bg-[#00bfff]/40 transition-colors pointer-events-none"></div>
              
              <div class="flex items-start justify-between mb-4 relative z-10">
                <div class="flex items-center gap-3">
                  <button @click.stop="toggleFavorite(planet)" class="focus:outline-none transform hover:scale-125 transition-transform">
                    <svg xmlns="http://www.w3.org/2000/svg" 
                         :class="planet.is_favorite ? 'text-yellow-400 fill-yellow-400' : 'text-gray-500 fill-transparent hover:text-yellow-400/50'" 
                         class="w-7 h-7 transition-colors duration-300 drop-shadow-md" 
                         viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                    </svg>
                  </button>
                  <h4 class="text-xl font-bold text-[#00bfff] group-hover:text-white transition-colors">{{ planet.name }}</h4>
                </div>
              </div>
              
              <span class="inline-block bg-black/60 text-gray-300 text-xs px-2.5 py-1 rounded-full border border-white/20 mb-3 relative z-10">
                {{ planet.discovery_method }}
              </span>
              
              <div class="space-y-2 text-sm text-gray-400 relative z-10">
                <div class="flex justify-between items-center border-b border-white/5 pb-1">
                  <span>Distance:</span>
                  <span class="text-gray-200 font-mono">{{ planet.distance_ly }} LY</span>
                </div>
                <div class="flex justify-between items-center border-b border-white/5 pb-1">
                  <span>Mass:</span>
                  <span class="text-gray-200 font-mono">{{ planet.mass_earth }} M⊕</span>
                </div>
                <div class="flex justify-between items-center pb-1">
                  <span>Period:</span>
                  <span class="text-gray-200 font-mono">{{ planet.orbital_period_days }} d</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Pagination Controls -->
          <div class="flex justify-between items-center mt-10 bg-black/60 backdrop-blur-xl p-4 rounded-xl shadow-lg border border-white/20">
            <button 
              @click="prevPage" 
              :disabled="searchFilters.page <= 1"
              class="px-6 py-2 rounded-lg font-bold transition flex items-center gap-2"
              :class="searchFilters.page <= 1 ? 'bg-black/30 text-gray-600 cursor-not-allowed' : 'bg-[#00bfff]/20 text-[#00bfff] hover:bg-[#00bfff]/40 border border-[#00bfff]/50'"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
              Previous
            </button>
            
            <div class="text-gray-300 font-mono bg-black/60 px-4 py-1.5 rounded-full border border-white/20">
              Page <span class="text-[#00bfff] font-bold">{{ searchFilters.page }}</span> / <span class="text-white font-bold">{{ totalPages }}</span>
            </div>
            
            <button 
              @click="nextPage" 
              :disabled="searchFilters.page >= totalPages"
              class="px-6 py-2 rounded-lg font-bold transition flex items-center gap-2"
              :class="searchFilters.page >= totalPages ? 'bg-black/30 text-gray-600 cursor-not-allowed' : 'bg-[#00bfff]/20 text-[#00bfff] hover:bg-[#00bfff]/40 border border-[#00bfff]/50'"
            >
              Next
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
              </svg>
            </button>
          </div>

        </div>
      </div>
    </div>

    <!-- Modals -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm transition-opacity">
      <div class="bg-indigo-950/80 backdrop-blur-xl border border-white/20 rounded-2xl p-8 max-w-sm w-full shadow-2xl">
        <h3 :class="isError ? 'text-red-400' : 'text-[#00bfff]'" class="text-xl font-bold mb-3">
          {{ isError ? 'Error' : 'Success' }}
        </h3>
        <p class="text-gray-200 mb-6 text-sm">
          {{ modalMessage }}
        </p>
        <button @click="showModal = false" class="w-full bg-white/10 hover:bg-white/20 border border-white/20 text-white font-semibold py-2 px-4 rounded-lg transition">
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