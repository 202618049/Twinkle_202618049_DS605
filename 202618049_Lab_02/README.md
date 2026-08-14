# Twinkle_202618049_DS605
DS605 Fundamentals of Machine Learning

Name: Twinkle Chauhan

Student ID: 202618049

# Lab 02: Data Analysis & Manipulation with NumPy and Pandas

Date: 14,August'2026

* **Dataset:** Titanic Dataset (`train.csv`)

## Project Details

This repository contains a complete exploratory data analysis (EDA) and data preprocessing workflow on the Titanic dataset using Python libraries (**NumPy**, **Pandas**, **Matplotlib**, and **Seaborn**).

# TASKS COMPLETED

## 🔹 Part A: NumPy Fundamentals
* **Array Operations:** Array creation, matrix transformations, reshaping, and indexing.
* **Mathematical & Statistical Analysis:** Array statistics (mean, variance, standard deviation, percentiles), vectorized arithmetic, and linear algebra operations.
* **Random Sampling:** Generating synthetic data following normal distributions and computing confidence intervals.


## 🔹 Part B: Pandas EDA & Preprocessing
* **Data Inspection & Filtering:** Checking dataset dimensions, column data types, missing counts, and applying complex boolean indexing.
* **Group Aggregations:** Grouping data by categorical features (`Sex`, `Pclass`) to analyze survival metrics.
* **Missing Value Imputation:** Evaluating and implementing Mean, Median, Mode, and Random sampling imputation strategies for missing values.
* **Outlier Detection:** Identifying extreme ticket price values (`Fare`) using the Interquartile Range (IQR) technique.
* **Feature Engineering:** Creating composite feature metrics including `FamilySize` (`SibSp + Parch + 1`) and `IsAlone`.
* **Pivot Tables & Visualization:** Generating multi-dimensional pivot tables, correlation heatmaps, survival distribution bar charts, and scatter plots (`Age` vs `Fare`).

---

## Repository Structure
```text
├── 202618049_Lab02.ipynb    # Main runnable Jupyter/Colab Notebook
├── train.csv                # Original Titanic Dataset
├── cleaned_train.csv        # Preprocessed Titanic Dataset
└── README.md                # Project details and observations
