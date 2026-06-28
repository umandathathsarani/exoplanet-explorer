<script setup>
import { ref, onMounted } from 'vue'
import { authState, logout } from '../state.js'

const props = defineProps({ planetId: Number })
const emit = defineEmits(['close'])

const planetData = ref(null)
const researchNote = ref('')
const isEditing = ref(false)
const showDeleteConfirm = ref(false)
const loading = ref(true)

const aiAnalysis = ref('')
const isAnalyzing = ref(false)
const errorMessage = ref('')

onMounted(async () => {
  if (!props.planetId) return;

  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${props.planetId}`, {
      headers: { 'Authorization': `Bearer ${authState.value.token}` }
    })
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)
    planetData.value = await response.json()
    researchNote.value = planetData.value.note
  } catch (error) {
    if (error.message.includes('401')) {
      logout(); 
      window.location.reload(); 
    }
    console.error("Load failed:", error)
  } finally {
    loading.value = false
  }
})

const saveNote = async () => {
  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/note`, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authState.value.token}` 
      },
      body: JSON.stringify({ content: researchNote.value })
    })
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)
    planetData.value.note = researchNote.value
    isEditing.value = false
  } catch (error) {
    if (error.message.includes('401')) { logout(); window.location.reload(); }
    console.error("Save note failed:", error)
  }
}

const deleteNote = async () => {
  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/note`, { 
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${authState.value.token}` }
    })
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)
    researchNote.value = ''
    planetData.value.note = ''
    showDeleteConfirm.value = false
    isEditing.value = false
  } catch (error) {
    if (error.message.includes('401')) { logout(); window.location.reload(); }
    console.error("Delete note failed:", error)
  }
}

const toggleFavorite = async () => {
  planetData.value.is_favorite = !planetData.value.is_favorite
  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/favorite`, { 
      method: 'PATCH',
      headers: { 'Authorization': `Bearer ${authState.value.token}` }
    })
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)
  } catch (error) {
    if (error.message.includes('401')) {
      logout(); 
      window.location.reload(); 
    }
    planetData.value.is_favorite = !planetData.value.is_favorite
    alert("Could not update favorite status.")
  }
}

const requestAnalysis = async () => {
  isAnalyzing.value = true
  errorMessage.value = ''
  aiAnalysis.value = ''
  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/analyze`, {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${authState.value.token}` }
    })
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)
    const data = await response.json()
    aiAnalysis.value = data.analysis
  } catch (error) {
    if (error.message.includes('401')) {
      logout(); 
      window.location.reload(); 
    }
    errorMessage.value = "We couldn't reach the AI observatory. Please check your connection."
  } finally {
    isAnalyzing.value = false
  }
}
</script>

