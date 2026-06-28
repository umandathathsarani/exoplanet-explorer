<script setup>
</script>

<template>
  <div class="space-y-12 leading-relaxed text-lg text-gray-300">
    <!-- Header -->
    <div class="border-b border-white/10 pb-8">
      <h1 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-2">Chapter 4</h1>
      <p class="text-xl text-[#00bfff] font-light">Methods Used to Detect Exoplanets</p>
    </div>

    <!-- Learning Objectives -->
    <section class="bg-black/40 p-6 rounded-2xl border border-white/10">
      <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" /></svg>
        Learning Objectives
      </h2>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 text-sm marker:text-[#00bfff]">
        <li>Understand why detecting exoplanets is challenging.</li>
        <li>Explain the scientific principles behind the major exoplanet detection methods.</li>
        <li>Compare the advantages and limitations of each detection technique.</li>
      </ul>
    </section>

    <!-- 4.1 & 4.2 Challenges -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">4.1 Introduction & 4.2 Why Is Detecting Exoplanets So Difficult?</h2>
      <p class="mb-4">Finding an exoplanet is one of the most difficult tasks in modern astronomy. Unlike stars, exoplanets do not produce their own light through nuclear fusion. They are relatively small, faint, and often lost in the overwhelming brightness of the stars they orbit.</p>
      
      <div class="space-y-4">
        <div class="bg-white/5 p-4 rounded-xl border border-white/10">
          <h3 class="font-bold text-[#00bfff]">1. Enormous Distances</h3>
          <p class="text-sm mt-1">Even the nearest known exoplanets are several light-years away (1 light-year ≈ 9.46 trillion km).</p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl border border-white/10">
          <h3 class="font-bold text-[#00bfff]">2. Stars Are Much Brighter</h3>
          <p class="text-sm mt-1">A typical star can be millions to billions of times brighter than the planets orbiting it. The star's light hides the planet.</p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl border border-white/10">
          <h3 class="font-bold text-[#00bfff]">3. Planets Are Very Small</h3>
          <p class="text-sm mt-1">The Sun's diameter is about 109 times greater than Earth's.</p>
        </div>
      </div>
    </section>

    <!-- 4.3 Overview -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">4.3 Overview of Detection Methods</h2>
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-sm">
          <thead>
            <tr class="border-b border-white/20 bg-white/5">
              <th class="p-3 text-white">Method</th>
              <th class="p-3 text-white">Primary Measurement</th>
              <th class="p-3 text-white">Most Useful For</th>
            </tr>
          </thead>
          <tbody class="text-gray-300">
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold text-[#00bfff]">Transit Method</td>
              <td class="p-3">Change in brightness</td>
              <td class="p-3">Planet size</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold text-[#00bfff]">Radial Velocity</td>
              <td class="p-3">Star's motion</td>
              <td class="p-3">Planet mass</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold text-[#00bfff]">Direct Imaging</td>
              <td class="p-3">Light from planet</td>
              <td class="p-3">Atmosphere and orbit</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold text-[#00bfff]">Gravitational Microlensing</td>
              <td class="p-3">Bending of light</td>
              <td class="p-3">Distant planets</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 4.4 Transit Method -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">4.4 The Transit Method</h2>
      <p class="mb-4">The <strong>transit method</strong> is the most successful and widely used technique for discovering exoplanets.</p>
      
      <div class="bg-black/30 p-6 rounded-xl border border-white/10 mb-6">
        <h3 class="text-xl font-bold text-[#00bfff] mb-4">Basic Principle</h3>
        <p class="mb-4 text-sm">A transit occurs when a planet passes directly between its host star and Earth. As the planet crosses the face of the star, it blocks a tiny portion of the star's light. This causes a small, temporary decrease in the star's brightness.</p>
        
        <pre class="bg-black/50 p-4 rounded-lg font-mono text-xs sm:text-sm text-gray-300">
Before Transit       ⭐
During Transit       ⭐⬤
After Transit        ⭐
        </pre>
      </div>

      <div class="bg-black/30 p-6 rounded-xl border border-white/10">
        <h3 class="text-xl font-bold text-[#00bfff] mb-4">Light Curves</h3>
        <p class="mb-4 text-sm">Astronomers record a star's brightness over time. This graph is called a <strong>light curve</strong>.</p>
        
        <pre class="bg-black/50 p-4 rounded-lg font-mono text-xs sm:text-sm text-yellow-400">
Brightness

100% ────────────────
          \
           \
99.8%       \____
                \
100%─────────────\──────────── Time
        </pre>
        <p class="mt-4 text-sm italic">If the dips occur at regular intervals, it strongly suggests that a planet is orbiting the star.</p>
      </div>
    </section>

  </div>
</template>
