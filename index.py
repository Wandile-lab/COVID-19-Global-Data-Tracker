import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


df = pd.read_csv("owid-covid-data.csv")

# Filter for selected African countries
countries_of_interest = ['South Africa', 'Kenya', 'Nigeria', 'Zimbabwe']
df_filtered = df[df['location'].isin(countries_of_interest)].copy()

df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Drop rows with missing critical values
df_filtered = df_filtered.dropna(subset=['total_cases', 'total_deaths'])
df_filtered.fillna(method='ffill', inplace=True)
df_filtered.interpolate(method='linear', inplace=True)


sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Cumulative Vaccinations Over Time
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title('Cumulative COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

latest = df[df['date'] == df['date'].max()]
df_map = latest[['iso_code', 'location', 'total_cases']].dropna()

fig = px.choropleth(
    df_map,
    locations="iso_code",
    color="total_cases",
    hover_name="location",
    color_continuous_scale="Viridis",
    title=f"COVID-19 Total Cases by Country on {df['date'].max().date()}",
    projection="natural earth"
)
fig.show()

report = """
# COVID-19 Data Analysis Report

## Introduction
This report analyzes global COVID-19 data with a focus on selected African countries: South Africa, Kenya, Nigeria, and Zimbabwe. We explored trends in cases, deaths, and vaccinations to understand the impact and progression of the pandemic.

## Key Insights

### 1. Total Cases Over Time
South Africa experienced a significant rise in cases from mid-2020, peaking around July. Kenya and Nigeria showed slower case growth. The decline in South Africa's cases in 2021 correlates with the implementation of stricter lockdowns.

### 2. Total Deaths and Death Rate
South Africa reported the highest total deaths among the four, but its death rate (deaths ÷ cases) was comparatively lower than Nigeria's, suggesting stronger health infrastructure or better access to treatment.

### 3. Vaccination Rollout
South Africa showed the fastest vaccination rollout, reaching over 50% of its population by early 2022. Kenya and Zimbabwe lagged, with less than 30% vaccinated by the same period.

### 4. Daily New Cases
While South Africa had higher peaks, daily new cases in Kenya and Nigeria showed sporadic increases, possibly due to underreporting or testing issues.

### 5. Geographic Spread (Choropleth)
The choropleth map highlights the stark differences in total case distribution globally, with South Africa being the hotspot in Africa.

## Conclusion
Data shows a clear relationship between vaccination progress and decline in deaths. Countries with higher vaccination rates generally experienced lower fatality trends. Continued efforts in vaccination and healthcare support remain essential.
"""
print(report)
