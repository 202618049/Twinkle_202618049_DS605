DS605 Fundamentals of Machine Learning

Name: Twinkle Chauhan

Student ID: 202618049

Lab 03: Scikit-learn Data Preprocessing & Model Evaluation


Date: 21 August 2026
Dataset: Hotel Bookings Dataset (hotel_bookings.csv)

Project Details

This repository contains a complete Scikit-learn machine learning workflow on the Hotel Bookings dataset. It covers data cleaning, missing value imputation, outlier detection, data leakage prevention, modular preprocessing pipelines (ColumnTransformer), and model performance evaluation comparing Logistic Regression and Decision Tree classifiers.



TASKS COMPLETED

🔹 Part A: Data Loading & Preprocessing with Scikit-learn

Data Inspection & Exploration: Inspected dataset dimensions, feature data types, summary statistics, and target class distribution (is_canceled).

Missing Value Analysis & Removal: Identified missing value percentages and dropped the company column due to excessive missingness (>94%).

Data Leakage Prevention: Removed features (reservation_status, reservation_status_date) that directly reveal the final outcome.

Outlier Removal: Visualized feature distributions using boxplots (adr, lead_time) and filtered extreme outliers using the 1.5 * IQR method on adr (removed 3,793 rows).

Preprocessing Pipelines: Built modular ColumnTransformer pipelines fitted strictly on training data (train_test_split, test_size=0.2, stratify=y):

Pipeline A: KNNImputer(n_neighbors=5) + StandardScaler for numerical features; SimpleImputer + OneHotEncoder for categorical features.

Pipeline B: KNNImputer(n_neighbors=5) + MinMaxScaler for numerical features; SimpleImputer + OneHotEncoder for categorical features.

🔹 Part B: Model Training & Performance Evaluation

Model Training: Trained four total model-pipeline combinations using LogisticRegression(max_iter=1000) and DecisionTreeClassifier(random_state=42).

Performance Evaluation: Evaluated all models on Train/Test Accuracy, Precision, Recall, and F1-score, and generated side-by-side Confusion Matrices.

Overfitting & Scaling Analysis: Analyzed performance gaps between training and testing scores and evaluated the impact of feature scaling.

Model Comparison Table

Logistic Regression (Pipeline A - StandardScaler) | Train Acc: 0.8213 | Test Acc: 0.8164 | Precision: 0.8085 | Recall: 0.6599 | F1-Score: 0.7267

Logistic Regression (Pipeline B - MinMaxScaler) | Train Acc: 0.8168 | Test Acc: 0.8126 | Precision: 0.8055 | Recall: 0.6505 | F1-Score: 0.7197

Decision Tree (Pipeline A - StandardScaler) | Train Acc: 0.9960 | Test Acc: 0.8663 | Precision: 0.8148 | Recall: 0.8263 | F1-Score: 0.8205

Decision Tree (Pipeline B - MinMaxScaler) | Train Acc: 0.9960 | Test Acc: 0.8665 | Precision: 0.8151 | Recall: 0.8266 | F1-Score: 0.8208

Final Observations

Best Overall Model: The Decision Tree models achieved the highest overall test accuracy (~86.6%) and F1-score (~82.1%).

Impact on Logistic Regression: StandardScaler (Pipeline A) yielded slightly better accuracy and stability compared to MinMaxScaler (Pipeline B) due to improved optimization convergence.

Impact on Decision Trees: Feature scaling made virtually no difference for Decision Trees because tree-based algorithms split nodes based on order/thresholds rather than spatial distances.

Overfitting Analysis: Logistic Regression showed high generalization with minimal train-test accuracy gap (~0.5%), whereas Decision Trees exhibited clear overfitting with ~99.6% train accuracy vs ~86.6% test accuracy.

Repository Structure

202618049_Lab_03/
├── 202618049_Lab03.ipynb       # Main runnable Colab Notebook
├── hotel_bookings.csv          # Original Hotel Bookings Dataset
├── cleaned_hotel_bookings.csv  # Preprocessed Base Dataset
└── README.md                   # Project details and observations
