<script setup>
</script>

<template>
  <div class="space-y-12 leading-relaxed text-lg text-gray-300">
    <!-- Header -->
    <div class="border-b border-white/10 pb-8">
      <h1 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-2">Chapter 7</h1>
      <p class="text-xl text-[#00bfff] font-light">Atmospheres, Climate, and Weather on Exoplanets</p>
    </div>

    <!-- Images Gallery -->
    <div class="grid md:grid-cols-3 gap-4">
      <img src="https://images.openai.com/static-rsc-4/Bcv5Q6UQQUhxi7-_X2voNIOZFAXiU0XrS7Sg-Y5xg6keiKzgYZz2MUObtIhL67e9Mh_qrbEi6Kp_0uCC72piiiBDD-aHvazFIghf-hUdYY2GKmS-9EqXGQxIJN1UvsgT491Jtw-ORa_HHEPo-bbhRAdEUGVRKuabxD6k5uJepLI1l9G6YOAC6ZD6qR5ouJaw?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-1.png'" />
      <img src="https://images.openai.com/static-rsc-4/QvfPWoDb_gEL6ud4Y2R3wic1nM6qbOwh8XdeMxauFNSGwA9KdhYKo-vaZEuNZS6hRXYts4-DXbegCcrBoEHibY1njAFyASuxzCORcM3OAvtwiJ6am8h3-O3CmEp2olQ2FkbDx7a5WrEoXxAzplqoaH4fVGX9n2SNXKXI1Sn0sGm5LIjq7WO6VAR4UQkhKLwj?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-2.png'" />
      <img src="https://images.openai.com/static-rsc-4/RON2E6yzibIjlYR418qfow7j6XP4gT22HkGPRGRH_oLwKgCe_5T2EUOggaEoTKGeJMNlSGbg-Dc853aRAZLIxteGKgvzmwyl0fegG9zYg336My5RX4jYHPTlLesN-FwQ4f4mLjJfM43AsJ_CDC_j7mnhxSsvPsL4otIQrzi97Olz9Og5IW8UgUTp5KsSNnQX?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-3.png'" />
    </div>

    <!-- Learning Objectives -->
    <section class="bg-black/40 p-6 rounded-2xl border border-white/10">
      <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" /></svg>
        Learning Objectives
      </h2>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 text-sm marker:text-[#00bfff]">
        <li>Explain what exoplanet atmospheres are made of and how they are studied.</li>
        <li>Understand how weather and climate systems form on different types of exoplanets.</li>
        <li>Describe extreme atmospheric phenomena on hot Jupiters and lava worlds.</li>
        <li>Explain how temperature, pressure, and chemistry shape planetary atmospheres.</li>
        <li>Understand atmospheric escape and long-term evolution of planets.</li>
        <li>Describe how telescopes analyze exoplanet atmospheres using spectroscopy.</li>
        <li>Compare Earth's climate system with alien climate systems.</li>
      </ul>
    </section>

    <!-- 7.1 to 7.3 -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">7.1 Introduction & 7.2 Atmospheres</h2>
      <p class="mb-4">When we think of "weather," we usually imagine clouds, rain, wind, and storms on Earth. However, weather is not unique to Earth. Every planet with an atmosphere can have <strong>climate systems and weather patterns</strong>, even if they are extremely different from what we experience.</p>
      
      <p class="mb-4">On exoplanets, weather can be extreme beyond imagination:</p>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 mb-4">
        <li>Iron clouds raining molten metal</li>
        <li>Winds traveling faster than sound</li>
        <li>Atmospheres evaporating into space</li>
        <li>Planets covered in global oceans of lava</li>
        <li>Gas giants with giant storm systems larger than Earth itself</li>
      </ul>
      <p class="mb-4">An <strong>atmosphere</strong> is a layer of gas surrounding a planet, held in place by gravity. Common gases found on exoplanets include Hydrogen (H₂), Helium (He), Water vapor (H₂O), Carbon dioxide (CO₂), Methane (CH₄), Sodium (Na), and Potassium (K).</p>
    </section>

    <!-- 7.4 Spectroscopy -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">7.4 How Do Scientists Study Exoplanet Atmospheres?</h2>
      <p class="mb-4">Because exoplanets are extremely far away, we cannot directly sample their air. Instead, scientists use <strong>light analysis (spectroscopy)</strong>.</p>
      
      <div class="bg-black/30 p-6 rounded-xl border border-white/10 mb-6">
        <h3 class="text-xl font-bold text-[#00bfff] mb-2">Transmission Spectroscopy</h3>
        <p class="text-sm mb-4">When a planet passes in front of its star, some starlight passes through its atmosphere. Different gases absorb different wavelengths of light.</p>
        <div class="bg-black/50 p-4 rounded-lg font-mono text-sm text-gray-300 whitespace-pre overflow-x-auto">
Star Light → | Atmosphere | → Telescope
        </div>
        <p class="text-sm mt-4">This creates a <strong>chemical signature</strong> that reveals atmospheric composition. The James Webb Space Telescope has revolutionized this field.</p>
      </div>
    </section>

    <!-- Weather Systems -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-6 border-l-4 border-[#00bfff] pl-4">Extreme Weather on Different Planets</h2>
      
      <div class="space-y-6">
        <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
          <h3 class="text-xl font-bold text-blue-400 mb-2">7.6 Weather on Gas Giants & 7.7 Hot Jupiters</h3>
          <p class="text-sm mb-4 text-gray-300">Gas giants like Jupiter and many exoplanets have extremely dynamic atmospheres with strong jet streams, massive storms, cloud bands, and lightning. On <strong>Hot Jupiters</strong>, these storms are intensified by extreme heat.</p>
          <div class="bg-black/30 p-4 rounded-lg border-l-4 border-purple-500">
            <h4 class="font-bold text-white">Example: HD 189733 b (Glass Rain)</h4>
            <p class="text-sm mt-1">Winds exceeding 8,000 km/h and temperatures over 1,000°C. Silicate particles lift high into the atmosphere, condense, and fall as <strong>molten glass rain</strong>, but sideways due to extreme winds.</p>
          </div>
        </div>

        <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
          <h3 class="text-xl font-bold text-red-500 mb-2">7.8 Lava World Atmospheres</h3>
          <p class="text-sm mb-4 text-gray-300">On lava planets, the atmosphere is not stable like Earth's. The surface is a global magma ocean where rock evaporates into the atmosphere.</p>
          <ul class="text-sm list-decimal pl-5 space-y-1 text-gray-400">
            <li>Rock evaporates on hot side</li>
            <li>Vapors move to cooler side</li>
            <li>Rock condenses and "rains" as molten droplets</li>
            <li>Material flows back into magma ocean</li>
          </ul>
        </div>
        
        <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
          <h3 class="text-xl font-bold text-cyan-400 mb-2">7.9 Weather on Ice Giants and Mini-Neptunes</h3>
          <p class="text-sm text-gray-300">These planets have thick atmospheres with complex chemistry. Features include high-altitude clouds, methane storms, and deep atmospheric pressure layers. In extreme pressure environments, carbon compounds may crystallize into <strong>diamond rain</strong>.</p>
        </div>
      </div>
    </section>

    <!-- 7.10 to 7.12 -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">7.10 Cloud Formation & 7.11 Atmospheric Escape</h2>
      <p class="mb-4">Clouds form when gases cool and condense. Unlike Earth's water clouds, exoplanets can have iron clouds, silicate clouds (rock dust), ammonia clouds, and methane clouds.</p>
      
      <div class="bg-black/30 p-6 rounded-xl border border-white/10 mb-6">
        <h3 class="text-lg font-bold text-[#00bfff] mb-2">Atmospheric Escape (e.g. HD 209458 b)</h3>
        <p class="text-sm text-gray-300">Some planets slowly lose their atmospheres into space. Star emits strong radiation → upper atmosphere heats up → gas molecules gain escape velocity → atmosphere forms a long trailing tail, similar to a comet.</p>
      </div>

      <h3 class="text-xl font-bold text-white mt-8 mb-4">7.12 Tidal Locking and Climate</h3>
      <p class="mb-4">Many exoplanets orbit close to red dwarf stars and become tidally locked. This creates unique climate zones: permanent day side (extreme heat), permanent night side (freezing cold), and twilight zone (possible stable temperatures). Strong winds may transfer heat between hemispheres.</p>
    </section>

    <!-- 7.16 Comparison -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">7.16 Comparing Earth's Weather with Exoplanets</h2>
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-sm">
          <thead>
            <tr class="border-b border-white/20 bg-white/5">
              <th class="p-3 text-white">Feature</th>
              <th class="p-3 text-[#00bfff]">Earth</th>
              <th class="p-3 text-red-400">Hot Jupiter</th>
              <th class="p-3 text-orange-500">Lava Planet</th>
            </tr>
          </thead>
          <tbody class="text-gray-300">
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold">Clouds</td>
              <td class="p-3">Water</td>
              <td class="p-3">Silicate / metal</td>
              <td class="p-3">Rock vapor</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold">Winds</td>
              <td class="p-3">Up to 400 km/h</td>
              <td class="p-3">Up to 8,000 km/h</td>
              <td class="p-3">Extreme vapor flows</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold">Rain</td>
              <td class="p-3">Water</td>
              <td class="p-3">Glass / silicates</td>
              <td class="p-3">Molten rock</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold">Temperature</td>
              <td class="p-3">Moderate</td>
              <td class="p-3">Extreme hot</td>
              <td class="p-3">Ultra-hot</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-3 font-semibold">Atmosphere</td>
              <td class="p-3">Stable N₂/O₂</td>
              <td class="p-3">Hydrogen/helium</td>
              <td class="p-3">Vaporized rock</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Summary -->
    <section class="bg-[#0a0a1a] p-8 rounded-2xl border border-white/20 mt-12">
      <h2 class="text-2xl font-bold text-white mb-6">Chapter Summary</h2>
      <ul class="list-disc pl-5 space-y-3 text-gray-300 text-sm md:text-base">
        <li>Atmospheres regulate climate and enable weather systems on planets.</li>
        <li>Exoplanet atmospheres can be composed of hydrogen, methane, water vapor, metals, and rock vapor.</li>
        <li>Scientists study atmospheres using <strong>spectroscopy and space telescopes</strong> like James Webb Space Telescope.</li>
        <li>Hot Jupiters can have extreme winds and glass rain.</li>
        <li>Lava planets can have rock vapor atmospheres and magma oceans.</li>
        <li>Ice giants and mini-Neptunes may experience exotic cloud chemistry and deep atmospheric processes.</li>
        <li>Some planets lose their atmospheres over time due to stellar radiation.</li>
        <li>Climate stability is crucial for long-term habitability.</li>
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
              <td class="p-2 font-bold text-[#00bfff]">Spectroscopy</td>
              <td class="p-2">Technique to analyze light for chemical composition</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Atmospheric Escape</td>
              <td class="p-2">Loss of gases into space</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Jet Stream</td>
              <td class="p-2">Fast-moving atmospheric wind band</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Cloud Condensation</td>
              <td class="p-2">Formation of clouds from cooling gases</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

  </div>
</template>
