<script setup>
const emit = defineEmits(['start'])
</script>

<template>
  <div class="animate-in fade-in slide-in-from-bottom-4 duration-1000 pb-12">
    <!-- Hero Section -->
    <div class="text-center mb-16 pt-10">
      <h1 class="text-5xl md:text-7xl font-extrabold text-white tracking-tight mb-6">
        Discover the Cosmos
      </h1>
      <p class="text-xl md:text-2xl text-gray-100 max-w-3xl mx-auto leading-relaxed font-light">
        Journey beyond our solar system. Explore thousands of confirmed exoplanets, analyze their atmospheric data, and unravel the mysteries of the universe with AI.
      </p>
      <button 
        @click="emit('start')" 
        class="mt-10 bg-gradient-to-r from-[#00bfff] to-blue-600 text-white font-bold text-lg py-4 px-10 rounded-full hover:shadow-[0_0_20px_rgba(0,191,255,0.5)] transition-all transform hover:-translate-y-1"
      >
        Launch Explorer
      </button>
    </div>

    <!-- Info Sections -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
      <!-- About Exoplanets -->
      <div class="bg-black/60 backdrop-blur-xl p-8 rounded-2xl border border-white/20 shadow-2xl relative overflow-hidden group hover:border-[#00bfff]/50 transition-colors">
        <div class="absolute -right-10 -top-10 w-32 h-32 bg-[#00bfff]/20 rounded-full blur-3xl pointer-events-none group-hover:bg-[#00bfff]/30 transition-colors"></div>
        <h2 class="text-2xl font-bold text-white mb-4 relative z-10 flex items-center gap-3">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          What are Exoplanets?
        </h2>
        <div class="text-gray-200 space-y-4 relative z-10 leading-relaxed text-lg">
          <p>
            An exoplanet is any planet beyond our solar system. Most orbit other stars, but free-floating exoplanets, called rogue planets, orbit the galactic center and are untethered to any star.
          </p>
          <p>
            The first exoplanets were discovered in the 1990s. Today, we know of thousands, ranging from rocky, Earth-sized worlds to massive gas giants like Jupiter, and exotic "hot Jupiters" that orbit extremely close to their stars.
          </p>
          <div class="mt-6 pt-4 border-t border-white/10">
            <h3 class="text-sm font-bold text-[#00bfff] uppercase tracking-widest mb-3">Learn More:</h3>
            <ul class="space-y-2">
              <li><a href="https://exoplanets.nasa.gov/" target="_blank" class="text-blue-400 hover:text-blue-300 flex items-center gap-2"><svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg> NASA Exoplanet Exploration</a></li>
              <li><a href="https://www.esa.int/Science_Exploration/Space_Science/Exoplanets" target="_blank" class="text-blue-400 hover:text-blue-300 flex items-center gap-2"><svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg> ESA Space Science - Exoplanets</a></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Developer Info -->
      <div class="bg-black/60 backdrop-blur-xl p-8 rounded-2xl border border-white/20 shadow-2xl relative overflow-hidden group hover:border-purple-500/50 transition-colors">
        <div class="absolute -left-10 -bottom-10 w-40 h-40 bg-purple-600/20 rounded-full blur-3xl pointer-events-none group-hover:bg-purple-600/30 transition-colors"></div>
        <h2 class="text-2xl font-bold text-white mb-6 relative z-10 flex items-center gap-3">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-purple-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" /></svg>
          Meet the Creator
        </h2>
        
        <div class="relative z-10 flex flex-col gap-6">
          <div>
            <h3 class="text-3xl font-extrabold text-white">Mummullage Binuri Umanda Thathsarani</h3>
            <p class="text-gray-200 mt-2 font-medium text-lg">BSc (Hons) in Information Technology</p>
            <p class="text-[#00bfff] font-bold uppercase tracking-wider text-sm mt-1">Specialized in Artificial Intelligence</p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-2 border-t border-white/10 pt-6">
            <a href="mailto:umathathsarani2003@gmail.com" class="flex items-center gap-3 text-gray-300 hover:text-white group/link transition-colors">
              <div class="bg-white/10 p-2 rounded-lg group-hover/link:bg-purple-500/30 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
              </div>
              <span class="truncate">umathathsarani2003@gmail.com</span>
            </a>
            
            <a href="https://wa.me/94742813833" target="_blank" class="flex items-center gap-3 text-gray-300 hover:text-white group/link transition-colors">
              <div class="bg-white/10 p-2 rounded-lg group-hover/link:bg-green-500/30 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" /></svg>
              </div>
              0742813833 (WhatsApp)
            </a>

            <a href="https://www.linkedin.com/in/binuri-umanda-859bba337" target="_blank" class="flex items-center gap-3 text-gray-300 hover:text-white group/link transition-colors">
              <div class="bg-white/10 p-2 rounded-lg group-hover/link:bg-blue-500/30 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
              </div>
              LinkedIn Profile
            </a>

            <a href="https://github.com/umandathathsarani" target="_blank" class="flex items-center gap-3 text-gray-300 hover:text-white group/link transition-colors">
              <div class="bg-white/10 p-2 rounded-lg group-hover/link:bg-gray-500/30 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
              </div>
              GitHub
            </a>
            
            <a href="https://www.instagram.com/b.uma.t" target="_blank" class="flex items-center gap-3 text-gray-300 hover:text-white group/link transition-colors">
              <div class="bg-white/10 p-2 rounded-lg group-hover/link:bg-pink-500/30 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              </div>
              Instagram
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
