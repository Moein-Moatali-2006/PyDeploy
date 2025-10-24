# Simple Data Science App - COVID-19 Analysis

This is a simple **Streamlit** web application for analyzing and visualizing **COVID-19 data**, especially focused on **Iran in April 2020**.

---

## 📋 Features

- Upload a **CSV file** containing COVID-19 data.
- View the **first few rows** of your uploaded data.
- Automatically filters and visualizes **New Deaths vs New Cases** in **Iran (April 2020)**.
- Beautiful line chart using **Matplotlib**.

---

## 🧠 About COVID-19

> COVID-19 is a disease caused by the coronavirus. It started in China in December 2019 and spread to almost every country in the world. People can get it when someone coughs, sneezes, or talks, and small drops with the virus go into the air. This app shows COVID-19 information in Iran.

---

## 🧩 Requirements

Create a file named `requirements.txt` and include these lines:

```
streamlit
pandas
matplotlib
```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have **Python 3.8+** installed.
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
5. Upload your `.csv` file and see the visualization!

---

## 📊 Example CSV Columns

Your file should contain at least these columns:

| Date | CountryRegion | New deaths | New cases |
|------|----------------|-------------|------------|
| 2020-04-01 | Iran | 138 | 2987 |
| 2020-04-02 | Iran | 124 | 2875 |
| ... | ... | ... | ... |

---

## 🧠 Author
**Created by:** Moein Moatali  
**Purpose:** Educational project for data science practice and Deploy it.

