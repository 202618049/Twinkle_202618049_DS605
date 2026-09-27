# DS605 Lab 05 — Machine Learning with Scikit-learn and From Scratch

## Assignment Overview

This assignment implements regression and classification models using
Scikit-learn and compares them with manually implemented versions
using only NumPy and Pandas.

## Dataset

UCI Garment Worker Productivity Dataset.

The dataset contains productivity-related information about garment
factory workers.

## Models

### Scikit-learn
- Linear Regression
- Logistic Regression

### From Scratch
- Linear Regression using NumPy
- Logistic Regression using gradient descent

## Part A — Scikit-learn

The Scikit-learn models use preprocessing including:
- Missing value handling
- Categorical encoding
- Feature scaling

A fixed 80:20 train-test split with random_state=42 is used.

## Part B — From Scratch

The same train-test samples are used.

The following were implemented manually:
- Missing value handling
- One-hot encoding
- Feature scaling
- Linear Regression
- Logistic Regression
- Sigmoid function
- Gradient descent
- Evaluation metrics

## Part C — Comparison and Optimization

The Scikit-learn and manual implementations are compared using:

### Regression
- MAE
- RMSE
- R²
- Training time
- Prediction time

### Classification
- Accuracy
- Precision
- Recall
- F1-score
- Training time
- Prediction time

An optimization experiment is also performed on the manual
implementation using parameter/convergence tuning.

## Key Observations

- Scikit-learn provides a more optimized and convenient implementation.
- The manually implemented Linear Regression produces results close
  to the Scikit-learn implementation.
- The manually implemented Logistic Regression also produces comparable
  classification results.
- Manual Logistic Regression requires more training time because the
  parameters are optimized iteratively using gradient descent.
- NumPy vectorization helps reduce unnecessary computation in the
  from-scratch implementation.

## Repository Structure

```text
Lab-05-ML-From-Scratch/
├── Lab_05_ML.ipynb
├── README.md
└── garments_worker_productivity.csv
