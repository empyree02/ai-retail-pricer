---
title: AI Retail Pricer
emoji: 💰
colorFrom: green
colorTo: blue
sdk: streamlit
app_file: app.py
python_version: 3.10
pinned: false
---

# 💰 AI Retail Pricer

**AI Retail Pricer** is a simple app that suggests a **retail price** based on your **purchase cost** and configurable business parameters like logistics, IT, personnel, and profit margin.

### 🎯 Purpose
Many small businesses struggle to set fair, profitable retail prices. This app provides a transparent and data-driven way to compute a consistent selling price.

### ⚙️ How it works
You enter:
- Purchase cost per item  
- Estimated overheads (logistics, IT, personnel, etc.)  
- Desired profit margin  

The app calculates:
```
Retail Price = Purchase Cost × (1 + Overhead + Margin)
```

### 🧠 Tech
Built using:
- **Python**
- **Streamlit** for the user interface
- **NumPy & Pandas** for calculations

### 🚀 Run locally
```bash
pip install -r requirements.txt
streamlit run app/app.py
```