<template>
  <div class="fixed inset-0 z-50 flex justify-end bg-black/80 backdrop-blur-md transition-opacity">
    <div class="w-full max-w-lg h-full bg-indigo-950/95 backdrop-blur-2xl border-l border-white/20 p-8 overflow-y-auto shadow-2xl">
      <button @click="emit('close')" class="mb-6 text-gray-400 hover:text-white transition flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" /></svg>
        Return to Database
      </button>

      <div v-if="loading" class="text-[#00bfff] font-mono animate-pulse mt-12 flex flex-col items-center gap-4">
        <div class="w-12 h-12 border-4 border-[#00bfff] border-t-transparent rounded-full animate-spin"></div>
        Accessing planetary archives...
      </div>

      <div v-else-if="planetData" class="space-y-8">
        <div class="flex items-start justify-between">
          <h2 class="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-[#00bfff] to-blue-400 drop-shadow-md">{{ planetData.name }}</h2>
          <button @click="toggleFavorite" class="mt-1 transition-transform hover:scale-125 focus:outline-none">
            <svg xmlns="http://www.w3.org/2000/svg" :class="planetData.is_favorite ? 'text-yellow-400 fill-yellow-400 drop-shadow-[0_0_8px_rgba(250,204,21,0.6)]' : 'text-gray-500 hover:text-gray-300'" class="w-10 h-10 transition-colors" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
            </svg>
          </button>
        </div>

        <div class="bg-black/60 backdrop-blur-xl p-6 rounded-2xl border border-white/20 shadow-xl">
          <h3 class="text-sm font-bold text-gray-300 uppercase mb-4 border-b border-white/20 pb-2 tracking-widest flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" /></svg>
            Planetary Profile
          </h3>
          <div class="space-y-4 font-mono text-sm text-gray-400">
            <div class="flex justify-between items-center border-b border-white/5 pb-2"><span>Mass:</span> <span class="text-gray-200">{{ planetData.mass_earth }} Earths</span></div>
            <div class="flex justify-between items-center border-b border-white/5 pb-2"><span>Year Length:</span> <span class="text-gray-200">{{ planetData.orbital_period_days }} Days</span></div>
            <div class="flex justify-between items-center"><span>Distance:</span> <span class="text-gray-200">{{ planetData.distance_ly }} Light Years</span></div>
          </div>
        </div>

        <div class="bg-black/60 backdrop-blur-xl p-6 rounded-2xl border border-[#00bfff]/30 shadow-xl relative overflow-hidden">
          <div class="absolute -right-10 -top-10 w-32 h-32 bg-[#00bfff]/20 rounded-full blur-3xl pointer-events-none"></div>
          <h3 class="text-sm font-bold text-[#00bfff] uppercase mb-4 border-b border-white/20 pb-2 tracking-widest flex items-center gap-2 relative z-10">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
            Host Star: {{ planetData.host_star.name }}
          </h3>
          <div class="space-y-4 font-mono text-sm text-gray-400 relative z-10">
            <div class="flex justify-between items-center border-b border-white/5 pb-2"><span>Temperature:</span> <span class="text-gray-200">{{ planetData.host_star.temperature_k }} K</span></div>
            <div class="flex justify-between items-center"><span>Luminosity:</span> <span class="text-gray-200">{{ planetData.host_star.luminosity }} (vs Sun)</span></div>
          </div>
        </div>

        <div class="bg-black/60 backdrop-blur-xl p-6 rounded-2xl border border-white/20 shadow-xl">
          <div class="flex justify-between mb-4 border-b border-white/20 pb-2 items-center">
            <h3 class="text-sm font-bold text-gray-300 uppercase tracking-widest flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" /></svg>
              Research Log
            </h3>
            <div v-if="!isEditing" class="flex gap-3">
              <div v-if="researchNote" class="flex gap-3">
                <button @click="isEditing = true" class="text-[#00bfff] hover:text-[#0099cc] text-sm transition-colors font-semibold">Edit</button>
                <button @click="showDeleteConfirm = true" class="text-red-400 hover:text-red-300 text-sm transition-colors font-semibold">Delete</button>
              </div>
              <button v-else @click="isEditing = true" class="text-[#00bfff] hover:text-[#0099cc] text-sm transition-colors font-semibold">Add Note</button>
            </div>
          </div>
          
          <p v-if="!isEditing" class="text-gray-300 min-h-[100px] text-sm leading-relaxed">{{ researchNote || 'No notes yet.' }}</p>
          
          <div v-else class="space-y-4">
            <textarea v-model="researchNote" class="w-full bg-black/60 border border-white/30 rounded-xl p-4 text-white focus:border-[#00bfff] focus:ring-1 focus:ring-[#00bfff] focus:outline-none text-sm transition-all min-h-[120px] shadow-inner"></textarea>
            <div class="flex gap-3">
              <button @click="saveNote" class="bg-gradient-to-r from-[#00bfff] to-blue-600 text-white px-6 py-2 rounded-lg text-sm font-bold hover:shadow-lg transition-all transform hover:-translate-y-0.5">Save Note</button>
              <button @click="isEditing = false" class="bg-white/10 text-white border border-white/20 px-6 py-2 rounded-lg text-sm hover:bg-white/20 transition-all">Cancel</button>
            </div>
          </div>
        </div>

        <div class="mt-4">
          <button 
            @click="requestAnalysis" 
            :disabled="isAnalyzing"
            class="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white py-3 rounded-xl transition-all font-bold disabled:opacity-50 shadow-lg shadow-purple-500/20 transform hover:-translate-y-1 flex items-center justify-center gap-2"
          >
            <svg v-if="!isAnalyzing" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.381z" clip-rule="evenodd" /></svg>
            <svg v-else class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            {{ isAnalyzing ? 'Consulting the AI Observatory...' : 'Request AI Analysis' }}
          </button>
          
          <div v-if="aiAnalysis" class="mt-6 p-6 bg-black/60 backdrop-blur-xl rounded-2xl border border-purple-500/30 text-gray-200 text-sm leading-relaxed italic font-serif shadow-inner">
            <h4 class="font-sans font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-[#00bfff] mb-3 not-italic uppercase text-xs tracking-widest flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-purple-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" /></svg>
              Astrophysical Report
            </h4>
            {{ aiAnalysis }}
          </div>
        </div>
      </div>
    </div>

    <div v-if="errorMessage" class="fixed inset-0 flex items-center justify-center bg-black/80 z-[70] backdrop-blur-sm">
      <div class="bg-indigo-950 p-8 rounded-2xl border border-red-500/50 max-w-sm w-full shadow-2xl">
        <h3 class="text-xl font-bold text-red-400 mb-4 flex items-center gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
          Transmission Error
        </h3>
        <p class="text-gray-300 mb-8">{{ errorMessage }}</p>
        <button @click="errorMessage = ''" class="w-full bg-white/10 py-3 rounded-xl text-white font-bold hover:bg-white/20 transition-colors border border-white/20">Dismiss</button>
      </div>
    </div>

    <div v-if="showDeleteConfirm" class="fixed inset-0 flex items-center justify-center bg-black/80 z-[60] backdrop-blur-sm">
      <div class="bg-indigo-950 p-8 rounded-2xl border border-white/10 max-w-sm w-full shadow-2xl">
        <h3 class="text-2xl font-bold text-white mb-2">Delete Log?</h3>
        <p class="text-gray-400 mb-8 text-sm">This action cannot be undone. All research data will be permanently purged.</p>
        <div class="flex gap-4">
          <button @click="deleteNote" class="flex-1 bg-red-600/80 py-3 rounded-xl text-white font-bold hover:bg-red-500 transition-colors shadow-lg border border-red-400/50">Delete</button>
          <button @click="showDeleteConfirm = false" class="flex-1 bg-white/10 py-3 rounded-xl text-white font-bold hover:bg-white/20 transition-colors border border-white/20">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>