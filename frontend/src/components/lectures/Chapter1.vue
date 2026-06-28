<script setup>
</script>

<template>
  <div class="space-y-12 leading-relaxed text-lg text-gray-300">
    <!-- Header -->
    <div class="border-b border-white/10 pb-8">
      <h1 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-2">Chapter 1</h1>
      <p class="text-xl text-[#00bfff] font-light">Introduction to Exoplanets and the History of Their Discovery</p>
    </div>

    <!-- Learning Objectives -->
    <section class="bg-black/40 p-6 rounded-2xl border border-white/10">
      <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" /></svg>
        Learning Objectives
      </h2>
      <p class="mb-4 text-sm">By the end of this chapter, you should be able to:</p>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 text-sm marker:text-[#00bfff]">
        <li>Define what an exoplanet is.</li>
        <li>Explain the difference between planets in our Solar System and exoplanets.</li>
        <li>Understand why the search for exoplanets is important.</li>
        <li>Describe the historical development of exoplanet discoveries.</li>
        <li>Explain why the discovery of exoplanets transformed modern astronomy.</li>
        <li>Identify major milestones in exoplanet research.</li>
      </ul>
    </section>

    <!-- 1.1 Introduction -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">1.1 Introduction</h2>
      <p class="mb-4">For as long as humans have looked at the night sky, they have wondered whether Earth is unique or whether other worlds exist beyond our own. Ancient civilizations observed countless stars scattered across the sky and imagined that some of them might have planets like the ones orbiting our Sun. However, for most of human history, there was no scientific evidence that planets existed around other stars.</p>
      <p class="mb-4">Today, we know that our galaxy is filled with planetary systems. Thousands of planets have been discovered orbiting stars beyond our Solar System, and scientists estimate that there may be <strong>hundreds of billions of planets</strong> in the Milky Way alone. This realization has fundamentally changed our understanding of the universe and our place within it.</p>
      <p class="mb-4">These distant worlds are called <strong>exoplanets</strong>, and their discovery is one of the greatest achievements in modern astronomy.</p>
    </section>

    <!-- 1.2 What Is an Exoplanet? -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">1.2 What Is an Exoplanet?</h2>
      <p class="mb-4">The word <strong>exoplanet</strong> comes from the prefix <strong>"exo,"</strong> meaning <em>outside</em> or <em>beyond</em>. An exoplanet is therefore a planet that exists beyond our Solar System.</p>
      
      <h3 class="text-xl font-semibold text-gray-100 mb-2">Definition</h3>
      <blockquote class="border-l-4 border-purple-500 bg-purple-900/20 p-4 rounded-r-lg italic text-gray-200 mb-6">
        An exoplanet is a natural celestial body that orbits a star other than the Sun and has sufficient mass for its own gravity to give it a nearly spherical shape.
      </blockquote>
      <p class="mb-6">Unlike stars, exoplanets do not produce their own light through nuclear fusion. Instead, they reflect light from their host stars, much like Earth reflects sunlight.</p>
      
      <h3 class="text-xl font-semibold text-gray-100 mb-2">Visual Comparison</h3>
      <div class="grid md:grid-cols-2 gap-6 mb-4">
        <div class="bg-black/40 p-6 rounded-xl border border-white/10">
          <h4 class="font-bold text-[#00bfff] mb-4 text-center">Our Solar System</h4>
          <pre class="font-mono text-xs sm:text-sm text-gray-400 text-center">
               Sun
                ☀
      ┌─────────┼─────────┐
      │         │         │
   Mercury    Earth    Jupiter
          </pre>
          <p class="text-center text-xs mt-2 italic">(All orbit the Sun)</p>
        </div>
        <div class="bg-black/40 p-6 rounded-xl border border-white/10">
          <h4 class="font-bold text-[#00bfff] mb-4 text-center">Another Star System</h4>
          <pre class="font-mono text-xs sm:text-sm text-gray-400 text-center">
             Alpha Star
                 ★
      ┌──────────┼──────────┐
      │          │          │
 Planet A    Planet B    Planet C
          </pre>
          <p class="text-center text-xs mt-2 italic">(All are exoplanets from Earth's perspective)</p>
        </div>
      </div>
      <p class="mb-4">The planets orbiting the Sun—Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune—are <strong>not</strong> exoplanets. However, if an observer living around another star looked at Earth, they would consider Earth to be an exoplanet because it orbits a different star from their own.</p>
    </section>

    <!-- 1.3 Our Solar System in Context -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">1.3 Our Solar System in Context</h2>
      <p class="mb-4">Before studying exoplanets, it is useful to understand our own Solar System because it serves as the basis for comparison.</p>
      <p class="mb-2">The Solar System consists of:</p>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 mb-4 marker:text-[#00bfff]">
        <li>The Sun</li>
        <li>Eight planets</li>
        <li>More than 200 known moons</li>
        <li>Dwarf planets</li>
        <li>Asteroids, Comets, Meteoroids, Dust and gas</li>
      </ul>
      <p class="mb-4">For many years, scientists assumed that most planetary systems would resemble our Solar System. However, discoveries over the past three decades have shown that planetary systems can be dramatically different. Some planetary systems contain giant planets orbiting closer to their stars than Mercury is to the Sun. Others contain several Earth-sized planets packed into very small regions. These discoveries have challenged long-held theories about how planetary systems form and evolve.</p>
    </section>

    <!-- 1.4 Why Are Exoplanets Important? -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">1.4 Why Are Exoplanets Important?</h2>
      <p class="mb-6">The discovery of exoplanets has expanded astronomy from the study of our Solar System to the study of planetary systems throughout the universe. Scientists study exoplanets to answer some of the biggest questions in science:</p>
      
      <div class="grid sm:grid-cols-2 gap-6">
        <div class="bg-white/5 p-5 rounded-xl border border-white/10 hover:border-white/30 transition">
          <h3 class="text-lg font-bold text-[#00bfff] mb-2">Are We Alone?</h3>
          <p class="text-sm text-gray-300">One of humanity's oldest questions is whether life exists elsewhere in the universe. If planets similar to Earth are common, then environments capable of supporting life may also be common.</p>
        </div>
        <div class="bg-white/5 p-5 rounded-xl border border-white/10 hover:border-white/30 transition">
          <h3 class="text-lg font-bold text-[#00bfff] mb-2">How Do Planets Form?</h3>
          <p class="text-sm text-gray-300">Before exoplanets were discovered, theories of planet formation were based only on our Solar System. By observing many different planetary systems, astronomers can test and refine these theories.</p>
        </div>
        <div class="bg-white/5 p-5 rounded-xl border border-white/10 hover:border-white/30 transition">
          <h3 class="text-lg font-bold text-[#00bfff] mb-2">How Rare Is Earth?</h3>
          <p class="text-sm text-gray-300">Earth possesses many characteristics that support life, including liquid water, a protective atmosphere, and moderate temperatures. Scientists want to know whether similar planets exist elsewhere.</p>
        </div>
        <div class="bg-white/5 p-5 rounded-xl border border-white/10 hover:border-white/30 transition">
          <h3 class="text-lg font-bold text-[#00bfff] mb-2">How Common Are Planetary Systems?</h3>
          <p class="text-sm text-gray-300">The discovery of thousands of exoplanets has shown that planets are not unusual. Current estimates suggest that most stars in the Milky Way likely have at least one planet.</p>
        </div>
      </div>
    </section>

    <!-- 1.5 - 1.6 History -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">1.5 Ancient Ideas & 1.6 The Scientific Revolution</h2>
      <p class="mb-4">The idea that other worlds might exist is much older than modern astronomy. Around 2,400 years ago, the Greek philosopher Democritus proposed that the universe contained countless worlds. Later, Epicurus argued that there could be an infinite number of worlds scattered throughout the universe. However, these ideas remained philosophical because no technology existed to test them.</p>
      
      <p class="mb-4">The Scientific Revolution transformed our understanding of the universe:</p>
      <ul class="list-disc pl-6 space-y-4 text-gray-200 marker:text-purple-400">
        <li><strong>Nicolaus Copernicus:</strong> In the 16th century, he proposed that Earth revolves around the Sun rather than the Sun revolving around Earth.</li>
        <li><strong>Galileo Galilei:</strong> Using one of the first telescopes, he observed moons orbiting Jupiter. This demonstrated that not everything revolves around Earth.</li>
        <li><strong>Johannes Kepler:</strong> He discovered that planets move in elliptical orbits rather than perfect circles. His laws remain fundamental today.</li>
      </ul>
    </section>

    <!-- 1.7 Why Were Exoplanets So Difficult to Discover? -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">1.7 Why Were Exoplanets So Difficult to Discover?</h2>
      <p class="mb-4">Although stars are incredibly bright, planets are comparatively faint. This makes detecting exoplanets one of the greatest observational challenges in astronomy. There are several reasons:</p>
      
      <div class="space-y-4 text-gray-300">
        <div class="bg-black/30 p-4 rounded-lg">
          <h4 class="font-bold text-white">Vast Distances</h4>
          <p class="text-sm">The nearest known exoplanet is more than four light-years away. Most are tens, hundreds, or thousands of light-years from Earth.</p>
        </div>
        <div class="bg-black/30 p-4 rounded-lg">
          <h4 class="font-bold text-white">Bright Host Stars</h4>
          <p class="text-sm">A star can be millions or billions of times brighter than its planets. The star's intense light often overwhelms the faint reflected light from the planets. <em>Analogy: Trying to spot a tiny firefly flying next to a powerful lighthouse from many kilometers away.</em></p>
        </div>
        <div class="bg-black/30 p-4 rounded-lg">
          <h4 class="font-bold text-white">Small Planetary Size</h4>
          <p class="text-sm">Compared with stars, planets are extremely small. Even Jupiter, the largest planet in our Solar System, is tiny compared to the Sun.</p>
          <pre class="font-mono text-xs text-gray-500 mt-2">
Sun    OOOOOOOOOOOOOOOOOOOOOOOO
Earth  o
          </pre>
        </div>
      </div>
      <p class="mt-4 text-sm italic">Because of these challenges, astronomers usually detect exoplanets indirectly, by observing their effects on their host stars rather than seeing the planets themselves.</p>
    </section>

    <!-- 1.8 - 1.10 Discoveries & Learnings -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">1.8 The First Discoveries & The Exoplanet Revolution</h2>
      <p class="mb-4">The first confirmed planets beyond our Solar System were discovered in the early 1990s orbiting a pulsar, a rapidly rotating neutron star.</p>
      <p class="mb-4">A major breakthrough came in <strong>1995</strong> with the discovery of <strong>51 Pegasi b</strong>. This planet was found orbiting a Sun-like star approximately 50 light-years from Earth. It was a <strong>Hot Jupiter</strong>, a giant gas planet orbiting very close to its star. Before this discovery, astronomers did not expect such planets to exist because our own Solar System has no similar example.</p>
      <p class="mb-4">Following 51 Pegasi b, astronomers developed increasingly powerful telescopes. Dedicated space missions like Kepler, TESS, and James Webb have accelerated the pace of discovery.</p>
      
      <div class="bg-gradient-to-r from-purple-900/30 to-[#00bfff]/20 p-6 rounded-2xl border border-[#00bfff]/30 mt-6">
        <h3 class="text-xl font-bold text-white mb-4">What Have We Learned?</h3>
        <ul class="list-disc pl-5 space-y-2 text-gray-200">
          <li>Some planets are larger than Jupiter, others smaller than Earth.</li>
          <li>Some orbit two stars instead of one.</li>
          <li>Some have years lasting only a few hours, others take centuries.</li>
          <li>Certain planets may have lava oceans or be covered by deep global oceans.</li>
          <li>A few are located within their stars' habitable zones.</li>
        </ul>
        <p class="mt-4 font-medium text-white italic">These discoveries show that nature creates planetary systems in many different ways.</p>
      </div>
    </section>

    <!-- Chapter Summary -->
    <section class="bg-[#0a0a1a] p-8 rounded-2xl border border-white/20 mt-12">
      <h2 class="text-2xl font-bold text-white mb-6">Chapter Summary</h2>
      <ul class="list-disc pl-5 space-y-3 text-gray-300">
        <li>An <strong>exoplanet</strong> is a planet orbiting a star other than the Sun.</li>
        <li>Humans have wondered about other worlds since ancient times.</li>
        <li>Exoplanets are difficult to detect because they are small, faint, and far away.</li>
        <li>The discovery of <strong>51 Pegasi b</strong> in 1995 marked the beginning of modern exoplanet science.</li>
        <li>Thousands of exoplanets have now been confirmed, revealing an incredible diversity.</li>
        <li>Studying exoplanets helps scientists understand planet formation, the uniqueness of Earth, and the possibility of life elsewhere in the universe.</li>
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
              <td class="p-2 font-bold text-[#00bfff]">Exoplanet</td>
              <td class="p-2">A planet orbiting a star other than the Sun.</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Host Star</td>
              <td class="p-2">The star around which an exoplanet orbits.</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Light-Year</td>
              <td class="p-2">The distance light travels in one year (about 9.46 trillion km).</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Hot Jupiter</td>
              <td class="p-2">A gas giant that orbits very close to its star.</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Habitable Zone</td>
              <td class="p-2">The region around a star where liquid water could exist on a planet's surface.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="text-xl font-bold text-white mt-8 mb-4">Review Questions</h3>
      <ol class="list-decimal pl-5 space-y-2 text-gray-300 text-sm">
        <li>Define an exoplanet in your own words.</li>
        <li>Why are exoplanets difficult to observe directly?</li>
        <li>Why was the discovery of 51 Pegasi b considered revolutionary?</li>
        <li>How did the work of Copernicus, Galileo, and Kepler contribute to modern exoplanet science?</li>
        <li>List three reasons why scientists study exoplanets.</li>
      </ol>
    </section>
  </div>
</template>
