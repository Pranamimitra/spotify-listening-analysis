# 🎧 Spotify Listening History Analysis

A data-driven project analyzing personal Spotify listening patterns using Python.

## Features

✅ Analyze top artists, songs, and total listening time  
✅ Identify peak listening hours and patterns over months  
✅ Visualize trends using bar charts, heatmaps, and line plots  
✅ (Optional) Enrich data with Spotify API for genres and recommendations 

## Tech Stack

- Python (Pandas, Matplotlib, Seaborn)
- JSON handling
- Jupyter Notebook
- Optional: Spotify API

## Project Structure

- `data/` - Raw and cleaned Spotify history files
- `notebooks/` - Jupyter notebooks for cleaning, EDA, and visual insights
- `reports/` - Final reports, charts, and presentation-ready material
- `src/` - Reusable Python functions for data cleaning and visualization

## Getting Started

```bash
git clone https://github.com/your-username/spotify-listening-analysis.git
cd spotify-listening-analysis
pip install -r requirements.txt
```

## Example Outputs

- 🎤 **Top Artists Bar Chart**  
  Visualizes your most listened-to artists based on play count.

- 🔥 **Listening Heatmaps**  
  Displays activity by weekday and hour to show peak listening times.

- 🕒 **Time-Based Trend Analysis**  
  Tracks your listening behavior over time (daily, monthly trends).

## Future Work
- Spotify API integration
- Personalized recommendations
- Dashboard with Streamlit
  
---

> *This project is for learning, portfolio enhancement, and demonstration purposes only.*


---

## 📄 `.gitignore`

```text
# Ignore raw and processed data
data/raw/*
data/processed/*
__pycache__/
*.ipynb_checkpoints
