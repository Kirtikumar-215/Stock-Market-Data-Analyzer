# 📈 Stock Market Data Analyzer

> A FAANG-level NumPy portfolio project for analyzing stock market data using Python and NumPy.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Latest-orange?logo=numpy)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

**Stock Market Data Analyzer** is a Python project that performs financial analysis on stock prices of multiple companies over a one-year period (365 days).

The project demonstrates how NumPy can be used to perform real-world financial computations efficiently using vectorized operations.

This project is ideal for:

- 📊 Data Analytics
- 🐍 Python Practice
- 📈 Financial Data Analysis
- 💼 Portfolio Projects
- 🎯 Technical Interview Preparation

---

## ✨ Features

- 📅 Daily Return Calculation
- 📈 Daily Percentage Return
- 🔄 Compare Any Two Trading Days
- 📉 7-Day Moving Average
- 📉 30-Day Moving Average
- 📉 90-Day Moving Average
- 📊 Highest, Lowest & Average Price
- 📈 Volatility Analysis (`np.std`)
- 🏆 Best Performing Companies
- 💹 Buy / Sell / Hold Signal
- ⚠ Risk Classification
- 💾 Save Portfolio (`np.save`)
- 📦 Compressed Portfolio (`np.savez_compressed`)

---

## 📂 Project Structure

```text
Stock_Market_Data_Analyzer/
│
├── main.py
├── stock_prices.npy
├── companies.npy
├── README.md
```

---

## 📊 Dataset

| Property | Value |
|----------|-------|
| Companies | 10 |
| Trading Days | 365 |
| Data Format | NumPy Array |
| Shape | (365, 10) |

Each row represents one trading day.

Each column represents one company.

---

## 🧠 NumPy Concepts Used

- NumPy Arrays
- Vectorization
- Broadcasting
- Array Indexing
- Array Slicing
- Aggregation Functions
- `np.mean()`
- `np.std()`
- `np.max()`
- `np.min()`
- `np.where()`
- `np.argsort()`
- `np.save()`
- `np.savez_compressed()`

---

## 📋 Features Explained

### 📅 Daily Return

Calculates today's stock price difference compared to yesterday.

---

### 📈 Percentage Return

Calculates daily percentage gain/loss using

```python
((today - yesterday) / yesterday) * 100
```

---

### 📉 Moving Average

Supports

- 7-Day
- 30-Day
- 90-Day

moving averages for trend analysis.

---

### 📊 Price Statistics

Displays

- Highest Price
- Lowest Price
- Average Price

for every company.

---

### 📈 Volatility

Calculates yearly stock volatility using

```python
np.std()
```

---

### 🏆 Best Performing Company

Ranks companies based on yearly percentage return using

```python
np.argsort()
```

---

### 💹 Buy / Sell Signal

Trading signals are generated based on the 30-Day Moving Average.

| Condition | Signal |
|-----------|--------|
| Price < MA30 - 5% | BUY |
| Price > MA30 + 5% | SELL |
| Otherwise | HOLD |

---

### ⚠ Risk Analysis

Companies are classified into:

- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

using yearly volatility.

---

### 💾 Save Portfolio

Supports

- `.npy`
- `.npz`

compressed file formats.

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/kirtikumar-215/Stock-Market-Data-Analyzer.git
```

### Navigate

```bash
cd Stock-Market-Data-Analyzer
```

### Install Dependencies

```bash
pip install numpy
```

### Run Project

```bash
python main.py
```

---

## 🖥 Sample Menu

```text
=========================================
      STOCK MARKET DATA ANALYZER
=========================================

1. Daily Return
2. Daily Percentage Return
3. Compare Two Days
4. 7-Day Moving Average
5. 30-Day Moving Average
6. 90-Day Moving Average
7. Price Statistics
8. Volatility
9. Best Performing Companies
10. Buy/Sell Signal
11. Risk Analysis
12. Save Portfolio
0. Exit

=========================================
```

---

## 📚 Learning Outcomes

After completing this project, you will understand:

- Financial Data Analysis
- Time-Series Calculations
- NumPy Vectorization
- Statistical Analysis
- Ranking Algorithms
- Conditional Operations
- Efficient Array Programming
- Real-world NumPy Applications

---

## 🔮 Future Improvements

- Read data from CSV files (Pandas)
- Live Stock Market API Integration
- Interactive Graphs using Matplotlib
- Company-wise Search
- Portfolio Performance Dashboard
- Machine Learning Price Prediction
- Streamlit Web Application

---

## 💻 Tech Stack

- Python 3
- NumPy

---

## 👨‍💻 Author

**Kirtikumar Prajapati**

Computer Science & Engineering Student

Learning Python • NumPy • Data Analytics • Machine Learning

---

## ⭐ Show Your Support

If you like this project,

⭐ Star this repository

🍴 Fork this repository

📢 Share it with others

---

## 📄 License

This project is licensed under the **MIT License**.

Feel free to use it for learning, practice, and educational purposes.
