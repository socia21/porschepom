const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from the 'public' folder (or root if you prefer)
app.use(express.static(path.join(__dirname, 'public')));

// Optional API endpoint to serve chart data (so frontend can fetch dynamically)
app.get('/api/data', (req, res) => {
  res.json({
    marginVsChina: {
      labels: ['2022', '2023', '2024', '2025', '2026', '2027(P)', '2028(P)'],
      datasets: {
        margin: [18.0, 18.6, 15.0, 12.5, 10.8, 15.5, 18.2],
        chinaDeliveries: [93.3, 79.3, 64.1, 41.9, 33.0, 48.0, 62.0]
      }
    },
    regionalDeliveries: {
      labels: ['N.America', 'Europe', 'China', 'Germany', 'Overseas'],
      '2023': [86.0, 70.2, 79.3, 32.4, 52.2],
      '2026': [76.5, 62.0, 33.0, 28.1, 46.0]
    },
    powertrainMix: {
      labels: ['2022', '2024', '2026 (Strategy)', '2028 (Target)'],
      BEV: [11, 13, 20, 35],
      PHEV: [15, 19, 30, 35],
      ICE: [74, 68, 50, 30]
    },
    productionVolume: {
      labels: ['Zuffenhausen', 'Leipzig', 'Other'],
      '2025': [82, 94, 28],
      '2026': [68, 85, 22]
    },
    qualityMetrics: {
      labels: ['Q1', 'Q2', 'Q3', 'Q4'],
      defectRate: [120, 95, 78, 65],
      complaints: [42, 38, 29, 21]
    },
    regionalMix: {
      labels: ['N.America', 'Europe', 'China', 'Germany', 'Overseas'],
      values: [30, 28, 18, 14, 10]
    }
  });
});

// Fallback: serve index.html for any unmatched routes (SPA mode)
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});