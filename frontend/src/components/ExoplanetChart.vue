<script setup>
import { computed } from 'vue'
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  Tooltip,
  Legend
} from 'chart.js'
import { Scatter } from 'vue-chartjs'

ChartJS.register(LinearScale, PointElement, Tooltip, Legend)

const props = defineProps({
  planets: {
    type: Array,
    required: true
  }
})

const chartData = computed(() => {
  return {
    datasets: [
      {
        label: 'Exoplanets',
        backgroundColor: 'rgba(0, 191, 255, 0.6)',
        borderColor: '#00bfff',
        pointBackgroundColor: '#00bfff',
        pointBorderColor: '#00bfff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: '#00bfff',
        pointRadius: 6,
        pointHoverRadius: 9,
        data: props.planets.map(p => ({
          x: p.distance_ly,
          y: p.mass_earth,
          planetName: p.name,
          discoveryMethod: p.discovery_method
        }))
      }
    ]
  }
})

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    x: {
      title: {
        display: true,
        text: 'Distance (Light Years)',
        color: '#aaaaaa',
        font: { size: 14, weight: 'bold' }
      },
      grid: { color: 'rgba(255, 255, 255, 0.05)' },
      ticks: { color: '#aaaaaa' }
    },
    y: {
      title: {
        display: true,
        text: 'Mass (Earth Masses)',
        color: '#aaaaaa',
        font: { size: 14, weight: 'bold' }
      },
      grid: { color: 'rgba(255, 255, 255, 0.05)' },
      ticks: { color: '#aaaaaa' }
    }
  },
  plugins: {
    legend: {
      labels: { color: '#ffffff' }
    },
    tooltip: {
      backgroundColor: 'rgba(15, 23, 42, 0.9)',
      titleColor: '#00bfff',
      bodyColor: '#ffffff',
      borderColor: 'rgba(0, 191, 255, 0.5)',
      borderWidth: 1,
      padding: 12,
      displayColors: false,
      callbacks: {
        title: function(context) {
          return context[0].raw.planetName;
        },
        label: function(context) {
          const point = context.raw;
          return [
            `Method: ${point.discoveryMethod}`,
            `Distance: ${point.x} LY`,
            `Mass: ${point.y} M⊕`
          ];
        }
      }
    }
  }
}
</script>

<template>
  <div class="h-[400px] w-full bg-black/60 backdrop-blur-xl rounded-2xl border border-white/20 p-4 shadow-2xl relative overflow-hidden group hover:border-[#00bfff]/50 transition-colors">
    <div class="absolute top-0 right-0 w-32 h-32 bg-[#00bfff]/10 rounded-bl-full blur-2xl group-hover:bg-[#00bfff]/20 transition-colors pointer-events-none"></div>
    <Scatter v-if="props.planets.length > 0" :data="chartData" :options="chartOptions" class="relative z-10" />
    <div v-else class="h-full flex items-center justify-center text-gray-500 font-mono relative z-10">
      Awaiting valid telemetry data...
    </div>
  </div>
</template>
