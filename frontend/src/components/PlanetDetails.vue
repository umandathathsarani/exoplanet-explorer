<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({ planetId: Number })
const emit = defineEmits(['close'])

const planetData = ref(null)
const researchNote = ref('')
const isEditing = ref(false)
const showDeleteConfirm = ref(false)
const loading = ref(true)

const aiAnalysis = ref('')
const isAnalyzing = ref(false)

onMounted(async () => {
  if (!props.planetId) return;

  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${props.planetId}`)
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
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ content: researchNote.value })
  })
  planetData.value.note = researchNote.value
  isEditing.value = false
}

const deleteNote = async () => {
  await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/note`, { method: 'DELETE' })
  researchNote.value = ''
  planetData.value.note = ''
  showDeleteConfirm.value = false
  isEditing.value = false
}

const toggleFavorite = async () => {
  planetData.value.is_favorite = !planetData.value.is_favorite
  try {
    await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/favorite`, { method: 'PATCH' })
  } catch (error) {
    planetData.value.is_favorite = !planetData.value.is_favorite
    alert("Could not update favorite status.")
  }
}

const requestAnalysis = async () => {
  isAnalyzing.value = true
  aiAnalysis.value = '' 
  try {
    const response = await fetch(`http://localhost:8000/api/exoplanets/${planetData.value.id}/analyze`, {
      method: 'POST'
    })
    const data = await response.json()
    aiAnalysis.value = data.analysis
  } catch (error) {
    console.error(error)
    alert("AI Analysis service currently unreachable.")
  } finally {
    isAnalyzing.value = false
  }
}
</script>

<template>
  <div class="fixed inset-0 z-50 flex justify-end bg-black/60 backdrop-blur-sm">
    <div class="w-full max-w-lg h-full bg-slate-900 border-l border-slate-700 p-8 overflow-y-auto">
      <button @click="emit('close')" class="mb-6 text-slate-400 hover:text-white transition">← Return to Database</button>

      <div v-if="loading" class="text-blue-400 font-mono animate-pulse mt-12">Accessing planetary archives...</div>

      <div v-else-if="planetData" class="space-y-8">
        <div class="flex items-start justify-between">
          <h2 class="text-4xl font-extrabold text-teal-300">{{ planetData.name }}</h2>
          <button @click="toggleFavorite" class="mt-1 transition-transform hover:scale-110">
            <svg xmlns="http://www.w3.org/2000/svg" :class="planetData.is_favorite ? 'text-yellow-400 fill-yellow-400' : 'text-slate-600'" class="w-10 h-10 transition-colors" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
            </svg>
          </button>
        </div>

        <div class="bg-slate-800 p-5 rounded-xl border border-slate-700">
          <h3 class="text-sm font-bold text-slate-400 uppercase mb-4 border-b border-slate-700 pb-2">Planetary Profile</h3>
          <div class="space-y-3 font-mono text-sm text-slate-300">
            <div class="flex justify-between"><span>Mass:</span> <span>{{ planetData.mass_earth }} Earths</span></div>
            <div class="flex justify-between"><span>Year Length:</span> <span>{{ planetData.orbital_period_days }} Days</span></div>
            <div class="flex justify-between"><span>Distance:</span> <span>{{ planetData.distance_ly }} Light Years</span></div>
          </div>
        </div>

        <div class="bg-indigo-950/30 p-5 rounded-xl border border-indigo-900/50">
          <h3 class="text-sm font-bold text-indigo-300 uppercase mb-4 border-b border-indigo-900/50 pb-2">Host Star: {{ planetData.host_star.name }}</h3>
          <div class="space-y-3 font-mono text-sm text-indigo-200">
            <div class="flex justify-between"><span>Temperature:</span> <span>{{ planetData.host_star.temperature_k }} K</span></div>
            <div class="flex justify-between"><span>Luminosity:</span> <span>{{ planetData.host_star.luminosity }} (vs Sun)</span></div>
          </div>
        </div>

        <div class="bg-slate-800 p-5 rounded-xl border border-slate-700">
          <div class="flex justify-between mb-4 border-b border-slate-700 pb-2">
            <h3 class="text-sm font-bold text-slate-400 uppercase">Research Log</h3>
            <div v-if="!isEditing" class="flex gap-3">
              <div v-if="researchNote" class="flex gap-3">
                <button @click="isEditing = true" class="text-blue-400 hover:text-blue-300 text-sm">Edit</button>
                <button @click="showDeleteConfirm = true" class="text-red-400 hover:text-red-300 text-sm">Delete</button>
              </div>
              <button v-else @click="isEditing = true" class="text-emerald-400 hover:text-emerald-300 text-sm">Add Note</button>
            </div>
          </div>
          <p v-if="!isEditing" class="text-slate-200 min-h-[100px] text-sm">{{ researchNote || 'No notes yet.' }}</p>
          <div v-else class="space-y-3">
            <textarea v-model="researchNote" class="w-full bg-slate-900 border border-slate-600 rounded p-3 text-white focus:border-blue-500 focus:outline-none text-sm"></textarea>
            <div class="flex gap-2">
              <button @click="saveNote" class="bg-blue-600 text-white px-4 py-2 rounded text-sm hover:bg-blue-500 transition">Save</button>
              <button @click="isEditing = false" class="bg-slate-700 text-white px-4 py-2 rounded text-sm hover:bg-slate-600 transition">Cancel</button>
            </div>
          </div>
        </div>

        <div class="mt-4">
          <button 
            @click="requestAnalysis" 
            :disabled="isAnalyzing"
            class="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white py-3 rounded-lg transition-all font-bold disabled:opacity-50"
          >
            {{ isAnalyzing ? 'Consulting the Observatory...' : 'Request AI Analysis' }}
          </button>
          
          <div v-if="aiAnalysis" class="mt-4 p-5 bg-indigo-950/40 rounded-xl border border-indigo-500/30 text-indigo-100 text-sm leading-relaxed italic font-serif">
            <h4 class="font-bold text-indigo-300 mb-2 not-italic uppercase text-xs tracking-wider">Astrophysical Report:</h4>
            {{ aiAnalysis }}
          </div>
        </div>
      </div>
    </div>

    <div v-if="showDeleteConfirm" class="fixed inset-0 flex items-center justify-center bg-black/80 z-[60]">
      <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 max-w-sm w-full">
        <h3 class="text-xl font-bold text-white mb-4">Delete Log?</h3>
        <p class="text-slate-400 mb-6">This action cannot be undone.</p>
        <div class="flex gap-3">
          <button @click="deleteNote" class="flex-1 bg-red-600 py-2 rounded text-white hover:bg-red-500 transition">Delete</button>
          <button @click="showDeleteConfirm = false" class="flex-1 bg-slate-700 py-2 rounded text-white hover:bg-slate-600 transition">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>