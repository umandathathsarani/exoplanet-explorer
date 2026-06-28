<script setup>
</script>

<template>
  <div class="space-y-12 leading-relaxed text-lg text-gray-300">
    <!-- Header -->
    <div class="border-b border-white/10 pb-8">
      <h1 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-2">Chapter 3</h1>
      <p class="text-xl text-[#00bfff] font-light">Classification and Types of Exoplanets</p>
    </div>

    <!-- Learning Objectives -->
    <section class="bg-black/40 p-6 rounded-2xl border border-white/10">
      <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" /></svg>
        Learning Objectives
      </h2>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 text-sm marker:text-[#00bfff]">
        <li>Explain why scientists classify exoplanets.</li>
        <li>Describe the major categories of exoplanets.</li>
        <li>Explain how mass, radius, density, and composition influence planetary classification.</li>
        <li>Describe unusual exoplanets such as lava worlds, ocean worlds, rogue planets, and circumbinary planets.</li>
      </ul>
    </section>

    <!-- 3.1 Introduction & 3.2 How to Classify -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">3.1 Introduction & 3.2 Classification</h2>
      <p class="mb-4">Since the discovery of the first confirmed exoplanets, astronomers have realized that planets come in an astonishing variety of sizes, compositions, temperatures, and orbital configurations. To make sense of this diversity, astronomers classify exoplanets according to physical characteristics:</p>
      
      <div class="grid sm:grid-cols-2 gap-4 my-6">
        <div class="bg-white/5 p-4 rounded-xl border border-white/10">
          <h4 class="font-bold text-[#00bfff]">1. Size (Radius)</h4>
          <p class="text-sm mt-1">Expressed relative to Earth. 1 R⊕ = 1 Earth Radius.</p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl border border-white/10">
          <h4 class="font-bold text-[#00bfff]">2. Mass</h4>
          <p class="text-sm mt-1">Amount of matter. 1 M⊕ = 1 Earth Mass.</p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl border border-white/10">
          <h4 class="font-bold text-[#00bfff]">3. Density</h4>
          <p class="text-sm mt-1">Mass divided by volume. High density means rocky/metallic; low density means gas/ice.</p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl border border-white/10">
          <h4 class="font-bold text-[#00bfff]">4. Composition</h4>
          <p class="text-sm mt-1">Rock, Iron, Water ice, Hydrogen, Helium, etc.</p>
        </div>
      </div>
    </section>

    <!-- Planet Types Gallery -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-6 border-l-4 border-[#00bfff] pl-4">Types of Exoplanets</h2>
      
      <div class="space-y-6">
        <!-- Rocky & Super-Earths -->
        <div class="flex flex-col lg:flex-row gap-6 items-center bg-black/30 p-6 rounded-2xl border border-white/10">
          <div class="w-full lg:w-1/3 flex justify-center">
            <img src="/space-bg-2.png" alt="Rocky Planet" class="rounded-full shadow-[0_0_30px_rgba(200,200,200,0.1)] w-48 h-48 object-cover border border-white/5" onerror="this.src='/space-bg-3.png'" />
          </div>
          <div class="w-full lg:w-2/3">
            <h3 class="text-xl font-bold text-white mb-2">3.3 Rocky Planets & 3.4 Super-Earths</h3>
            <p class="text-sm mb-3">Rocky (terrestrial) planets are composed primarily of rock and metal. They have a solid surface, an iron-rich core, and a silicate mantle.</p>
            <p class="text-sm mb-3"><strong>Super-Earths</strong> are larger and more massive than Earth but smaller than Neptune (1.2–2 Earth radii). Despite the name, they aren't necessarily Earth-like. They could be rocky, ocean-covered, or have thick atmospheres.</p>
          </div>
        </div>

        <!-- Gas Giants -->
        <div class="flex flex-col lg:flex-row-reverse gap-6 items-center bg-black/30 p-6 rounded-2xl border border-white/10">
          <div class="w-full lg:w-1/3 flex justify-center">
            <img src="/space-bg-3.png" alt="Gas Giant" class="rounded-full shadow-[0_0_30px_rgba(255,150,50,0.1)] w-48 h-48 object-cover border border-white/5" onerror="this.src='/space-bg-3.png'" />
          </div>
          <div class="w-full lg:w-2/3">
            <h3 class="text-xl font-bold text-white mb-2">3.6 Gas Giants & Hot Jupiters</h3>
            <p class="text-sm mb-3">Enormous planets composed mainly of hydrogen and helium. They have very low average density, thick atmospheres, and no clearly defined solid surface. Under immense pressure, hydrogen behaves like an electrical conductor (metallic hydrogen).</p>
            <p class="text-sm"><strong>Hot Jupiters</strong> are gas giants that orbit extremely close to their stars, with surface temperatures exceeding 1,000°C.</p>
          </div>
        </div>

        <!-- Unusual Worlds -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div class="bg-white/5 p-4 rounded-xl border border-white/10 hover:border-[#00bfff]/50 transition">
            <h4 class="font-bold text-blue-300">3.8 Ocean Worlds</h4>
            <p class="text-xs mt-2 text-gray-400">Covered almost entirely by deep global oceans, hundreds of kilometers of water. May support microbial life.</p>
          </div>
          <div class="bg-white/5 p-4 rounded-xl border border-white/10 hover:border-red-500/50 transition">
            <h4 class="font-bold text-red-400">3.9 Lava Worlds</h4>
            <p class="text-xs mt-2 text-gray-400">Orbit so close to stars that surfaces melt into rock oceans. Temperatures exceed 2,000°C.</p>
          </div>
          <div class="bg-white/5 p-4 rounded-xl border border-white/10 hover:border-white/50 transition">
            <h4 class="font-bold text-gray-300">3.11 Rogue Planets</h4>
            <p class="text-xs mt-2 text-gray-400">Ejected from planetary systems. Do not orbit any star and travel through interstellar space.</p>
          </div>
          <div class="bg-white/5 p-4 rounded-xl border border-white/10 hover:border-purple-400/50 transition">
            <h4 class="font-bold text-purple-400">3.12 Circumbinary</h4>
            <p class="text-xs mt-2 text-gray-400">Orbit two stars instead of one. From the surface, you would see two suns rising and setting.</p>
          </div>
          <div class="bg-white/5 p-4 rounded-xl border border-white/10 hover:border-cyan-400/50 transition">
            <h4 class="font-bold text-cyan-400">3.7 Ice Giants</h4>
            <p class="text-xs mt-2 text-gray-400">Rich in water, ammonia, and methane ices. Blue color is caused by methane gas absorbing red light.</p>
          </div>
        </div>

      </div>
    </section>

    <!-- Comparison Table -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">3.15 Comparing Major Planet Types</h2>
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-sm">
          <thead>
            <tr class="border-b border-white/20 bg-white/5">
              <th class="p-3 text-[#00bfff]">Type</th>
              <th class="p-3 text-white">Main Composition</th>
              <th class="p-3 text-white">Habitability Potential</th>
            </tr>
          </thead>
          <tbody class="text-gray-300">
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold">Rocky Planet</td>
              <td class="p-3">Rock, Metal</td>
              <td class="p-3 text-green-400">High (if conditions favorable)</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold">Super-Earth</td>
              <td class="p-3">Rock/Ice</td>
              <td class="p-3 text-green-400">Moderate to High</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold">Gas Giant</td>
              <td class="p-3">Hydrogen, Helium</td>
              <td class="p-3 text-red-400">Very Low</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold">Ocean World</td>
              <td class="p-3">Water + Rock</td>
              <td class="p-3 text-yellow-400">Unknown</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold">Lava World</td>
              <td class="p-3">Rock</td>
              <td class="p-3 text-red-400">Extremely Low</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

  </div>
</template>
