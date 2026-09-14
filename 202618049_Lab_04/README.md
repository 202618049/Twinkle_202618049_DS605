# DS605: Fundamentals of Machine Learning

**Name:** Twinkle Chauhan  
**Student ID:** 202618049  

**Lab Assignment - 4: End-to-End Machine Learning Project**

**Project:** Airbnb Price Prediction

**Dataset:** Kaggle New York City Airbnb Open Data (`AB_NYC_2019.csv`)

---
# 🏠 StayPredict AI

### Smart Airbnb Price Intelligence using Machine Learning

🌐 **Live Demo:** https://YOUR-STREAMLIT-LINK.streamlit.app/


## Project Details

This project implements an end-to-end machine learning workflow for predicting Airbnb nightly prices using the New York City Airbnb dataset.

The project covers data analysis, cleaning, preprocessing, feature engineering, feature selection, regression model comparison, hyperparameter tuning, model evaluation, and a Streamlit web application for price prediction.

---

## TASKS COMPLETED

### 🔹 Task 1: Data Analysis and Preparation

- Analyzed the New York City Airbnb dataset.
- Original dataset contained **48,895 records and 16 columns**.
- Cleaned the dataset and obtained **45,912 records and 14 columns**.
- Handled missing values using appropriate preprocessing techniques.
- Selected **11 relevant features** for prediction.
- Performed feature engineering by creating the `host_activity` feature.
- Applied preprocessing using numerical imputation and categorical encoding.
- Split the data into training and testing sets.
- Analyzed important features that may influence Airbnb prices.

### 🔹 Task 2: Model Training and Evaluation

Three regression models were trained and compared:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Models were evaluated using:

- MAE
- MSE
- RMSE
- R² Score

Random Forest achieved the best initial performance and was selected for hyperparameter tuning using `RandomizedSearchCV`.

The final preprocessing workflow and trained model were saved as:

`airbnb_price_pipeline.pkl`

---

## Model Comparison

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 34.101 | 46.456 | 0.523 |
| Random Forest | 31.710 | 43.838 | 0.576 |
| Gradient Boosting | 32.471 | 44.549 | 0.562 |

### 🏆 Best Model

**Random Forest Regressor**

It achieved the lowest MAE and RMSE and the highest R² score among the three models.

---

## Final Model Performance

**Final Model:** Tuned Random Forest Regressor

| Metric | Result |
|---|---:|
| MAE | 31.674 |
| MSE | 1914.195 |
| RMSE | 43.752 |
| R² Score | 0.577 |
| Training R² | 0.643 |
| Testing R² | 0.577 |

The training and testing R² difference was **0.066**, indicating no major overfitting or underfitting.

---

### 🔹 Task 3: Streamlit Application

A Streamlit application named **StayPredict AI** was developed.

The application accepts relevant Airbnb listing information such as:

- Neighbourhood Group
- Neighbourhood
- Latitude
- Longitude
- Room Type
- Minimum Nights
- Number of Reviews
- Reviews per Month
- Host Listings Count
- Availability per Year

The application uses the saved machine learning pipeline to generate an estimated Airbnb nightly price.


---

### 🔹 Task 4: Final Project Summary

The project successfully demonstrates an end-to-end machine learning workflow for Airbnb price prediction.

The final tuned Random Forest model achieved:

- **MAE:** 31.674
- **RMSE:** 43.752
- **R²:** 0.577

The trained model was integrated into a Streamlit application that allows users to enter Airbnb listing information and receive an estimated nightly price.

---

## Important Limitations

- The model was trained using historical NYC Airbnb data.
- The model explains approximately **57.7%** of the variation in Airbnb prices.
- Important factors such as amenities, property size, ratings, photographs, seasonal demand, and special events are not included.
- The model is specific to the New York City Airbnb dataset.
- Predicted prices are estimates and may differ from actual market prices.

---

## Repository Structure

```text
202618049_Lab_04/

├── Airbnb_Price_Prediction.ipynb    # Main Jupyter Notebook
├── app.py                           # Streamlit Application
├── airbnb_price_pipeline.pkl        # Saved ML Pipeline
├── requirements.txt                 # Required Libraries
├── AB_NYC_2019.csv                  # Airbnb Dataset
└── README.md                        # Project Documentation
