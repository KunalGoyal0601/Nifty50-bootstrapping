# Confidence Intervals by Bootstrapping: NIFTY 50

A statistical analysis of **NIFTY 50 market returns and risk measures using bootstrap resampling**.

This project investigates how different bootstrap confidence-interval methods behave when applied to financial return data. Multiple bootstrap approaches are implemented and compared with classical statistical confidence intervals for **mean daily return, annualized volatility, and Sharpe Ratio**.

> **Academic Project** — Advanced Statistical Methods and Stochastic Process
> Central University of Rajasthan

---

## 📌 Overview

Financial market returns are noisy and frequently deviate from the assumptions underlying classical statistical methods.

A point estimate such as an average return or volatility does not describe the uncertainty associated with that estimate. **Confidence intervals** provide a range of plausible values for the underlying population parameter.

This project uses **bootstrap resampling** to empirically estimate the sampling distribution of financial statistics and construct confidence intervals without relying entirely on strong parametric assumptions.

The analysis focuses on:

* Mean daily log return
* Annualized volatility
* Sharpe Ratio
* Bootstrap sampling distributions
* Confidence-interval width
* Classical vs. bootstrap confidence intervals
* Uncertainty in financial risk measures

---

## 🎯 Objectives

The main objectives of this project are to:

* Understand the statistical foundations of bootstrap resampling.
* Apply bootstrap methods to real financial market data.
* Construct confidence intervals for financial statistics.
* Compare multiple bootstrap confidence-interval techniques.
* Compare bootstrap intervals with classical statistical intervals.
* Investigate how skewness affects confidence-interval estimation.
* Quantify uncertainty in return and volatility estimates.
* Demonstrate practical applications of bootstrap confidence intervals in financial analysis.

---

## 📊 Dataset

The analysis uses historical **NIFTY 50 Index** data obtained from **Yahoo Finance**.

### Dataset Information

| Property            | Description                    |
| ------------------- | ------------------------------ |
| Market              | NIFTY 50                       |
| Frequency           | Daily                          |
| Data Source         | Yahoo Finance                  |
| Period              | January 2018 – June 2026       |
| Observations        | Daily trading data             |
| Variables           | Open, High, Low, Close, Volume |
| Main price variable | Close                          |
| Derived variable    | Daily log return               |

The raw dataset is cleaned, converted to appropriate numerical and datetime formats, sorted chronologically, and then used to calculate log returns.

---

## 🔄 Analysis Pipeline

```text
NIFTY 50 Historical Data
          │
          ▼
    Data Cleaning
          │
          ▼
   Data Preprocessing
          │
          ▼
     Close Prices
          │
          ▼
      Log Returns
          │
          ▼
 Descriptive Statistics
          │
          ▼
 Bootstrap Resampling
          │
          ├───────────────┐
          ▼               ▼
   Return Analysis   Risk Analysis
          │               │
          ▼               ▼
   Mean Return       Volatility
          │               │
          └───────┬───────┘
                  ▼
        Confidence Intervals
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
    Classical   Bootstrap   Comparison
       │          │          │
       └──────────┼──────────┘
                  ▼
       Statistical Interpretation
                  │
                  ▼
        Financial Applications
```

---

## 📐 Statistical Methodology

The project implements and compares the following confidence-interval methods.

### Classical Confidence Intervals

Classical statistical intervals are used as a baseline comparison:

* **t-based confidence interval** for mean return
* **Chi-square-based confidence interval** for volatility

These provide a reference against which the bootstrap approaches can be evaluated.

### Bootstrap Confidence Intervals

Five bootstrap methods are implemented:

| Method                                 | Description                                                          |
| -------------------------------------- | -------------------------------------------------------------------- |
| **Normal Bootstrap**                   | Uses the bootstrap standard error and normal approximation           |
| **Percentile**                         | Uses empirical quantiles of the bootstrap distribution               |
| **Bias-Corrected (BC)**                | Adjusts percentile limits for bootstrap bias                         |
| **Bias-Corrected & Accelerated (BCa)** | Corrects for both bias and acceleration/skewness                     |
| **Studentized**                        | Uses a bootstrap pivot and nested resampling to estimate uncertainty |

The **BCa method** uses jackknife resampling to estimate the acceleration parameter.

The **Studentized method** uses a nested bootstrap procedure and is therefore considerably more computationally expensive.

---

## 📈 Financial Statistics

### 1. Log Returns

Daily log returns are calculated from consecutive closing prices:

$$
r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$

where:

* $P_t$ = current NIFTY 50 closing price
* $P_{t-1}$ = previous closing price
* $r_t$ = daily log return

Log returns are used as the primary statistical variable throughout the analysis.

---

### 2. Annualized Volatility

Daily volatility is estimated using the sample standard deviation of log returns.

Annualized volatility is calculated as:

$$
\sigma_{annual} = \sigma_{daily}\sqrt{252}
$$

where 252 represents the approximate number of trading days in a year.

---

### 3. Sharpe Ratio

The project also estimates uncertainty around the annualized Sharpe Ratio.

The implementation uses:

$$
Sharpe =
\frac{\bar{r}-r_f}{\sigma}
\sqrt{252}
$$

where:

* $\bar{r}$ = mean daily return
* $r_f$ = daily risk-free rate
* $\sigma$ = daily return volatility

A bootstrap distribution is generated for the Sharpe Ratio and a **BCa confidence interval** is calculated.

---

