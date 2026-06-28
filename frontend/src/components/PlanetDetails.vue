<script setup>
import { ref, onMounted } from 'vue'
import { authState } from '../state.js'

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
    if (!response.ok) throw new Error("Failed to fetch")
    planetData.value = await response.json()
    researchNote.value = planetData.value.note
  } catch (error) {
    console.error("Load failed:", error)
  } finally {
    loading.value = false
  }
})

const saveNote = async () => {
  await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/note`, {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${authState.value.token}` 
    },
    body: JSON.stringify({ content: researchNote.value })
  })
  planetData.value.note = researchNote.value
  isEditing.value = false
}

const deleteNote = async () => {
  await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/note`, { 
    method: 'DELETE',
    headers: { 'Authorization': `Bearer ${authState.value.token}` }
  })
  researchNote.value = ''
  planetData.value.note = ''
  showDeleteConfirm.value = false
  isEditing.value = false
}

const toggleFavorite = async () => {
  planetData.value.is_favorite = !planetData.value.is_favorite
  try {
    await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/favorite`, { 
      method: 'PATCH',
      headers: { 'Authorization': `Bearer ${authState.value.token}` }
    })
  } catch (error) {
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
    if (!response.ok) throw new Error("Service Unavailable")
    const data = await response.json()
    aiAnalysis.value = data.analysis
  } catch (error) {
    errorMessage.value = "We couldn't reach the AI observatory. Please check your connection."
  } finally {
    isAnalyzing.value = false
  }
}
</script>

