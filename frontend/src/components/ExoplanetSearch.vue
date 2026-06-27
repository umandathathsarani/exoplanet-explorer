<script setup>
import { ref } from 'vue'

const searchFilters = ref({
  method: '',
  maxDistance: 2000,
  minMass: 0.1
})

const showModal = ref(false)
const modalMessage = ref('')
const isError = ref(false)

const handleSearch = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/exoplanets/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(searchFilters.value)
    })

    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)

    const data = await response.json()
    
    isError.value = false
    modalMessage.value = data.message
    showModal.value = true

  } catch (error) {
    console.error("Communication error:", error)
    isError.value = true
    modalMessage.value = "Failed to connect to the backend. Is FastAPI running?"
    showModal.value = true
  }
}
</script>

<template>
  <div>
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
  </div>
</template>