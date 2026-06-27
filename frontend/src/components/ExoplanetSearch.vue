<script setup>
import { ref, computed } from 'vue'

const searchFilters = ref({
  method: '',
  maxDistance: 2000,
  minMass: 0.1
})

const handleSearch = () => {
  console.log("Sending query to FastAPI backend:", searchFilters.value)
  // Soon we will use fetch/axios here to call: http://localhost:8000/api/exoplanets/search
}
</script>

<template>
  <div class="bg-slate-800/50 border border-slate-700/60 p-6 rounded-xl backdrop-blur-md max-w-2xl mx-auto shadow-xl">
    <h2 class="text-2xl font-bold text-blue-400 mb-6">Cosmic Database Query</h2>
    
    <form @submit.prevent="handleSearch" class="space-y-6">
      <div>
        <label class="block text-sm font-semibold text-slate-300 mb-2">Discovery Method</label>
        <select 
          v-model="searchFilters.method"
          class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-slate-200 focus:outline-none focus:border-blue-500"
        >
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
        <input 
          type="range" 
          min="10" 
          max="5000" 
          step="50"
          v-model.number="searchFilters.maxDistance"
          class="w-full h-2 bg-slate-900 rounded-lg appearance-none cursor-pointer accent-blue-500"
        />
      </div>

      <div>
        <div class="flex justify-between text-sm mb-2">
          <label class="font-semibold text-slate-300">Minimum Planet Mass</label>
          <span class="text-blue-400 font-mono">{{ searchFilters.minMass }} M⊕ (Earth Masses)</span>
        </div>
        <input 
          type="range" 
          min="0.1" 
          max="30" 
          step="0.1"
          v-model.number="searchFilters.minMass"
          class="w-full h-2 bg-slate-900 rounded-lg appearance-none cursor-pointer accent-blue-500"
        />
      </div>

      <button 
        type="submit"
        class="w-full bg-gradient-to-r from-blue-500 to-indigo-600 hover:from-blue-600 hover:to-indigo-700 text-white font-bold py-3 px-4 rounded-lg transition shadow-md hover:shadow-indigo-500/20"
      >
        Scan Deep Space
      </button>
    </form>
  </div>
</template>