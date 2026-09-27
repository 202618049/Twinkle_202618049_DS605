# DS605 Fundamentals of Machine Learning

Name: Twinkle Chauhan

Student ID: 202618049

Lab 05: Machine Learning with Scikit-learn and From Scratch

Dataset: UCI Garment Worker Productivity Dataset (garments_worker_productivity.csv)

## Project Details

This repository contains a complete machine learning workflow on the
UCI Garment Worker Productivity dataset. It covers data preprocessing,
regression and classification using Scikit-learn, manual implementation
of the same models using NumPy and Pandas, model performance evaluation,
execution time comparison, and optimization of the from-scratch models.

## TASKS COMPLETED

🔹 Part A: Machine Learning with Scikit-learn

Data Loading & Inspection: Loaded the Garment Worker Productivity
dataset and inspected its dimensions, feature types, summary
statistics, and missing values.

Target Preparation: Used actual_productivity as the target variable
for regression. For classification, created a binary MeetsTarget
variable where:

MeetsTarget = 1 if actual_productivity >= targeted_productivity

MeetsTarget = 0 otherwise

Feature Selection: actual_productivity was excluded from the
classification input features to prevent target leakage.

Missing Value Handling: Handled missing numerical values using median
imputation and categorical missing values using the most frequent value.

Categorical Encoding: Applied one-hot encoding to categorical features
including date, quarter, department, day, and team.

Feature Scaling: Standardized numerical features before model training.

Train-Test Split: Used a fixed 80:20 train-test split with
random_state=42. The same train and test samples were reused throughout
the project for a consistent comparison.

Regression Model: Implemented Linear Regression using Scikit-learn.

Classification Model: Implemented Logistic Regression using
Scikit-learn.

Performance Evaluation: Evaluated regression using MAE, RMSE, and R²,
and classification using Accuracy, Precision, Recall, and F1-score.

Training and Prediction Time: Measured model training and prediction
execution times.


🔹 Part B: From-Scratch Machine Learning Implementation

Manual Preprocessing: Reimplemented missing value handling,
categorical encoding, and feature scaling using Pandas and NumPy.

Manual Linear Regression: Implemented Linear Regression using NumPy
matrix operations and the pseudoinverse.

Manual Logistic Regression: Implemented Logistic Regression using
NumPy and gradient descent.

Sigmoid Function: Implemented the sigmoid function manually for
converting model outputs into probabilities.

Parameter Optimization: Updated Logistic Regression parameters
iteratively using gradient descent.

Manual Prediction: Implemented regression predictions and
classification probability/threshold-based predictions manually.

Manual Evaluation Metrics: Implemented MAE, RMSE, R², Accuracy,
Precision, Recall, and F1-score without using Scikit-learn metric
functions.

Same Train-Test Samples: Reused the same train-test split from Part A
to ensure a fair comparison between Scikit-learn and from-scratch
implementations.

Execution Time: Measured training and prediction time for the manual
implementations.


🔹 Part C: Model Comparison & Optimization

Comparison: Compared Scikit-learn and from-scratch implementations
using predictive performance and execution time.

Regression Optimization: Improved the manual Linear Regression
implementation using NumPy's least-squares solver (np.linalg.lstsq).

Logistic Regression Optimization: Tested multiple learning rates
(0.05, 0.10, 0.20, and 0.30) for the manual Logistic Regression.

Early Stopping: Added convergence-based early stopping to reduce
unnecessary gradient descent iterations.

Selected Learning Rate: The final optimized Logistic Regression used
a learning rate of 0.10.

Iteration Reduction: The optimized Logistic Regression converged in
3812 iterations compared with the original 5000 iterations.

Final Performance Comparison: Compared the original manual models,
optimized manual models, and Scikit-learn models using the same
evaluation metrics.


## Model Comparison Table

### Regression

Scikit-learn Linear Regression | MAE: 0.112 | RMSE: 0.151 | R²: 0.145 | Training Time: 0.059 s | Prediction Time: 0.009 s

From-Scratch Linear Regression | MAE: 0.113 | RMSE: 0.151 | R²: 0.138 | Training Time: 0.084 s | Prediction Time: 0.000 s

Optimized From-Scratch Linear Regression | MAE: 0.112 | RMSE: 0.151 | R²: 0.145 | Training Time: 0.022 s | Prediction Time: 0.001 s


### Classification

Scikit-learn Logistic Regression | Accuracy: 0.750 | Precision: 0.775 | Recall: 0.932 | F1-Score: 0.846 | Training Time: 0.059 s | Prediction Time: 0.012 s

From-Scratch Logistic Regression | Accuracy: 0.738 | Precision: 0.779 | Recall: 0.898 | F1-Score: 0.835 | Training Time: 0.666 s | Prediction Time: 0.001 s

Optimized From-Scratch Logistic Regression | Accuracy: 0.742 | Precision: 0.780 | Recall: 0.904 | F1-Score: 0.838 | Training Time: 1.124 s | Prediction Time: 0.000 s


## Final Observations

Regression Performance: The from-scratch Linear Regression produced
results close to the Scikit-learn implementation. The optimized
NumPy implementation achieved R² of 0.145 with a training time of
0.022 seconds.

Regression Optimization: Using NumPy's least-squares solver improved
the manual Linear Regression training time from 0.084 seconds to
0.022 seconds while producing the same reported R² value of 0.145.

Classification Performance: The from-scratch Logistic Regression
produced classification results close to the Scikit-learn model.

Learning Rate Optimization: Testing different learning rates showed
that higher learning rates converged in fewer iterations for this
dataset. A learning rate of 0.10 was selected for the final optimized
implementation.

Early Stopping: The optimized Logistic Regression reduced the number
of iterations from 5000 to 3812.

Classification Optimization: The optimized Logistic Regression
slightly improved Accuracy from 0.738 to 0.742 and F1-score from
0.835 to 0.838.

Training Time: Scikit-learn implementations generally required less
training time because they use highly optimized library-level
implementations. The manual Logistic Regression requires iterative
gradient descent and therefore takes more computation time.

From-Scratch Learning: Implementing the algorithms manually provided
a better understanding of preprocessing, model parameters, sigmoid
activation, gradient descent, prediction, and evaluation metrics.


## Repository Structure

202618049_Lab_05/

├── Lab_05_ML.ipynb                    # Main runnable Colab Notebook

├── garments_worker_productivity.csv   # UCI Garment Worker Productivity Dataset

└── README.md                           # Project details and observations
