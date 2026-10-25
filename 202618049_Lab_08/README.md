DS605 Fundamentals of Machine Learning

Name: Twinkle Chauhan

Student ID: 202618049

Lab 08: Decision Trees and Support Vector Machines (SVM

Dataset: UCI Banknote Authentication Dataset

---

## 1. Overview

This lab explores Decision Tree and Support Vector Machine (SVM) classification algorithms using the Banknote Authentication dataset.

The main objective is to understand how these algorithms work, implement selected algorithms from scratch using NumPy, visualize decision boundaries, explore nonlinear SVM kernels, and compare model performance using Scikit-learn.

The experiment progresses from two-feature classification and decision-boundary visualization to final model evaluation using all four dataset features.

## 2. Dataset

The Banknote Authentication dataset contains **1,372 samples**, four numerical input features, and one binary target variable.

### Features

| Feature | Description |
|---|---|
| `variance` | Variance of the Wavelet Transformed image |
| `skewness` | Skewness of the Wavelet Transformed image |
| `curtosis` | Curtosis of the Wavelet Transformed image |
| `entropy` | Entropy of the image |
| `class` | Target class: 0 or 1 |

The dataset is used to classify banknotes based on statistical features extracted from images.

**Dataset source:** [UCI Machine Learning Repository – Banknote Authentication](https://archive.ics.uci.edu/dataset/267/banknote+authentication)

## 3. Objectives

- Understand the working principles of Decision Trees and SVMs.
- Implement a Decision Tree from scratch using NumPy.
- Implement a soft-margin Linear SVM from scratch using NumPy.
- Visualize two-feature decision boundaries.
- Compare Gini impurity and entropy for Decision Tree splitting.
- Study the effect of tree depth and SVM hyperparameters.
- Compare linear, polynomial, and RBF SVM kernels.
- Evaluate five final models using all four features.
- Compare classification metrics, training time, and prediction time.

## 4. Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Google Colab

## 5. Implementation and Workflow

### Part A: Decision Tree from Scratch

A Decision Tree classifier is implemented without using Scikit-learn for model training.

The implementation includes:
- Gini impurity calculation.
- Entropy calculation.
- Best split selection.
- Recursive tree construction.
- Prediction using the constructed tree.
- Decision-boundary visualization using two features.
- Comparison with Scikit-learn's Decision Tree classifier.

Different splitting criteria and tree depths are explored to understand their effect on classification performance.

### Part B: Linear SVM from Scratch

A soft-margin Linear SVM is implemented using NumPy.

The implementation includes:
- Feature standardization.
- Binary label mapping from `0/1` to `-1/+1`.
- Hinge-loss-based optimization using subgradient descent.
- Prediction using the learned weight vector and bias.
- Visualization of the decision boundary and margins.
- Identification of margin-violating samples.
- Comparison with Scikit-learn's Linear SVM.
- Experiments with different values of `C`, learning rate, and iteration count.

### Part C: Kernel SVM

A nonlinear two-dimensional dataset is generated using `make_moons`.

Three SVM models are trained and compared:

1. **Linear SVM:** Uses a linear decision boundary.
2. **Polynomial SVM:** Uses a polynomial kernel to model nonlinear relationships.
3. **RBF SVM:** Uses a Radial Basis Function kernel to learn flexible nonlinear boundaries.

Decision-boundary plots and classification metrics are used to study the differences between these kernels.

### Part D: Final Four-Feature Comparison

The original Banknote Authentication dataset is used with all four input features:

- `variance`
- `skewness`
- `curtosis`
- `entropy`

The following five models are compared:

1. Manual Decision Tree
2. Scikit-learn Decision Tree
3. Manual Linear SVM
4. Scikit-learn Linear SVM
5. RBF SVM

All models use the same stratified 80:20 train-test split with `random_state=42` for a consistent comparison.

The SVM models use feature scaling fitted on the training data only.

## 6. Evaluation Metrics

The models are evaluated using the following metrics:

| Metric | Purpose |
|---|---|
| Accuracy | Measures the overall proportion of correct predictions. |
| Precision | Measures the proportion of predicted positive cases that are actually positive. |
| Recall | Measures the proportion of actual positive cases correctly identified. |
| F1-score | Represents the harmonic mean of precision and recall. |
| Training Time | Measures the time required to train the model. |
| Prediction Time | Measures the time required to predict the test samples. |

The results are presented in a comparison table and visualized using performance graphs.

## 7. Key Observations

The experiment helps demonstrate the following:

- Decision Trees are interpretable because their predictions can be explained through feature-based rules.
- Limiting tree depth can help control overfitting.
- Linear SVMs learn linear decision boundaries.
- Feature scaling is important for SVM models.
- Polynomial and RBF kernels can model nonlinear decision boundaries.
- Manual implementations help explain the internal working of classification algorithms.
- Scikit-learn provides optimized implementations that can be compared with the manual models.
- Model selection should consider classification performance, computational time, interpretability, and the risk of overfitting.

The best-performing model should be identified from the actual test results generated by the notebook.

## 8. Conclusion

This lab provides practical experience with Decision Trees and Support Vector Machines, from implementing algorithms from scratch to evaluating Scikit-learn models.

The experiment demonstrates how feature selection, scaling, model complexity, hyperparameters, and kernel choice affect classification performance. It also highlights the trade-offs between predictive performance, computational cost, and interpretability.

---
