<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({ planetId: Number })
const emit = defineEmits(['close'])

const planetData = ref(null)
const researchNote = ref('')
const isEditing = ref(false)
const showDeleteConfirm = ref(false)

onMounted(async () => {
  const response = await fetch(`http://localhost:8000/api/exoplanets/${props.planetId}`)
  planetData.value = await response.json()
  researchNote.value = planetData.value.note
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
</script>

<template>
  <div class="fixed inset-0 z-50 flex justify-end bg-black/60 backdrop-blur-sm">
    <div class="w-full max-w-lg h-full bg-slate-900 border-l border-slate-700 p-8 overflow-y-auto">
      <button @click="emit('close')" class="mb-6 text-slate-400 hover:text-white">← Return</button>

      <div v-if="planetData" class="space-y-6">
        <h2 class="text-4xl font-bold text-teal-300">{{ planetData.name }}</h2>

        <div class="bg-slate-800 p-5 rounded-xl border border-slate-700">
          <div class="flex justify-between mb-4">
            <h3 class="text-sm font-bold text-slate-400 uppercase">Research Log</h3>
            <button v-if="!isEditing" @click="isEditing = true" class="text-blue-400 hover:text-blue-300 text-sm">Edit</button>
          </div>
          
          <p v-if="!isEditing" class="text-slate-200 min-h-[100px]">{{ researchNote || 'No notes yet.' }}</p>
          
          <div v-else class="space-y-3">
            <textarea v-model="researchNote" class="w-full bg-slate-900 border border-slate-600 rounded p-3 text-white"></textarea>
            <div class="flex gap-2">
              <button @click="saveNote" class="bg-blue-600 text-white px-4 py-2 rounded">Save</button>
              <button @click="isEditing = false" class="bg-slate-700 text-white px-4 py-2 rounded">Cancel</button>
              <button @click="showDeleteConfirm = true" class="text-red-400 ml-auto hover:text-red-300">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showDeleteConfirm" class="fixed inset-0 flex items-center justify-center bg-black/80 z-[60]">
      <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 max-w-sm w-full">
        <h3 class="text-xl font-bold text-white mb-4">Delete Log?</h3>
        <p class="text-slate-400 mb-6">This action cannot be undone.</p>
        <div class="flex gap-3">
          <button @click="deleteNote" class="flex-1 bg-red-600 py-2 rounded text-white">Delete</button>
          <button @click="showDeleteConfirm = false" class="flex-1 bg-slate-700 py-2 rounded text-white">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>