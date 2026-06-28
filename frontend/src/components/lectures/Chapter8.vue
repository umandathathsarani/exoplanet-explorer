<script setup>
</script>

<template>
  <div class="space-y-12 leading-relaxed text-lg text-gray-300">
    <!-- Header -->
    <div class="border-b border-white/10 pb-8">
      <h1 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-2">Chapter 8</h1>
      <p class="text-xl text-[#00bfff] font-light">Searching for Life Beyond Earth</p>
    </div>

    <!-- Images Gallery -->
    <div class="grid md:grid-cols-3 gap-4">
      <img src="https://images.openai.com/static-rsc-4/9-odexIaygb1QfAro78iJt3SdkKGJb3Iy_zdqR-fzGi4HKWhBqj9FpOhqiQnOzPuyeKa5HBWhTt00g5-Q2-g_V5yZ9eowPBLH_y3Z3frH_x7vHwRT0P2bdG3t4Xllue7_27PLW0ZJZ2ggMImT0SKwkjqt87knQIGR69r2kdXz-Mh1wuwD6gKVrrAC77j2ldr?purpose=fullsize" class="w-full h-48 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-1.png'" />
      <img src="https://images.openai.com/static-rsc-4/H6fKARPqTp8pkGtpffOEqfsw9q9vdaHAGmYwlKuUwitcWoijEIJE_rpzO8nahA91U7q3pHLIGPZ1maQUERMTPE8l1YJ8xirTfehDVbSmCWixRcLHmL3PSUqx1LfC1eruz5H6pIFuvl-3hGlRRKsgCC4k-THs3JfDKnpwqMN4_yjuoA5PSgskRl95dkKtIne1?purpose=fullsize" class="w-full h-48 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-2.png'" />
      <img src="https://images.openai.com/static-rsc-4/QvfPWoDb_gEL6ud4Y2R3wic1nM6qbOwh8XdeMxauFNSGwA9KdhYKo-vaZEuNZS6hRXYts4-DXbegCcrBoEHibY1njAFyASuxzCORcM3OAvtwiJ6am8h3-O3CmEp2olQ2FkbDx7a5WrEoXxAzplqoaH4fVGX9n2SNXKXI1Sn0sGm5LIjq7WO6VAR4UQkhKLwj?purpose=fullsize" class="w-full h-48 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-3.png'" />
    </div>

    <!-- Learning Objectives -->
    <section class="bg-black/40 p-6 rounded-2xl border border-white/10 mt-8">
      <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" /></svg>
        Learning Objectives
      </h2>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 text-sm marker:text-[#00bfff]">
        <li>Explain what biosignatures and technosignatures are.</li>
        <li>Understand how scientists search for signs of life on exoplanets.</li>
        <li>Describe the importance of Earth as a reference for life detection.</li>
        <li>Identify key gases that may indicate biological activity.</li>
        <li>Understand extremophiles and their relevance to astrobiology.</li>
        <li>Explain the limitations of current life-detection technology.</li>
        <li>Describe promising exoplanets for habitability studies.</li>
        <li>Understand why detecting life is extremely challenging.</li>
      </ul>
    </section>

    <!-- 8.1 Introduction & 8.2 What is Life? -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">8.1 Introduction</h2>
      <p class="mb-4">One of the most profound questions in science is: <strong>"Is Earth the only planet where life exists?"</strong></p>
      
      <p class="mb-4">To answer this, scientists do not search for creatures directly. Instead, they search for <strong>indirect evidence of life</strong>, such as chemical changes in a planet’s atmosphere or unusual energy patterns. This field of study is called <strong>astrobiology</strong>.</p>
      
      <h3 class="text-xl font-bold text-white mt-8 mb-4">8.2 What Is Life?</h3>
      <p class="mb-4">Before searching for life elsewhere, scientists must first define it. Life on Earth generally has the following characteristics:</p>
      <ul class="list-disc pl-6 space-y-1 text-gray-200">
        <li>Ability to grow</li>
        <li>Ability to reproduce</li>
        <li>Metabolism (energy use)</li>
        <li>Response to environment</li>
        <li>Ability to evolve</li>
      </ul>
      <p class="mt-4 italic text-sm text-yellow-400">However, scientists are careful: life elsewhere may not behave exactly like Earth life. This makes detection even more difficult.</p>
    </section>

    <!-- 8.3 & 8.4 Biosignatures -->
    <section>
      <div class="bg-black/30 p-8 rounded-3xl border border-[#00bfff]/20">
        <h2 class="text-2xl font-bold text-[#00bfff] mb-4">8.3 Biosignatures</h2>
        <p class="mb-4">A <strong>biosignature</strong> is any substance, pattern, or phenomenon that may indicate the presence of life.</p>
        
        <div class="grid md:grid-cols-2 gap-8">
          <div>
            <h3 class="font-bold text-white mb-2">Common atmospheric biosignatures:</h3>
            <ul class="list-disc pl-5 text-gray-300 space-y-1">
              <li>Oxygen (O₂)</li>
              <li>Ozone (O₃)</li>
              <li>Methane (CH₄)</li>
              <li>Carbon dioxide (CO₂)</li>
              <li>Water vapor (H₂O)</li>
              <li>Nitrous oxide (N₂O)</li>
            </ul>
          </div>
          <div>
            <h3 class="font-bold text-white mb-2">Why These Gases Matter</h3>
            <p class="text-sm text-gray-300">On Earth, Oxygen is produced by photosynthesis. Methane is produced by biological and geological processes. The combination of oxygen + methane is especially interesting because they react quickly and should not coexist in large amounts without continuous replenishment.</p>
          </div>
        </div>

        <div class="bg-yellow-900/20 border-l-4 border-yellow-500 p-4 rounded-r-lg mt-6">
          <p class="text-sm text-yellow-400"><strong>Important Warning:</strong> A biosignature is not proof of life. Non-biological processes can also produce similar gases. Scientists must carefully rule out false positives.</p>
        </div>

        <h2 class="text-xl font-bold text-[#00bfff] mt-8 mb-4">8.4 How Biosignatures Are Detected</h2>
        <p class="text-gray-300 mb-4">Scientists use <strong>spectroscopy</strong> to analyze light from a star passing through a planet’s atmosphere.</p>
        <div class="bg-black/50 p-4 rounded-lg font-mono text-sm text-gray-400 mb-4 whitespace-pre overflow-x-auto">
Star light → Planet atmosphere → Telescope

Absorption lines = chemical fingerprint
        </div>
        <p class="text-sm text-gray-400">Each gas absorbs specific wavelengths of light, creating a unique spectral pattern. The James Webb Space Telescope is currently one of the most powerful tools for this type of analysis.</p>
      </div>
    </section>

    <!-- 8.5 Technosignatures -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">8.5 Technosignatures (Signs of Intelligent Life)</h2>
      <p class="mb-4">Unlike biosignatures, <strong>technosignatures</strong> are evidence of technology. Possible technosignatures include:</p>
      
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-4 my-6">
        <div class="bg-white/5 p-4 rounded-xl text-center border border-white/10">
          <p class="text-sm font-bold text-blue-400">Radio Signals</p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl text-center border border-white/10">
          <p class="text-sm font-bold text-red-400">Laser Pulses</p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl text-center border border-white/10">
          <p class="text-sm font-bold text-green-400">Industrial Pollutants</p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl text-center border border-white/10">
          <p class="text-sm font-bold text-yellow-400">City Lights</p>
        </div>
        <div class="bg-white/5 p-4 rounded-xl text-center border border-white/10">
          <p class="text-sm font-bold text-purple-400">Megastructures</p>
        </div>
      </div>
      
      <p class="mb-4 text-sm text-gray-300">Projects like SETI (Search for Extraterrestrial Intelligence) listen for narrow-band radio signals, repeating patterns, and non-random transmissions. So far, no confirmed technosignatures have been detected.</p>
    </section>

    <!-- 8.6 & 8.7 Earth & Extremophiles -->
    <section>
      <div class="grid md:grid-cols-2 gap-8">
        <div>
          <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-green-500 pl-4">8.6 Earth as a Reference Model</h2>
          <p class="text-gray-300 mb-4">Earth is the only known planet with life, so it is used as a <strong>baseline model</strong>. Scientists study Earth’s atmospheric composition, biological cycles, ocean chemistry, and seasonal variations.</p>
          <p class="text-sm text-gray-400 italic">However, this creates a limitation: Life elsewhere may not resemble Earth life at all.</p>
        </div>
        
        <div>
          <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-orange-500 pl-4">8.7 Extremophiles</h2>
          <p class="text-gray-300 mb-4">On Earth, life exists in extreme environments (deep ocean vents, acidic lakes, frozen ice). These organisms are <strong>extremophiles</strong>.</p>
          <p class="text-sm text-gray-400">They prove that life can survive without sunlight, under extreme pressure, in toxic environments, and at extreme temperatures. This expands the range of possible habitable environments on exoplanets.</p>
        </div>
      </div>
    </section>

    <!-- 8.8 to 8.11 False Positives -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">8.8 Habitable Exoplanets & 8.9 The Role of Water</h2>
      <p class="mb-4">Promising candidates for further study include Proxima Centauri b, TRAPPIST-1e, and Kepler-186f. They are studied for atmospheric composition, surface temperature, radiation environment, and water presence.</p>
      <p class="mb-6">Water is prioritized because it supports chemical reactions, stabilizes temperature, and dissolves biological molecules.</p>
      
      <div class="bg-red-900/20 p-6 rounded-2xl border border-red-500/30">
        <h3 class="text-xl font-bold text-red-400 mb-4">8.10 False Positives & 8.11 Atmospheric Context</h3>
        <p class="text-gray-300 mb-4">One of the biggest challenges is avoiding misinterpretation. False positives include oxygen from photochemical reactions or methane from volcanic activity.</p>
        <ul class="list-disc pl-5 text-sm text-gray-300 space-y-1 mb-4">
          <li><strong>Oxygen + Methane together</strong> → Strong potential biosignature</li>
          <li><strong>Carbon dioxide alone</strong> → Not sufficient</li>
          <li><strong>Water vapor alone</strong> → Not sufficient</li>
        </ul>
        <p class="text-sm text-red-300 font-bold">Context is everything in astrobiology. Multiple lines of evidence are required before claiming life.</p>
      </div>
    </section>

    <!-- 8.12 to 8.15 -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">8.12 Earth 2.0 & 8.13 Current Limits</h2>
      <p class="mb-4">Scientists are searching for <strong>Earth analogs</strong>—Earth-sized planets in habitable zones with stable atmospheres and liquid water potential. However, no confirmed "Earth 2.0" has been found.</p>
      <p class="mb-6">Current limits include: small planets are hard to analyze, signals are extremely weak, and interstellar distances are enormous. Detections are mostly indirect and probabilistic.</p>

      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">8.14 Future Missions & 8.15 Philosophy</h2>
      <p class="mb-4">Future telescopes aim to detect smaller biosignatures, image Earth-like planets directly, and search for technosignatures more effectively.</p>
      <p class="text-gray-300 italic">The search for life raises deep philosophical questions: Is life common or rare? Are we early or late in the universe's timeline? What would discovery mean for humanity?</p>
    </section>

    <!-- Summary -->
    <section class="bg-[#0a0a1a] p-8 rounded-2xl border border-white/20 mt-12">
      <h2 class="text-2xl font-bold text-white mb-6">Chapter Summary</h2>
      <ul class="list-disc pl-5 space-y-3 text-gray-300 text-sm md:text-base">
        <li>Biosignatures are chemical indicators of possible life, while technosignatures indicate intelligent technology.</li>
        <li>Spectroscopy is the main method used to study exoplanet atmospheres.</li>
        <li>Earth is used as a reference model, but extremophiles show life can survive in extreme conditions.</li>
        <li>False positives make life detection extremely challenging.</li>
        <li>Future telescopes may significantly improve our ability to detect life.</li>
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
              <td class="p-2 font-bold text-[#00bfff]">Astrobiology</td>
              <td class="p-2">Study of life in the universe</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Biosignature</td>
              <td class="p-2">Chemical or physical sign of possible life</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Technosignature</td>
              <td class="p-2">Evidence of technological civilization</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Extremophile</td>
              <td class="p-2">Organism that survives extreme conditions</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">False Positive</td>
              <td class="p-2">Signal that appears biological but is not</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>