<template>
  <div class="fixed inset-0 z-50 flex justify-end bg-black/70 backdrop-blur-sm transition-opacity">
    <div class="w-full max-w-lg h-full bg-[#1a1a1a] border-l border-gray-700 p-8 overflow-y-auto shadow-2xl">
      <button @click="emit('close')" class="mb-6 text-gray-400 hover:text-white transition">← Return to Database</button>

      <div v-if="loading" class="text-[#00bfff] font-mono animate-pulse mt-12">Accessing planetary archives...</div>

      <div v-else-if="planetData" class="space-y-8">
        <div class="flex items-start justify-between">
          <h2 class="text-4xl font-extrabold text-[#00bfff] drop-shadow-md">{{ planetData.name }}</h2>
          <button @click="toggleFavorite" class="mt-1 transition-transform hover:scale-110">
            <svg xmlns="http://www.w3.org/2000/svg" :class="planetData.is_favorite ? 'text-yellow-400 fill-yellow-400' : 'text-gray-500'" class="w-10 h-10 transition-colors" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
            </svg>
          </button>
        </div>

        <div class="bg-[#2d2d2d] p-5 rounded-xl border border-gray-700 shadow-sm">
          <h3 class="text-sm font-bold text-gray-300 uppercase mb-4 border-b border-gray-700 pb-2 tracking-wide">Planetary Profile</h3>
          <div class="space-y-3 font-mono text-sm text-gray-400">
            <div class="flex justify-between"><span>Mass:</span> <span class="text-gray-200">{{ planetData.mass_earth }} Earths</span></div>
            <div class="flex justify-between"><span>Year Length:</span> <span class="text-gray-200">{{ planetData.orbital_period_days }} Days</span></div>
            <div class="flex justify-between"><span>Distance:</span> <span class="text-gray-200">{{ planetData.distance_ly }} Light Years</span></div>
          </div>
        </div>

        <div class="bg-[#222222] p-5 rounded-xl border border-gray-700 shadow-sm">
          <h3 class="text-sm font-bold text-[#00bfff] uppercase mb-4 border-b border-gray-700 pb-2 tracking-wide">Host Star: {{ planetData.host_star.name }}</h3>
          <div class="space-y-3 font-mono text-sm text-gray-400">
            <div class="flex justify-between"><span>Temperature:</span> <span class="text-gray-200">{{ planetData.host_star.temperature_k }} K</span></div>
            <div class="flex justify-between"><span>Luminosity:</span> <span class="text-gray-200">{{ planetData.host_star.luminosity }} (vs Sun)</span></div>
          </div>
        </div>

        <div class="bg-[#2d2d2d] p-5 rounded-xl border border-gray-700 shadow-sm">
          <div class="flex justify-between mb-4 border-b border-gray-700 pb-2">
            <h3 class="text-sm font-bold text-gray-300 uppercase tracking-wide">Research Log</h3>
            <div v-if="!isEditing" class="flex gap-3">
              <div v-if="researchNote" class="flex gap-3">
                <button @click="isEditing = true" class="text-[#00bfff] hover:text-[#0099cc] text-sm transition-colors">Edit</button>
                <button @click="showDeleteConfirm = true" class="text-red-400 hover:text-red-300 text-sm transition-colors">Delete</button>
              </div>
              <button v-else @click="isEditing = true" class="text-[#00bfff] hover:text-[#0099cc] text-sm transition-colors">Add Note</button>
            </div>
          </div>
          
          <p v-if="!isEditing" class="text-gray-300 min-h-[100px] text-sm">{{ researchNote || 'No notes yet.' }}</p>
          
          <div v-else class="space-y-3">
            <textarea v-model="researchNote" class="w-full bg-[#1a1a1a] border border-gray-600 rounded-lg p-3 text-white focus:border-[#00bfff] focus:ring-1 focus:ring-[#00bfff] focus:outline-none text-sm transition-all"></textarea>
            <div class="flex gap-2">
              <button @click="saveNote" class="bg-[#00bfff] text-white px-4 py-2 rounded-lg text-sm hover:bg-[#0099cc] transition-colors shadow-sm">Save</button>
              <button @click="isEditing = false" class="bg-[#444444] text-white px-4 py-2 rounded-lg text-sm hover:bg-[#555555] transition-colors">Cancel</button>
            </div>
          </div>
        </div>

        <div class="mt-4">
          <button 
            @click="requestAnalysis" 
            :disabled="isAnalyzing"
            class="w-full bg-[#00bfff] hover:bg-[#0099cc] text-white py-3 rounded-lg transition-all font-bold disabled:opacity-50 shadow-md shadow-[#00bfff]/20"
          >
            {{ isAnalyzing ? 'Consulting the Observatory...' : 'Request AI Analysis' }}
          </button>
          
          <div v-if="aiAnalysis" class="mt-4 p-5 bg-[#1a1a1a] rounded-xl border border-[#00bfff]/30 text-gray-200 text-sm leading-relaxed italic font-serif shadow-inner">
            <h4 class="font-bold text-[#00bfff] mb-2 not-italic uppercase text-xs tracking-wider">Astrophysical Report:</h4>
            {{ aiAnalysis }}
          </div>
        </div>
      </div>
    </div>

    <div v-if="errorMessage" class="fixed inset-0 flex items-center justify-center bg-black/80 z-[70]">
      <div class="bg-[#2d2d2d] p-6 rounded-xl border border-red-500/50 max-w-sm w-full shadow-2xl">
        <h3 class="text-xl font-bold text-red-400 mb-4">Transmission Error</h3>
        <p class="text-gray-300 mb-6">{{ errorMessage }}</p>
        <button @click="errorMessage = ''" class="w-full bg-[#444444] py-2 rounded-lg text-white hover:bg-[#555555] transition-colors">Dismiss</button>
      </div>
    </div>

    <div v-if="showDeleteConfirm" class="fixed inset-0 flex items-center justify-center bg-black/80 z-[60]">
      <div class="bg-[#2d2d2d] p-6 rounded-xl border border-gray-700 max-w-sm w-full shadow-2xl">
        <h3 class="text-xl font-bold text-white mb-2">Delete Log?</h3>
        <p class="text-gray-400 mb-6 text-sm">This action cannot be undone.</p>
        <div class="flex gap-3">
          <button @click="deleteNote" class="flex-1 bg-red-600 py-2 rounded-lg text-white hover:bg-red-500 transition-colors shadow-sm">Delete</button>
          <button @click="showDeleteConfirm = false" class="flex-1 bg-[#444444] py-2 rounded-lg text-white hover:bg-[#555555] transition-colors">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>