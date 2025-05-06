# COVID-19-Global-Data-Tracker

This project is a data analysis and visualization tool that explores global trends in COVID-19 cases, deaths, and vaccinations, with a special focus on selected African countries. The analysis is conducted using Python, pandas, seaborn, matplotlib, and Plotly.

## 📊 Project Summary

The goal of this project is to analyze real-world COVID-19 data from [Our World in Data](https://ourworldindata.org/covid-data) to generate insights and visualize the impact of the pandemic across different countries over time. It highlights trends in total cases, deaths, vaccinations, and compares metrics across selected African countries.

## 🌍 Countries of Focus

- South Africa  
- Kenya  
- Nigeria  
- Zimbabwe  

## ✅ Features & Objectives

- ✅ Import and clean a real-world COVID-19 dataset.
- ✅ Analyze time-series trends for cases, deaths, and vaccinations.
- ✅ Compare metrics across selected countries.
- ✅ Visualize data using line charts and a global choropleth map.
- ✅ Present findings in a readable and sharable format.

## 📁 Dataset

- Source: [Our World in Data - owid-covid-data.csv](https://ourworldindata.org/covid-data)
- Format: CSV
- Key columns used:
  - `date`
  - `location`
  - `total_cases`
  - `total_deaths`
  - `total_vaccinations`
  - `iso_code`

## 🧪 Tools & Libraries Used

- `pandas` — Data manipulation  
- `matplotlib` & `seaborn` — Data visualization  
- `plotly.express` — Interactive choropleth map  
- `Jupyter Notebook` or `VS Code` — Development environment  

## 📈 Visualizations Included

- Total COVID-19 cases over time (line chart)
- Cumulative vaccinations over time (line chart)
- Interactive world map showing total cases by country (choropleth)

## 🔍 Key Insights

1. **South Africa** showed the highest total cases and vaccinations among the selected countries.
2. **Nigeria** had a lower total case count but a higher death rate relative to cases.
3. Vaccination rollouts varied significantly, with South Africa leading and Zimbabwe lagging.
4. Daily new cases showed erratic spikes in Kenya and Nigeria, likely due to reporting inconsistencies.

## 📌 How to Run

1. Clone this repository or download the `.ipynb` file.
2. Ensure you have Python 3.x and the required libraries:
   ```bash
   pip install pandas matplotlib seaborn plotly
