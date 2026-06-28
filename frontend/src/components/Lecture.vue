<script setup>
import { ref } from 'vue'
import Chapter1 from './lectures/Chapter1.vue'
import Chapter2 from './lectures/Chapter2.vue'
import Chapter3 from './lectures/Chapter3.vue'
import Chapter4 from './lectures/Chapter4.vue'

const currentChapter = ref(1)
const totalChapters = 4
</script>

<template>
  <div class="animate-in fade-in slide-in-from-bottom-4 duration-1000 pb-12 pt-6">
    <div class="max-w-6xl mx-auto flex flex-col md:flex-row gap-6 px-4">
      
      <!-- Sidebar Navigation -->
      <div class="w-full md:w-64 shrink-0">
        <div class="bg-black/60 backdrop-blur-2xl p-6 rounded-3xl border border-white/20 shadow-2xl sticky top-24">
          <h2 class="text-xl font-bold text-white mb-6 border-b border-white/10 pb-4">Chapters</h2>
          <nav class="space-y-2">
            <button 
              v-for="i in totalChapters" :key="i"
              @click="currentChapter = i"
              :class="currentChapter === i ? 'bg-[#00bfff]/20 text-[#00bfff] border-[#00bfff]/50' : 'text-gray-400 hover:text-white hover:bg-white/5 border-transparent'"
              class="w-full text-left px-4 py-3 rounded-xl border transition duration-200 font-medium text-sm flex items-center justify-between"
            >
              <span>Chapter {{ i }}</span>
              <svg v-if="currentChapter === i" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" /></svg>
            </button>
            <div class="px-4 py-3 text-xs text-gray-500 italic mt-4 border-t border-white/5 pt-4">More chapters coming soon...</div>
          </nav>
        </div>
      </div>

      <!-- Main Content -->
      <div class="flex-1 bg-black/60 backdrop-blur-2xl p-8 md:p-12 rounded-3xl border border-white/20 shadow-2xl text-gray-200 min-h-[500px]">
        <Chapter1 v-if="currentChapter === 1" />
        <Chapter2 v-if="currentChapter === 2" />
        <Chapter3 v-if="currentChapter === 3" />
        <Chapter4 v-if="currentChapter === 4" />
        
        <!-- Pagination -->
        <div class="mt-16 pt-8 border-t border-white/10 flex justify-between items-center">
          <button 
            @click="currentChapter > 1 ? currentChapter-- : null"
            :disabled="currentChapter === 1"
            :class="currentChapter === 1 ? 'opacity-30 cursor-not-allowed' : 'hover:bg-white/10 hover:text-white'"
            class="px-5 py-2 rounded-xl text-gray-400 border border-white/10 transition flex items-center gap-2 text-sm font-medium"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" /></svg>
            Previous
          </button>
          
          <div class="text-sm text-gray-500 font-medium">
            {{ currentChapter }} of {{ totalChapters }}
          </div>

          <button 
            @click="currentChapter < totalChapters ? currentChapter++ : null"
            :disabled="currentChapter === totalChapters"
            :class="currentChapter === totalChapters ? 'opacity-30 cursor-not-allowed' : 'hover:bg-white/10 hover:text-white'"
            class="px-5 py-2 rounded-xl text-gray-400 border border-white/10 transition flex items-center gap-2 text-sm font-medium"
          >
            Next
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" /></svg>
          </button>
        </div>
      </div>



    </div>
  </div>
</template>
