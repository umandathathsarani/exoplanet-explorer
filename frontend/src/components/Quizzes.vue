<script setup>
import { ref } from 'vue'

const quizzes = [
  {
    level: "Level 1: Easy (Basics)",
    color: "green",
    questions: [
      {
        id: 1,
        text: "What is an exoplanet?",
        options: ["A star inside our galaxy", "A planet outside our solar system", "A moon of Jupiter", "A comet"],
        answer: 1, // index of option
        explanation: "Exoplanets are planets that orbit stars other than our Sun."
      },
      {
        id: 2,
        text: "Which method detects exoplanets by observing dips in starlight?",
        options: ["Radial velocity", "Transit method", "Microlensing", "Direct imaging"],
        answer: 1,
        explanation: "It detects tiny dips in a star’s brightness when a planet passes in front of it."
      },
      {
        id: 3,
        text: "What is the main requirement for life as we know it?",
        options: ["Methane", "Oxygen", "Liquid water", "Hydrogen"],
        answer: 2,
        explanation: "All known life on Earth depends on liquid water for chemical reactions."
      },
      {
        id: 4,
        text: "What does a habitable zone mean?",
        options: ["Area with no radiation", "Region where planets are frozen", "Region where liquid water can exist", "Area with no stars"],
        answer: 2,
        explanation: "The habitable zone is the 'Goldilocks zone' where conditions are just right for liquid water."
      },
      {
        id: 5,
        text: "Which telescope discovered thousands of exoplanets?",
        options: ["Hubble", "Kepler Space Telescope", "Voyager", "Spitzer"],
        answer: 1,
        explanation: "Kepler discovered thousands of exoplanets using the transit method."
      }
    ]
  },
  {
    level: "Level 2: Medium (Understanding Concepts)",
    color: "yellow",
    questions: [
      {
        id: 6,
        text: "Why are exoplanets difficult to detect?",
        options: ["They are too hot", "They are too small and dim compared to stars", "They move too fast", "They emit no gravity"],
        answer: 1,
        explanation: "Stars are millions to billions of times brighter than planets, making detection difficult."
      },
      {
        id: 7,
        text: "What causes the 'stellar wobble' in radial velocity method?",
        options: ["Planet explosion", "Star rotation", "Gravitational pull of a planet", "Solar wind"],
        answer: 2,
        explanation: "A planet causes its star to 'wobble' slightly due to gravity."
      },
      {
        id: 8,
        text: "What is a biosignature?",
        options: ["A type of telescope", "A chemical or pattern that may indicate life", "A star type", "A galaxy structure"],
        answer: 1,
        explanation: "Biosignatures are indirect signs of biological activity, like oxygen or methane imbalance."
      },
      {
        id: 9,
        text: "Why is Proxima Centauri b important?",
        options: ["It is the biggest planet", "It is the closest known exoplanet", "It is the hottest planet", "It has rings"],
        answer: 1,
        explanation: "Proxima Centauri b is only about 4.24 light-years away."
      },
      {
        id: 10,
        text: "What is tidal locking?",
        options: ["Planet has rings", "One side always faces the star", "Planet has no orbit", "Two planets collide"],
        answer: 1,
        explanation: "Tidal locking occurs when a planet’s rotation matches its orbit."
      },
      {
        id: 11,
        text: "What is the main limitation of direct imaging?",
        options: ["Planets are too far apart", "Stars are too bright compared to planets", "Planets move too slowly", "Telescopes are too fast"],
        answer: 1,
        explanation: "The star’s light overwhelms the faint reflected light of planets."
      }
    ]
  },
  {
    level: "Level 3: Hard (Deep Understanding)",
    color: "red",
    questions: [
      {
        id: 12,
        text: "Why is oxygen alone NOT a guaranteed biosignature?",
        options: ["It is always artificial", "It can be produced by non-biological processes", "It does not exist on Earth", "It only comes from stars"],
        answer: 1,
        explanation: "Oxygen can form through photochemical reactions, not only life."
      },
      {
        id: 13,
        text: "What makes Hot Jupiters scientifically important?",
        options: ["They are Earth-like", "They are easy to detect and challenge formation theories", "They contain life", "They are very small"],
        answer: 1,
        explanation: "Hot Jupiters were unexpected and helped revise planet formation models."
      },
      {
        id: 14,
        text: "Why is TRAPPIST-1 system important in exoplanet research?",
        options: ["It has only one planet", "It has seven Earth-sized planets", "It has no atmosphere", "It is the closest star system"],
        answer: 1,
        explanation: "TRAPPIST-1 system is unique for having multiple potentially rocky planets."
      },
      {
        id: 15,
        text: "What is atmospheric escape?",
        options: ["Planet disappears", "Atmosphere slowly leaves into space", "Star explodes", "Ocean freezes"],
        answer: 1,
        explanation: "High-energy radiation can strip atmospheric gases away over time."
      },
      {
        id: 16,
        text: "Why do scientists combine transit + radial velocity methods?",
        options: ["To measure color", "To determine both radius and mass", "To increase brightness", "To create images"],
        answer: 1,
        explanation: "Transit gives size; radial velocity gives mass → together give density."
      },
      {
        id: 17,
        text: "What is the biggest risk of false biosignatures?",
        options: ["Wrong telescope", "Misinterpreting non-biological gases as life", "Planet explosion", "Star dying"],
        answer: 1,
        explanation: "Some gases can be produced by geology or chemistry, not biology."
      },
      {
        id: 18,
        text: "Why are red dwarf stars both good and bad for habitability?",
        options: ["They are always stable", "They are long-lived but have strong radiation flares", "They are too bright", "They have no planets"],
        answer: 1,
        explanation: "Red dwarfs live trillions of years but often produce harmful flares."
      },
      {
        id: 19,
        text: "What is the main goal of future exoplanet missions?",
        options: ["To count stars", "To directly image Earth-like planets and detect life", "To travel to Mars", "To measure asteroid sizes"],
        answer: 1,
        explanation: "Future missions aim to find biosignatures and Earth analogs."
      },
      {
        id: 20,
        text: "What would a confirmed technosignature indicate?",
        options: ["Volcano activity", "Presence of intelligent civilization", "Water existence", "Planet formation"],
        answer: 1,
        explanation: "Technosignatures suggest technology, not just biological life."
      }
    ]
  }
]

