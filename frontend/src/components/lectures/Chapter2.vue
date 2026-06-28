<script setup>
</script>

<template>
  <div class="space-y-12 leading-relaxed text-lg text-gray-300">
    <!-- Header -->
    <div class="border-b border-white/10 pb-8">
      <h1 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-2">Chapter 2</h1>
      <p class="text-xl text-[#00bfff] font-light">Formation of Stars, Solar Systems, and Exoplanets</p>
    </div>

    <!-- Learning Objectives -->
    <section class="bg-black/40 p-6 rounded-2xl border border-white/10">
      <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" /></svg>
        Learning Objectives
      </h2>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 text-sm marker:text-[#00bfff]">
        <li>Explain how stars are born.</li>
        <li>Describe the structure of giant molecular clouds and nebulae.</li>
        <li>Understand how protoplanetary disks form.</li>
        <li>Explain how planets grow from tiny dust particles (accretion).</li>
        <li>Explain planetary migration and its effects.</li>
        <li>Understand why some planetary systems contain rocky planets, gas giants, or ice giants.</li>
      </ul>
    </section>

    <!-- 2.1 Introduction & 2.2 Where Do Stars Come From? -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">2.1 Introduction & 2.2 Star Formation</h2>
      <p class="mb-4">Every star in the universe has a story. Around many of these stars, planets, moons, asteroids, and comets also form. Understanding how exoplanets form begins with understanding <strong>how stars are born</strong>.</p>
      <p class="mb-4">Stars do not appear suddenly. They form inside enormous clouds of gas and dust known as <strong>giant molecular clouds</strong>. These clouds are extremely cold (-263°C), and consist mainly of Hydrogen (74%) and Helium (24%).</p>
      
      <div class="bg-blue-900/20 p-4 rounded-lg border border-blue-500/30 text-sm italic my-6">
        <strong>Did You Know?</strong> The famous Orion Nebula is one of the nearest stellar nurseries to Earth and is actively forming new stars today.
      </div>
    </section>

    <!-- 2.3 The Birth of a Star & 2.4 Disk -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">2.3 The Birth of a Star & 2.4 Protoplanetary Disk</h2>
      <p class="mb-4">A star begins to form when part of a molecular cloud becomes unstable and collapses under its own gravity. As gravity pulls the gas inward, pressure increases, temperature rises, and the material begins to rotate faster.</p>
      <p class="mb-4">At the center, a dense object called a <strong>protostar</strong> forms. Eventually, the core temperature reaches approximately 10 million Kelvin, allowing hydrogen nuclei to fuse into helium. Nuclear fusion begins, and a true star is born.</p>
      
      <h3 class="text-xl font-semibold text-gray-100 mt-6 mb-2">The Protoplanetary Disk</h3>
      <p class="mb-4">Because the collapsing cloud is rotating, much of the remaining material spreads into a flat, rotating disk surrounding the young star. This is called a <strong>protoplanetary disk</strong>.</p>
      
      <pre class="bg-black/50 p-4 rounded-xl font-mono text-xs sm:text-sm text-[#00bfff] text-center mb-6">
                 Gas and Dust

             ********************
          *****              *****
        ****                    ****
             \              /
              \            /
               \          /
                \        /
                 \      /
                  \    /
                   \  /
                    ☀
                Young Star
      </pre>
    </section>

    <!-- 2.5 - 2.6 Dust to Planets -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">2.5 The Solar Nebula Theory & 2.6 Accretion</h2>
      <p class="mb-4">The most widely accepted explanation for the formation of planetary systems is the <strong>Solar Nebula Theory</strong>. It states that a molecular cloud collapses, forms a protostar, and then dust particles stick together to eventually form planets.</p>
      
      <div class="space-y-4">
        <div class="flex flex-col md:flex-row gap-4 items-center">
          <div class="w-full md:w-1/3 bg-white/5 p-4 rounded-lg border border-white/10 text-center">
            <h4 class="font-bold text-white">1. Dust Grains</h4>
            <p class="text-xs text-gray-400 mt-2">Microscopic dust particles collide and stick together via electrostatic forces.</p>
          </div>
          <span class="hidden md:block text-2xl text-[#00bfff]">→</span>
          <div class="w-full md:w-1/3 bg-white/5 p-4 rounded-lg border border-white/10 text-center">
            <h4 class="font-bold text-white">2. Pebbles</h4>
            <p class="text-xs text-gray-400 mt-2">Grains grow into pebbles and rocks. Gravity begins to play a larger role.</p>
          </div>
          <span class="hidden md:block text-2xl text-[#00bfff]">→</span>
          <div class="w-full md:w-1/3 bg-white/5 p-4 rounded-lg border border-white/10 text-center">
            <h4 class="font-bold text-white">3. Planetesimals</h4>
            <p class="text-xs text-gray-400 mt-2">Bodies measuring several kilometers form. They collide and grow into Protoplanets.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 2.7 - 2.9 Diversity -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">2.7 The Snow Line & 2.9 Planetary Migration</h2>
      <p class="mb-4">Why are there different types of planets? It depends on temperature. Near the star, it is too hot for water/ice, so only rock and metal survive. Farther away, temperatures drop below freezing.</p>
      <div class="bg-gradient-to-r from-red-900/30 to-blue-900/30 p-4 rounded-lg flex items-center justify-between font-mono text-sm mb-6">
        <div class="text-red-400 text-center w-1/2 border-r border-white/20">
          <strong>Inside Snow Line</strong><br>Rocky Planets
        </div>
        <div class="text-blue-400 text-center w-1/2">
          <strong>Outside Snow Line</strong><br>Gas/Ice Giants
        </div>
      </div>
      
      <h3 class="text-xl font-semibold text-gray-100 mt-6 mb-2">Planetary Migration</h3>
      <p class="mb-4">One of the biggest surprises was discovering <strong>Hot Jupiters</strong>—gas giants orbiting very close to stars. According to theories, gas giants form beyond the snow line. How did they get so close?</p>
      <p class="text-[#00bfff] font-medium">The answer is planetary migration. After forming, planets can interact with the disk and spiral inward.</p>
    </section>

  </div>
</template>
