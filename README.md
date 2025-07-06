<h1 align="center">🎧 Spotify Data Analysis</h1>

<p align="center">
Unlocking insights from personal Spotify listening history using Python, Data Analysis, and Visualization techniques.
</p>

---

## 📌 Overview

This project analyzes personal Spotify data to reveal music preferences, listening habits, and search patterns. Using Python and visualization libraries, it transforms raw data into actionable insights and visually engaging reports — perfect for showcasing analytical skills.

---

## 📂 Project Structure

```
spotify-data-analysis/
├── data/           # Raw Spotify data files (.json) extracted from your account
├── notebooks/      # Colab or Jupyter notebooks for analysis and exploration
├── src/            # Reusable Python scripts for data handling and visualization
├── outputs/        # Saved charts, plots, and generated visual assets
├── requirements.txt  # List of required Python dependencies
└── README.md       # Project overview and documentation
```

---

## 🚀 Key Features

✅ Visualize your top artists, tracks, and playlists
✅ Generate heatmaps of listening activity by hour and day
✅ Analyze playlist composition (tracks & artists breakdown)
✅ Create WordClouds from most played artists
✅ Explore search history trends over time
✅ Modular codebase for easy reuse and scalability

---

## 🛠️ Getting Started

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Prepare Your Spotify Data

* Visit the [Spotify Privacy Portal](https://www.spotify.com/account/privacy/)
* Request your data export and download the `.zip` file (Spotify may take a few days to prepare)
* Extract the following `.json` files into the `data/` folder:

```
spotify-data-analysis/
├── data/
│   ├── StreamingHistory0.json      # Your listening history
│   ├── Playlist1.json               # Your saved playlists
│   ├── SearchQueries.json           # Your Spotify search history
│   └── ... (other Spotify data files)
```

⚠️ **Important:**

* File names may vary slightly based on your Spotify export — adjust script paths if needed
* Only use your personal data; this project is designed for private, offline analysis
* Do **NOT** share your `.json` data publicly — outputs like charts are safe to share if they don't reveal sensitive info

---

## 📊 Visual Insights Included

✔️ **Top Artists & Tracks** — Bar charts summarizing your most played songs and performers
✔️ **Listening Heatmaps** — Discover peak listening times by hour and day
✔️ **Playlist Summaries** — Analyze track counts and artist diversity in playlists
✔️ **WordClouds** — Visual representation of most listened artists
✔️ **Search Trends** — Track keyword search activity over time

---

## ⚠️ Data Privacy Notice

This project is intended for personal analysis and educational purposes only. Spotify data contains sensitive information — please avoid sharing raw data files publicly. All shared outputs exclude personal identifiers or sensitive fields.

---

## 🌟 Future Enhancements

🔸 Mood and genre-based music insights
🔸 Compare yearly Wrapped statistics
🔸 Interactive dashboards using Streamlit or Plotly
🔸 Long-term trend analysis across multiple years

---

## 👩‍💻 About the Creator

**Pranami Mitra**
Aspiring Data Analyst | Passionate about Music, Data Storytelling, and Visual Analytics

[![GitHub](https://img.shields.io/badge/GitHub-Pranamimitra-181717?style=flat\&logo=github)](https://github.com/Pranamimitra)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Pranami%20Mitra-0A66C2?style=flat\&logo=linkedin)](https://www.linkedin.com/in/pranamimitra/)

---

<h3 align="center">🎧 Ready to Explore Your Listening Trends? Let's turn your music habits into insights!</h3>
