<script setup>
import { ref, onMounted } from 'vue'
import { authState, logout } from '../state.js'
import PlanetDetails from './PlanetDetails.vue'

const loading = ref(true)
const dashboardData = ref({ favorites: [], notes: [] })
const errorMessage = ref('')
const selectedPlanetId = ref(null)

const fetchDashboard = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/dashboard', {
      headers: { 'Authorization': `Bearer ${authState.value.token}` }
    })
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)
    const data = await response.json()
    dashboardData.value = data
  } catch (error) {
    if (error.message.includes('401')) {
      logout()
      window.location.reload()
    }
    errorMessage.value = "Failed to load observatory data."
    console.error(error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  if (authState.value.isAuthenticated) {
    fetchDashboard()
  }
})

const handleModalClose = () => {
  selectedPlanetId.value = null
  fetchDashboard()
}
</script>

<template>
  <div class="pb-12 animate-in fade-in slide-in-from-bottom-4 duration-700">
    <div class="mb-12">
      <h2 class="text-3xl font-bold text-white mb-2">My Observatory</h2>
      <p class="text-gray-400">Your personalized collection of celestial discoveries.</p>
    </div>

    <div v-if="loading" class="flex justify-center py-20">
      <div class="text-[#00bfff] font-mono animate-pulse">Syncing with orbital database...</div>
    </div>

    <div v-else-if="errorMessage" class="bg-red-900/30 border border-red-500 text-red-200 p-6 rounded-xl">
      {{ errorMessage }}
    </div>

    <div v-else class="space-y-16">
      
      <!-- Favorites Section -->
      <section>
        <h3 class="text-2xl font-bold text-gray-100 mb-6 border-b border-gray-700 pb-2 flex items-center gap-3">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-yellow-400 fill-yellow-400" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
          </svg>
          Favorited Planets
        </h3>
        
        <div v-if="dashboardData.favorites.length === 0" class="text-gray-500 italic bg-[#222222] p-8 rounded-xl border border-gray-800 text-center">
          You haven't bookmarked any planets yet. Search the database to find your first favorite!
        </div>
        
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="planet in dashboardData.favorites" :key="'fav-'+planet.id" @click="selectedPlanetId = planet.id" class="bg-gradient-to-br from-[#2d2d2d] to-[#1f1f1f] hover:from-[#333333] hover:to-[#2a2a2a] p-5 rounded-xl transition-all shadow-lg cursor-pointer border border-gray-700 hover:border-[#00bfff]">
            <h4 class="text-xl font-bold text-[#00bfff] mb-2">{{ planet.name }}</h4>
            <div class="space-y-1 text-sm text-gray-400 font-mono">
              <p>Type: <span class="text-gray-200">{{ planet.discovery_method }}</span></p>
              <p>Dist: <span class="text-gray-200">{{ planet.distance_ly }} LY</span></p>
              <p>Mass: <span class="text-gray-200">{{ planet.mass_earth }} M⊕</span></p>
            </div>
          </div>
        </div>
      </section>

      <!-- Notes Section -->
      <section>
        <h3 class="text-2xl font-bold text-gray-100 mb-6 border-b border-gray-700 pb-2 flex items-center gap-3">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
          </svg>
          Research Notes
        </h3>
        
        <div v-if="dashboardData.notes.length === 0" class="text-gray-500 italic bg-[#222222] p-8 rounded-xl border border-gray-800 text-center">
          No research notes found. Add notes to planets to see them appear here.
        </div>
        
        <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div v-for="noteObj in dashboardData.notes" :key="'note-'+noteObj.id" @click="selectedPlanetId = noteObj.id" class="bg-gradient-to-br from-[#222222] to-[#1a1a1a] p-6 rounded-xl transition-all shadow-md cursor-pointer border border-gray-800 hover:border-[#00bfff] group relative overflow-hidden">
            <div class="absolute top-0 right-0 w-16 h-16 bg-[#00bfff]/10 rounded-bl-full group-hover:bg-[#00bfff]/20 transition-colors"></div>
            <h4 class="text-lg font-bold text-gray-200 mb-3">{{ noteObj.name }}</h4>
            <p class="text-gray-400 text-sm italic border-l-2 border-[#00bfff] pl-3 min-h-[40px] line-clamp-3">
              "{{ noteObj.note_content }}"
            </p>
          </div>
        </div>
      </section>

    </div>

    <PlanetDetails 
      v-if="selectedPlanetId !== null" 
      :planetId="selectedPlanetId" 
      @close="handleModalClose" 
    />
  </div>
</template>
