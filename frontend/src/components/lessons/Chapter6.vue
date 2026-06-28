<script setup>
</script>

<template>
  <div class="space-y-12 leading-relaxed text-lg text-gray-300">
    <!-- Header -->
    <div class="border-b border-white/10 pb-8">
      <h1 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-2">Chapter 6</h1>
      <p class="text-xl text-[#00bfff] font-light">Habitable Zones and Planetary Habitability</p>
    </div>

    <!-- Learning Objectives -->
    <section class="bg-black/40 p-6 rounded-2xl border border-white/10">
      <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" /></svg>
        Learning Objectives
      </h2>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 text-sm marker:text-[#00bfff]">
        <li>Explain what the habitable zone is and how it is defined.</li>
        <li>Understand why liquid water is central to habitability.</li>
        <li>Describe different factors that affect planetary habitability.</li>
        <li>Compare habitable conditions around different types of stars.</li>
        <li>Understand how atmospheres influence surface temperature.</li>
        <li>Explain the role of magnetic fields and geology in supporting life.</li>
        <li>Evaluate why being in the habitable zone does not guarantee life.</li>
        <li>Understand key hypotheses about life in the universe (Drake Equation, Rare Earth idea).</li>
      </ul>
    </section>

    <!-- 6.1 Introduction & 6.2 Habitable Zone -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">6.1 Introduction & 6.2 What Is the Habitable Zone?</h2>
      <p class="mb-4">When scientists search for life beyond Earth, they do not start by looking for living organisms directly. Instead, they first search for <strong>environments where life could exist</strong>.</p>
      
      <p class="mb-4">The most important concept in this search is the <strong>habitable zone (HZ)</strong>, sometimes called the "Goldilocks Zone." This is the region around a star where conditions are <em>not too hot and not too cold</em>, allowing liquid water to exist on a planet's surface under the right atmospheric conditions.</p>
      
      <div class="bg-black/50 p-6 rounded-xl font-mono text-center text-gray-300 my-6 flex justify-between items-center overflow-x-auto text-sm">
        <div class="text-red-400">
          <div class="text-xl mb-2">☀</div>
          <strong>Too Hot</strong><br/>
          <span class="text-xs">Venus-like</span>
        </div>
        <div class="w-full max-w-sm h-3 bg-gradient-to-r from-red-500 via-green-500 to-blue-500 mx-4 rounded-full relative">
          <div class="absolute inset-0 flex items-center justify-center text-xs font-bold text-white drop-shadow-md">
            Habitable Zone
          </div>
        </div>
        <div class="text-blue-400">
          <div class="text-xl mb-2">❄</div>
          <strong>Too Cold</strong><br/>
          <span class="text-xs">Mars-like</span>
        </div>
      </div>

      <h3 class="text-xl font-bold text-white mt-8 mb-4">Why Water?</h3>
      <p class="mb-4">Water is considered essential because:</p>
      <ul class="list-disc pl-6 space-y-1 text-gray-200">
        <li>It is an excellent solvent for chemical reactions.</li>
        <li>It supports complex chemistry.</li>
        <li>It remains liquid across a wide temperature range.</li>
        <li>It is abundant in the universe.</li>
      </ul>
      <p class="mt-4 italic text-sm text-[#00bfff]">On Earth, every known form of life depends on water.</p>
    </section>

    <!-- 6.3 Edges -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">6.3 The Inner and Outer Edges of the Habitable Zone</h2>
      <div class="grid md:grid-cols-2 gap-6">
        <div class="bg-red-900/20 p-5 rounded-xl border border-red-500/30">
          <h3 class="text-lg font-bold text-red-400 mb-2">Inner Edge (Too Hot)</h3>
          <ul class="text-sm list-disc pl-4 text-gray-300 space-y-1">
            <li>Water evaporates.</li>
            <li>Atmosphere becomes saturated with steam.</li>
            <li>Greenhouse gases trap heat.</li>
            <li>Planet may enter a <strong>runaway greenhouse state</strong>.</li>
            <li class="mt-2 italic text-gray-400">Example: Venus</li>
          </ul>
        </div>
        <div class="bg-blue-900/20 p-5 rounded-xl border border-blue-500/30">
          <h3 class="text-lg font-bold text-blue-400 mb-2">Outer Edge (Too Cold)</h3>
          <ul class="text-sm list-disc pl-4 text-gray-300 space-y-1">
            <li>Water freezes.</li>
            <li>Ice reflects sunlight, increasing cooling.</li>
            <li>CO₂ may condense into ice.</li>
            <li>Planet becomes a global snowball.</li>
            <li class="mt-2 italic text-gray-400">Example: Mars-like conditions</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 6.4 Star Types -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">6.4 Habitable Zones Around Different Stars</h2>
      <p class="mb-6">Not all stars are the same. The habitable zone changes depending on star type.</p>
      
      <div class="space-y-4">
        <div class="bg-white/5 p-4 rounded-xl border border-white/10">
          <h3 class="font-bold text-yellow-400">1. Sun-like Stars (G-type)</h3>
          <p class="text-sm mt-1">Moderate temperature, stable radiation, wide habitable zone. <em>Earth is located in this category.</em></p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl border border-white/10">
          <h3 class="font-bold text-red-400">2. Red Dwarfs (M-type stars)</h3>
          <p class="text-sm mt-1">Small, cool, and very long-lived. They have a narrow habitable zone very close to the star. <strong>Challenges:</strong> Strong stellar flares, radiation bursts, and tidal locking.</p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl border border-white/10">
          <h3 class="font-bold text-blue-400">3. Large Stars (A-type and beyond)</h3>
          <p class="text-sm mt-1">Very bright, very hot, with short lifespans. Habitability is less likely because life may not have enough time to develop before the star evolves.</p>
        </div>
      </div>
    </section>

    <!-- 6.5 Greenhouse & 6.6 Atmospheres -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">6.5 The Greenhouse Effect & 6.6 Atmospheres</h2>
      <p class="mb-4">The <strong>greenhouse effect</strong> plays a major role in planetary temperature. Surface absorbs stellar energy and re-emits it as infrared radiation, which is trapped by gases like CO₂, H₂O, and CH₄.</p>
      
      <div class="overflow-x-auto mb-8">
        <table class="w-full text-left border-collapse text-sm">
          <thead>
            <tr class="border-b border-white/20 bg-white/5">
              <th class="p-3 text-white">Greenhouse Type</th>
              <th class="p-3 text-white">Result</th>
            </tr>
          </thead>
          <tbody class="text-gray-300">
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold text-green-400">Mild greenhouse</td>
              <td class="p-3">Stable temperatures (Earth-like)</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold text-yellow-400">Strong greenhouse</td>
              <td class="p-3">Extreme heat (Venus-like)</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold text-red-500">Runaway greenhouse</td>
              <td class="p-3">Ocean evaporation, sterilization</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p class="mb-4"><strong>Functions of an Atmosphere:</strong></p>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 text-sm mb-4">
        <li>Regulates temperature</li>
        <li>Protects from radiation</li>
        <li>Enables weather cycles</li>
        <li>Supports liquid water stability</li>
        <li>Helps maintain pressure</li>
      </ul>
      <p class="text-sm text-gray-400 italic">Too thin → water evaporates or freezes easily (Mars). Too thick → extreme pressure and heat (Venus). Just right → stable climate (Earth).</p>
    </section>

    <!-- 6.7 to 6.10 -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">6.7 Magnetic Fields & 6.8 Geology</h2>
      <p class="mb-4">A <strong>magnetic field</strong> protects a planet from harmful stellar radiation and solar wind. Without it, the atmosphere may be stripped away, surface radiation increases, and water can be lost to space.</p>
      <p class="mb-4"><strong>Geology</strong> plays a key role in long-term habitability by recycling carbon (carbon-silicate cycle), releasing gases through volcanoes, and stabilizing climate over millions of years. Earth is currently the only known planet with active <strong>plate tectonics</strong>.</p>
      
      <h3 class="text-xl font-bold text-white mt-8 mb-4">6.9 Tidal Locking</h3>
      <p class="mb-4">Many exoplanets orbit close to red dwarf stars and become <strong>tidally locked</strong>. One side always faces the star (permanent day), and one side always faces away (permanent night). This creates extreme temperature differences and possible strong winds between hemispheres.</p>

      <h3 class="text-xl font-bold text-red-400 mt-8 mb-4">6.10 Habitability Does NOT Guarantee Life</h3>
      <p class="mb-4">Even if a planet is in the habitable zone, it may still be uninhabitable due to no atmosphere, toxic atmosphere, extreme radiation, lack of water, unstable climate, or frequent asteroid impacts. (e.g., Mars lies near the outer edge of the Sun's habitable zone but is cold and dry).</p>
    </section>

    <!-- 6.11 & 6.12 -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">6.11 The Rare Earth Hypothesis & 6.12 The Drake Equation</h2>
      
      <div class="bg-white/5 p-6 rounded-2xl border border-white/10 mb-6">
        <h3 class="text-xl font-bold text-[#00bfff] mb-2">The Rare Earth Hypothesis</h3>
        <p class="mb-4 text-sm text-gray-300">Suggests that complex life may be extremely rare because many conditions must align perfectly. These include a stable star, right distance, magnetic field, large moon, plate tectonics, liquid water, and a suitable atmosphere.</p>
      </div>

      <div class="bg-black/40 p-6 rounded-2xl border border-white/10">
        <h3 class="text-xl font-bold text-[#00bfff] mb-2">The Drake Equation</h3>
        <p class="mb-4 text-sm text-gray-300">Estimates the number of intelligent civilizations in the galaxy:</p>
        <p class="text-center font-mono text-lg text-white mb-4 bg-white/5 py-3 rounded-lg border border-white/10">N = R × fₚ × nₑ × fₗ × fᵢ × f꜀ × L</p>
        <ul class="text-xs text-gray-400 space-y-1 grid sm:grid-cols-2 gap-2">
          <li><strong>R</strong> = star formation rate</li>
          <li><strong>fₚ</strong> = fraction of stars with planets</li>
          <li><strong>nₑ</strong> = number of habitable planets per system</li>
          <li><strong>fₗ</strong> = fraction where life appears</li>
          <li><strong>fᵢ</strong> = fraction where intelligent life develops</li>
          <li><strong>f꜀</strong> = fraction that develop communication</li>
          <li><strong>L</strong> = lifetime of civilizations</li>
        </ul>
      </div>
    </section>

    <!-- Summary -->
    <section class="bg-[#0a0a1a] p-8 rounded-2xl border border-white/20 mt-12">
      <h2 class="text-2xl font-bold text-white mb-6">Chapter Summary</h2>
      <ul class="list-disc pl-5 space-y-3 text-gray-300">
        <li>The habitable zone is the region where liquid water can exist.</li>
        <li>Habitability depends on many factors beyond distance from a star.</li>
        <li>Atmospheres regulate temperature and protect life.</li>
        <li>Magnetic fields shield planets from radiation.</li>
        <li>Geological activity helps stabilize climate over time.</li>
        <li>Many planets in habitable zones may still be uninhabitable.</li>
        <li>Life may be rare or common depending on which scientific hypothesis is correct.</li>
        <li>The Drake Equation provides a framework for thinking about life in the galaxy.</li>
      </ul>
      
      <h3 class="text-xl font-bold text-white mt-8 mb-4">Key Terms</h3>
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="border-b border-white/20">
              <th class="p-2 text-white">Term</th>
              <th class="p-2 text-white">Meaning</th>
            </tr>
          </thead>
          <tbody class="text-sm text-gray-300">
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Habitable Zone</td>
              <td class="p-2">Region around a star where liquid water can exist.</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Greenhouse Effect</td>
              <td class="p-2">Atmospheric warming caused by trapped infrared radiation.</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Tidal Locking</td>
              <td class="p-2">One side of a planet permanently faces its star.</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Magnetic Field</td>
              <td class="p-2">Protective field generated by a planet's core.</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Plate Tectonics</td>
              <td class="p-2">Movement of a planet's crust that regulates climate.</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Rare Earth Hypothesis</td>
              <td class="p-2">Idea that complex life may be extremely rare.</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Drake Equation</td>
              <td class="p-2">Formula estimating number of intelligent civilizations.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>
