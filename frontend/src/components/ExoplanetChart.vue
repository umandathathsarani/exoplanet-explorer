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
      grid: { color: '#333333' },
      ticks: { color: '#aaaaaa' }
    },
    y: {
      title: {
        display: true,
        text: 'Mass (Earth Masses)',
        color: '#aaaaaa',
        font: { size: 14, weight: 'bold' }
      },
      grid: { color: '#333333' },
      ticks: { color: '#aaaaaa' }
    }
  },
  plugins: {
    legend: {
      labels: { color: '#ffffff' }
    },
    tooltip: {
      backgroundColor: 'rgba(30, 30, 30, 0.9)',
      titleColor: '#00bfff',
      bodyColor: '#ffffff',
      borderColor: '#00bfff',
      borderWidth: 1,
      padding: 10,
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
  <div class="h-[400px] w-full bg-[#1e1e1e] rounded-xl border border-gray-800 p-4 shadow-2xl relative overflow-hidden group hover:border-gray-600 transition-colors">
    <div class="absolute top-0 right-0 w-32 h-32 bg-[#00bfff]/5 rounded-bl-full group-hover:bg-[#00bfff]/10 transition-colors pointer-events-none"></div>
    <Scatter v-if="props.planets.length > 0" :data="chartData" :options="chartOptions" />
    <div v-else class="h-full flex items-center justify-center text-gray-500 font-mono">
      Awaiting valid telemetry data...
    </div>
  </div>
</template>
