# 📊 COVID-19 Data Analysis & Visualization – Week 7

## 📝 Overview

This project involves analyzing and visualizing COVID-19 data using Python. The analysis includes data loading, cleaning, exploratory data analysis (EDA), and visualization to understand the spread and impact of the pandemic across selected countries.

---

## 👣 Steps Followed

### ✅ Step 1: Data Acquisition
- Dataset: `owid-covid-data.csv`
- Source: [Our World in Data – COVID-19 Dataset](https://ourworldindata.org/covid-cases)

### ✅ Step 2: Data Cleaning
- Checked for missing values.
- Converted date columns to datetime objects.
- Removed null or non-country data rows where necessary.

### ✅ Step 3: Country Selection
- Selected countries for comparative analysis:
  - Kenya
  - South Africa
  - Nigeria
  - United States
  - India
  - Brazil

### ✅ Step 4: Exploratory Data Analysis (EDA)
- Used `pandas`, `matplotlib`, and `seaborn` to explore:
  - Total cases over time.
  - Total cases per country on the latest available date.

### ✅ Step 5: Visualizations
- 📈 **Line Plot**: Showing total COVID-19 cases over time for selected countries.
- 📊 **Bar Plot**: Comparing total cases by country on the most recent date.

### ✅ Step 6: Summary of Insights
- The United States had the highest number of total cases among selected countries.
- Emerging economies like India and Brazil also reported significantly high cases.
- Kenya, while lower in total numbers, exhibited a steady rise in cases over time.

---
## 📁 Project Structure

- `covid_global_tracker.ipynb` – Jupyter Notebook containing the full analysis and visualizations.
- `requirements.txt` – List of Python packages required to run the notebook.

---

## 🔧 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