const bonusChallenges = [
  {
    id: 21,
    question: "Explain why a planet in the habitable zone might still be uninhabitable.",
    answer: "Even in the habitable zone, a planet may be uninhabitable due to: no atmosphere or very thin atmosphere, toxic gases (e.g., CO2-dominated like Venus), strong stellar radiation, no magnetic field leading to atmosphere loss, lack of water, or extreme climate instability. Habitability depends on many factors, not just distance from the star."
  },
  {
    id: 22,
    question: "If oxygen and methane are found together in an exoplanet atmosphere, why is this significant?",
    answer: "Oxygen and methane react quickly and destroy each other in a natural environment. If both are found together in large amounts, something must constantly replenish them. This could indicate biological activity. On Earth, this imbalance is maintained by life."
  },
  {
    id: 23,
    question: "Why is direct imaging of Earth-like exoplanets much harder than detecting gas giants?",
    answer: "Earth-like planets are very small, reflect very little light, and are extremely close to bright stars. The star's brightness overwhelms the planet's light. Gas giants are easier because they are larger, brighter, and often orbit further out."
  },
  {
    id: 24,
    question: "How does atmospheric composition influence planetary climate stability?",
    answer: "Atmospheres trap heat (greenhouse effect), distribute energy via winds, protect from radiation, and maintain pressure for liquid water. Without a stable atmosphere, the climate becomes extreme and unstable."
  },
  {
    id: 25,
    question: "If you were designing a future telescope, what 2 features would you prioritize for detecting life and why?",
    answer: "1. High-contrast imaging (like using a starshade or coronagraph) to block star light and directly see Earth-like planets. \n2. High-resolution spectroscopy to detect biosignatures like oxygen, methane, and water. These two together allow both detection and chemical analysis."
  }
]

const userAnswers = ref({})
const showExplanations = ref({})
const showBonusExplanations = ref({})

const selectAnswer = (questionId, optionIndex) => {
  if (showExplanations.value[questionId]) return; // Don't allow changing answer after revealing
  userAnswers.value[questionId] = optionIndex
}

const revealAnswer = (questionId) => {
  if (userAnswers.value[questionId] !== undefined) {
    showExplanations.value[questionId] = true
  }
}

const toggleBonus = (id) => {
  showBonusExplanations.value[id] = !showBonusExplanations.value[id]
}

const getOptionClass = (q, optionIndex) => {
  const isSelected = userAnswers.value[q.id] === optionIndex
  const isRevealed = showExplanations.value[q.id]
  const isCorrect = q.answer === optionIndex

  if (!isRevealed) {
    return isSelected 
      ? 'border-[#00bfff] bg-[#00bfff]/20 text-white' 
      : 'border-white/10 hover:border-white/30 text-gray-300 bg-white/5 cursor-pointer'
  }

  if (isCorrect) {
    return 'border-green-500 bg-green-500/20 text-white shadow-[0_0_15px_rgba(34,197,94,0.3)]'
  }
  
  if (isSelected && !isCorrect) {
    return 'border-red-500 bg-red-500/20 text-gray-300 line-through opacity-70'
  }

  return 'border-white/5 bg-white/5 text-gray-500 opacity-50'
}
</script>