## 🔬 Bootstrap Procedure

For each statistic:

1. Start with the observed NIFTY 50 return series.
2. Draw bootstrap samples with replacement.
3. Calculate the statistic for each resampled dataset.
4. Repeat the process across multiple bootstrap iterations.
5. Construct the empirical sampling distribution.
6. Calculate confidence intervals using different methods.
7. Compare interval locations and widths.

The notebook uses a fixed random seed to improve reproducibility.

---

## 📊 Analysis Performed

The project contains several stages of statistical analysis.

### Exploratory Data Analysis

* NIFTY 50 price trend
* Daily return distribution
* Descriptive statistics
* Return skewness
* Excess kurtosis
* Distributional characteristics

### Confidence-Interval Analysis

Confidence intervals are calculated for:

* Mean daily return
* Annualized volatility
* Sharpe Ratio

### Method Comparison

The following approaches are compared:

```text
Classical
   │
   ├── t-based CI
   └── Chi-square CI
            │
            ▼
Bootstrap
   │
   ├── Normal
   ├── Percentile
   ├── Bias-Corrected (BC)
   ├── BCa
   └── Studentized
```

The comparison focuses on:

* Lower confidence limit
* Upper confidence limit
* Interval width
* Differences between methods
* Effect of distributional characteristics

---

## 📉 Visual Analysis

The project generates visualizations including:

* NIFTY 50 price trends
* Return distributions
* Bootstrap sampling distributions
* Confidence-interval comparisons
* Confidence-interval width comparisons
* Sharpe Ratio bootstrap distribution

Example output structure:

```text
outputs/
├── 01_price_trend.png
├── 02_return_distribution.png
├── 03_bootstrap_distributions.png
├── 04_ci_comparison.png
├── 05_ci_width_comparison.png
└── 06_sharpe_ratio_ci.png
```

---

## 💼 Financial Applications

The project demonstrates how statistical uncertainty can be incorporated into financial analysis.

### Risk Estimation

Confidence intervals for volatility can be used to understand uncertainty around estimated market risk.

The project also demonstrates how volatility uncertainty can affect a simple Value-at-Risk calculation.

### Sharpe Ratio Analysis

Bootstrap confidence intervals provide an empirical way to quantify uncertainty around the estimated Sharpe Ratio.

### Market Interpretation

The project includes an illustrative analysis of the confidence interval for mean returns and volatility.

These applications are intended to demonstrate statistical methodology rather than provide investment recommendations.

---

## 🗂️ Project Structure

```text
nifty50-bootstrap-ci/
│
├── bootstrap_nifty50_ci.ipynb
│
├── data/
│   └── NIFTY50_data.csv
│
├── outputs/
│   ├── bootstrap_distributions.png
│   ├── ci_comparison.png
│   ├── ci_width_comparison.png
│   └── sharpe_ratio_ci.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technology Stack

**Programming**

* Python

**Data Analysis**

* NumPy
* Pandas
* SciPy

**Visualization**

* Matplotlib

**Environment**

* Jupyter Notebook
* Git
* GitHub

---

## 🚀 Getting Started

### Prerequisites

Make sure you have:

* Python 3.8+
* pip
* Jupyter Notebook or JupyterLab

### Clone the Repository

```bash
git clone https://github.com/Yashu057/nifty50-bootstrap-ci.git
cd nifty50-bootstrap-ci
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
bootstrap_nifty50_ci.ipynb
```

Run the notebook cells sequentially.

---

## 🔁 Reproducibility

The analysis uses a fixed NumPy random seed:

```python
np.random.seed(42)
```

This helps make the bootstrap results reproducible when the same dataset, parameters, and computational environment are used.

---

## ⚠️ Important Statistical Note

The standard bootstrap procedure implemented in this project resamples individual return observations independently.

Financial returns can exhibit **serial dependence and volatility clustering**. For a more rigorous time-series bootstrap analysis, methods such as:

* Moving Block Bootstrap
* Stationary Bootstrap
* Circular Block Bootstrap

could be investigated.

Therefore, the results should be interpreted as an **academic demonstration of bootstrap confidence-interval methods**, rather than a complete treatment of financial time-series dependence.

---

## 🎓 Academic Context

**Course:** Advanced Statistical Methods and Stochastic Process
**Course Code:** 6.0MBD10
**Department:** Data Science & Analytics
**Institution:** Central University of Rajasthan
**Academic Session:** 2025–26

**Instructor:** Dr. Vidyottama Jain

---

## 👥 Authors

**Yash Verma**
**Kunal Goyal**

M.Sc. Computer Science — Big Data Analytics
Central University of Rajasthan

---

## 📜 License

This project was developed for **academic and educational purposes**.

The code and analysis are provided for learning and research demonstration. Please refer to the repository for the applicable usage terms.

---

## ⚠️ Disclaimer

This project is intended for **educational and statistical analysis purposes only**.

The results should not be interpreted as financial advice, investment recommendations, or a recommendation to buy or sell any security.

---

## ⭐ Project Highlights

```text
✓ Real-world NIFTY 50 financial data
✓ Bootstrap-based statistical inference
✓ Five bootstrap confidence-interval methods
✓ Classical vs. bootstrap comparison
✓ Mean return and volatility analysis
✓ Sharpe Ratio uncertainty estimation
✓ Bootstrap distribution visualization
✓ Financial risk application
✓ Reproducible statistical workflow
✓ Time-series bootstrap limitations discussed
```
