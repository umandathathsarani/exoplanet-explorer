<script setup>
</script>

<template>
  <div class="space-y-12 leading-relaxed text-lg text-gray-300">
    <!-- Header -->
    <div class="border-b border-white/10 pb-8">
      <h1 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-2">Chapter 9</h1>
      <p class="text-xl text-[#00bfff] font-light">Space Missions and Future Exploration</p>
    </div>

    <!-- Images Gallery Top -->
    <div class="grid md:grid-cols-3 gap-4">
      <img src="https://images.openai.com/static-rsc-4/f5a0gQx3tIVkiydt3G9ZdKzIP95zEvx_V_ffZdktC1AEyPGKOdIyMA0mYMnP454CtOqYpB6TxhkBfdqItkES5vqKpic58vxMJFQXYyNcv8cn8UyZN307qp9RoSpdEwHRfAWiLhv1YMyAV7zTo8YoWWzoVFtWdR5Ue8daxPNNedfAhGFqi2i6AhIOdxBspCow?purpose=fullsize" class="w-full h-48 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-1.png'" />
      <img src="https://images.openai.com/static-rsc-4/WwVN_mB1wYRq-cWVayulybr0-HC8iLix5x3SoSkyOEPPTB_s0KrZY4AFjgxOPWSKj6DN4SFE32LSnRqRLm1Fa6XIXKBwOlpo2AU_ckdOZpdQXNMT9iYBJwtTs8WRiIBiitqAG13KUE1zzElXDUbxDln8U6XBMPOWv0BUl0u-OQrKZNQ6UhcOArxZ_lF_pTwP?purpose=fullsize" class="w-full h-48 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-2.png'" />
      <img src="https://images.openai.com/static-rsc-4/I1Uq0DnUJJuk9HGFdGDJWFRLMsLWuVrllVkz3-IZ2TD81URTIvrsXf9X8uGWVXvWFGiS2xMXqeTXOClgsaFJI8y6Ifzzi6qd_cctmIKJSJf88uO3Y8UHWp4qsALE7KlMOtTyYHSEixTxQrIIHHWKj9M4POZCdRhfEgwlM4zQFgHWMDcnmtNOx0C42-PYv3eo?purpose=fullsize" class="w-full h-48 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-3.png'" />
    </div>

    <!-- Learning Objectives -->
    <section class="bg-black/40 p-6 rounded-2xl border border-white/10 mt-8">
      <h2 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-[#00bfff]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" /></svg>
        Learning Objectives
      </h2>
      <ul class="list-disc pl-6 space-y-1 text-gray-200 text-sm marker:text-[#00bfff]">
        <li>Understand the major space missions that discovered and studied exoplanets.</li>
        <li>Explain how different telescopes contributed to exoplanet science.</li>
        <li>Describe how space-based and ground-based observatories work together.</li>
        <li>Understand the role of current and future missions in finding habitable planets.</li>
        <li>Explain the importance of direct imaging missions.</li>
        <li>Describe next-generation telescopes and technologies.</li>
        <li>Understand the long-term future of exoplanet exploration.</li>
      </ul>
    </section>

    <!-- 9.1 & 9.2 -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">9.1 Introduction & 9.2 Why Space Missions Are Important</h2>
      <p class="mb-4">Exoplanet science did not develop overnight. It is the result of decades of technological progress, careful planning, and major space missions. Without advanced telescopes, most exoplanets would remain invisible.</p>
      <p class="mb-4">Space telescopes are essential because Earth's atmosphere blocks and distorts many wavelengths of light. Space telescopes avoid atmospheric distortion, observe continuous starlight, detect faint signals, and capture infrared and UV data.</p>
    </section>

    <!-- 9.3 Kepler -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-purple-500 pl-4">9.3 The Kepler Mission</h2>
      <h3 class="text-xl font-bold text-purple-400 mb-4">Kepler Space Telescope</h3>
      
      <div class="grid md:grid-cols-3 gap-4 mb-6">
        <img src="https://images.openai.com/static-rsc-4/_k2NthYdjNJH2l29UAAGYgzpAutOWhxyNlJ3WXzNcb_ICEGuNPFH6W0SVCVw7wge0-Kb_ll7B7Z5A3bCySMUbfDNGjhIHJwsSyNIn-SkVdcK-xXf5qyVMIf45h5O2T1pLSjMANtHhDvuweU8S7W1TSHrJPCYOFJQpGITcqqNTmHTYyhxb_A264Vspq6oJDb-?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-1.png'" />
        <img src="https://images.openai.com/static-rsc-4/uTqJRYyO6Ml_OLa5paDrWeUrKELCLDulY9lFg-nUM3eHQlS1waPk3mgPxNezyqYjd8YTbFC84y68MDF24Hjz7aNwNi7W0OTNN5ZGS8eEB8PA4Czq2QrkfR-RyBJcOzHgi-alXk3l6sSWoGE_yN9kMOktbt3BksK1pzssiu4NIydGCo3-ssVGgf7yrChoWwov?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-2.png'" />
        <img src="https://images.openai.com/static-rsc-4/bBd5vT2lXMbkLOJGhfpO6tC_gMLjN5r-ct3hw6FrypLSWbthDoN1495KntG2zv52a94OiFBTl_p29I5Cfcze_4jGh6dK2drWTZJf3uSxdq-kElRZBq_huzRD9-FMgkDw1u7E1thUIbGfgog9WnoNxVVo6v4ArN_P2k_zpJ80ukMyR4nnL3j_ehPieCp6KEuB?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-3.png'" />
      </div>

      <div class="bg-black/30 p-6 rounded-2xl border border-purple-500/30">
        <ul class="list-disc pl-5 text-gray-300 space-y-1 mb-4">
          <li><strong>Launched:</strong> 2009</li>
          <li><strong>Mission Type:</strong> Planet hunting</li>
          <li><strong>Method:</strong> Transit photometry</li>
          <li><strong>Stars observed:</strong> 150,000+</li>
        </ul>
        <p class="text-gray-300"><strong>Goal:</strong> Answer how common Earth-like planets are. It confirmed thousands of exoplanets and proved that planets are extremely common in the galaxy.</p>
      </div>
    </section>

    <!-- 9.4 TESS -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-blue-500 pl-4">9.4 The TESS Mission</h2>
      <h3 class="text-xl font-bold text-blue-400 mb-4">Transiting Exoplanet Survey Satellite</h3>
      
      <div class="grid md:grid-cols-3 gap-4 mb-6">
        <img src="https://images.openai.com/static-rsc-4/1k0q-8GKoVl4oeCukX0hWNVsBnntcs7JwglvkjOjghMAUUhX6GpWgHAfiTLGQEoXgaGv03nkt-odQaxT9-k35sgb1Mup7hfuzbqe0lKnZFZZZOgp6_2gks7g8iEvlqWbb_8V5fCcefsaD3n0zsEWb1cy3afOdJGwS4lrOY-CcIa3GvvnkF17vUR6iJh80kq-?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-1.png'" />
        <img src="https://images.openai.com/static-rsc-4/sEt5cwlzMMZuXSio4ixzWEhkBc-K5Fl9jGP-gN8kGsQuzTP-qHVAY7pyCUxk16qmyAZq0qVOfdrYWAsWOLKmGvHeEB_TXwtki-lg1DImbrgL3ArsnTG7HfOAExHmAfEzTkkJ5RGm65GtfyuKWm7xfYSSk1sSrAGRrXiC27z8sYsUxRTjC4UvodAGFbT_lRkM?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-2.png'" />
        <img src="https://images.openai.com/static-rsc-4/Vj5cIUpGZ-eAJRKCrSkLLOpSt7JkgnUa0SZLve8CzxK76moHSiOQBgLtpWBS7VrianZvZ8ftmKXXc_q_7AEZ2uu6sF6_zgVYhXurfTx4BiAqIy7S0Bp4XOz8ci6iixjB2lJzFl-Dmy0n18r7EEwaiLVRFpHyJFI8D4g-Xa4ZZqiuTAkjupViq68mRxEEvPrt?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-3.png'" />
      </div>

      <div class="bg-black/30 p-6 rounded-2xl border border-blue-500/30">
        <ul class="list-disc pl-5 text-gray-300 space-y-1 mb-4">
          <li><strong>Launched:</strong> 2018</li>
          <li><strong>Mission:</strong> All-sky survey</li>
        </ul>
        <p class="text-gray-300">Unlike Kepler, TESS scans almost the entire sky, focusing on bright nearby stars. TESS finds planets that are closer to Earth, making them easier to study with telescopes like JWST.</p>
      </div>
    </section>

    <!-- 9.5 JWST -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-yellow-500 pl-4">9.5 The James Webb Space Telescope</h2>
      <h3 class="text-xl font-bold text-yellow-400 mb-4">James Webb Space Telescope</h3>
      
      <div class="grid md:grid-cols-3 gap-4 mb-6">
        <img src="https://images.openai.com/static-rsc-4/DWZt_Yd-DW08bENmt5QXYh9OLKI_GeYpuN7UvnHH1t22wovDmLKYFvK1IjKnWcxO8yoavYpXZ7FY08VSPPVOda7iISQYSH1KwYJL0Fx00vMWYoX6_pNykCkYsL7TIRzTWpyLNm_XLWDJvYdaJ57YPGCz9xQMoFpwrw6CtqkaXfkToGlCuL32um2ktCana9Xo?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-1.png'" />
        <img src="https://images.openai.com/static-rsc-4/MDFHstt11jKGOclWGPwNFo0DXFu9FRqy3QsEy1Tg1X37Xem8JwDMznkoaU62UPtaMPRwWGw5xw8KI-bGYqRZDRwGxO2LlkS5qQIyIkW6vYiSdkj1VmWGDe6PiGwdA2d-UNzdtlKYpgrekkSw5zoRmZJg4_XwQ1w9HzAqRoMwIPAmfgz6VpOQyAPwiT91nCO1?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-2.png'" />
        <img src="https://images.openai.com/static-rsc-4/rliRFYba1u0tGOf21MLRohFlgndCVkFGletGHmc18_xXz77EjNTxO3HizEBAu-irsfaRjg5GvmSv-280dHM0QWXq4N2EGBHyWsF5q9tvnKJ5ANJ4tMqI5wo2Y7odwBL0cAYxxUqXJW6-9AGAD1DoStttUbisAPxQjOfF4NhgE8p2DZWUO-KzmBj3hlMUi5Up?purpose=fullsize" class="w-full h-40 object-cover rounded-xl border border-white/10" onerror="this.src='/space-bg-3.png'" />
      </div>

      <div class="bg-black/30 p-6 rounded-2xl border border-yellow-500/30">
        <ul class="list-disc pl-5 text-gray-300 space-y-1 mb-4">
          <li><strong>Launched:</strong> 2021</li>
          <li><strong>Type:</strong> Infrared space telescope</li>
          <li><strong>Primary role:</strong> Exoplanet atmosphere analysis</li>
        </ul>
        <p class="text-gray-300">Infrared light can pass through dust clouds, reveal heat signatures, and detect molecules. JWST represents a shift from "Finding planets" to "Studying planets in detail".</p>
      </div>
    </section>

    <!-- 9.6 - 9.12 -->
    <section>
      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-green-500 pl-4">9.6 Ground-Based Telescopes & 9.7 Direct Imaging</h2>
      <p class="text-gray-300 mb-4">Ground-based observatories like VLT and Keck measure radial velocity and confirm candidates. Future direct imaging missions will use <strong>Coronagraphs</strong> and <strong>Starshades</strong> to block starlight and reveal faint planets directly.</p>

      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-red-500 pl-4">9.8 Future Missions & 9.9 Interstellar Exploration</h2>
      <ul class="list-disc pl-5 text-gray-300 space-y-2 mb-6">
        <li><strong>LUVOIR & HabEx:</strong> Concepts to directly image Earth-like habitable worlds.</li>
        <li><strong>ELT (Extremely Large Telescope):</strong> Ground-based behemoth for imaging and spectroscopy.</li>
        <li><strong>Breakthrough Starshot:</strong> Uses laser-driven light sails to send tiny probes to Proxima Centauri.</li>
      </ul>

      <h2 class="text-2xl font-bold text-white mb-4 border-l-4 border-[#00bfff] pl-4">9.12 The Ultimate Goal</h2>
      <blockquote class="border-l-4 border-purple-500 bg-purple-900/20 p-4 rounded-r-lg text-gray-200 my-4 text-center text-xl">
        To find a planet that shows clear signs of life.
      </blockquote>
      <p class="text-gray-300 text-center">This could include oxygen-rich atmospheres, chemical disequilibrium, surface water, or technosignatures.</p>
    </section>

    <!-- Summary -->
    <section class="bg-[#0a0a1a] p-8 rounded-2xl border border-white/20 mt-12">
      <h2 class="text-2xl font-bold text-white mb-6">Chapter Summary</h2>
      <ul class="list-disc pl-5 space-y-3 text-gray-300 text-sm md:text-base">
        <li>Space missions are essential for detecting and studying exoplanets.</li>
        <li><strong>Kepler</strong> discovered thousands of exoplanets using the transit method.</li>
        <li><strong>TESS</strong> focuses on nearby stars and new planetary candidates.</li>
        <li><strong>JWST</strong> studies atmospheres in detail using infrared light.</li>
        <li>Ground-based telescopes provide confirmation and mass measurements.</li>
        <li>Future missions aim to directly image Earth-like planets using starshades.</li>
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
              <td class="p-2 font-bold text-[#00bfff]">Transit Photometry</td>
              <td class="p-2">Detecting planets via brightness dips</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Infrared Astronomy</td>
              <td class="p-2">Observing heat radiation from objects</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Coronagraph</td>
              <td class="p-2">Device that blocks starlight</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="p-2 font-bold text-[#00bfff]">Starshade</td>
              <td class="p-2">External structure used to block star light</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>