<template>
  <div class="max-w-4xl mx-auto py-8">
    
    <div class="text-center mb-16">
      <h1 class="text-4xl md:text-5xl font-extrabold text-white tracking-tight mb-4">Exoplanet Quizzes</h1>
      <p class="text-xl text-gray-400">Test your knowledge from all 10 chapters!</p>
    </div>

    <!-- Levels -->
    <div class="space-y-16">
      <section v-for="section in quizzes" :key="section.level">
        
        <h2 class="text-3xl font-bold mb-8 flex items-center gap-3" 
            :class="{
              'text-green-400': section.color === 'green',
              'text-yellow-400': section.color === 'yellow',
              'text-red-400': section.color === 'red'
            }">
          <div class="w-3 h-8 rounded-full"
               :class="{
                 'bg-green-500': section.color === 'green',
                 'bg-yellow-500': section.color === 'yellow',
                 'bg-red-500': section.color === 'red'
               }"></div>
          {{ section.level }}
        </h2>

        <div class="space-y-8">
          <div v-for="(q, idx) in section.questions" :key="q.id" class="bg-black/40 border border-white/10 p-6 rounded-2xl shadow-xl">
            <h3 class="text-xl text-white font-semibold mb-6">
              <span class="text-gray-500 mr-2">{{ q.id }}.</span> {{ q.text }}
            </h3>
            
            <div class="grid md:grid-cols-2 gap-4 mb-6">
              <div 
                v-for="(opt, oIdx) in q.options" 
                :key="oIdx"
                @click="selectAnswer(q.id, oIdx)"
                class="p-4 rounded-xl border transition-all duration-300"
                :class="getOptionClass(q, oIdx)"
              >
                <span class="font-bold mr-2 text-sm" :class="userAnswers.value?.[q.id] === oIdx ? 'text-white' : 'text-gray-500'">{{ String.fromCharCode(65 + oIdx) }})</span>
                {{ opt }}
              </div>
            </div>

            <div class="flex justify-between items-center">
              <button 
                @click="revealAnswer(q.id)"
                :disabled="userAnswers[q.id] === undefined || showExplanations[q.id]"
                class="px-6 py-2 rounded-full font-bold text-sm transition-all"
                :class="userAnswers[q.id] === undefined 
                  ? 'bg-gray-800 text-gray-500 cursor-not-allowed' 
                  : showExplanations[q.id] ? 'bg-transparent text-gray-400' : 'bg-[#00bfff] text-black hover:bg-[#0099cc] shadow-[0_0_15px_rgba(0,191,255,0.4)]'"
              >
                {{ showExplanations[q.id] ? 'Answer Revealed' : 'Check Answer' }}
              </button>
            </div>

            <!-- Explanation -->
            <div v-if="showExplanations[q.id]" class="mt-6 p-4 rounded-xl border"
                 :class="userAnswers[q.id] === q.answer ? 'bg-green-900/20 border-green-500/30' : 'bg-red-900/20 border-red-500/30'">
              <p class="text-sm">
                <strong :class="userAnswers[q.id] === q.answer ? 'text-green-400' : 'text-red-400'">
                  {{ userAnswers[q.id] === q.answer ? 'Correct!' : 'Incorrect.' }}
                </strong>
                <span class="text-gray-300 ml-2">{{ q.explanation }}</span>
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Bonus Challenge -->
      <section>
        <h2 class="text-3xl font-bold mb-8 flex items-center gap-3 text-purple-400">
          <div class="w-3 h-8 rounded-full bg-purple-500 shadow-[0_0_15px_rgba(168,85,247,0.5)]"></div>
          🧠 Bonus Challenge (Very Hard)
        </h2>
        
        <div class="space-y-6">
          <div v-for="b in bonusChallenges" :key="b.id" class="bg-gradient-to-r from-purple-900/20 to-black border border-purple-500/20 p-6 rounded-2xl">
            <h3 class="text-lg text-white font-semibold mb-4">
              <span class="text-purple-400 mr-2">{{ b.id }}.</span> {{ b.question }}
            </h3>
            
            <button 
              @click="toggleBonus(b.id)"
              class="text-sm font-bold text-purple-400 hover:text-purple-300 transition-colors"
            >
              {{ showBonusExplanations[b.id] ? 'Hide Answer' : 'Reveal Answer' }}
            </button>

            <div v-if="showBonusExplanations[b.id]" class="mt-4 p-4 bg-black/40 rounded-xl border border-purple-500/30 text-gray-300 text-sm whitespace-pre-line">
              {{ b.answer }}
            </div>
          </div>
        </div>
      </section>

    </div>

  </div>
</template>
