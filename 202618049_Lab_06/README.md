# DS605 Fundamentals of Machine Learning

Name: Twinkle Chauhan

Student ID: 202618049

Lab 06: Feature Extraction and Machine Learning with Image and Text Data

Image Dataset: Asphalt Crack Dataset - 400 Images

Text Dataset: Email Spam Classification Dataset

## Project Details

This repository contains a machine learning workflow for image feature extraction and email spam classification. It covers image preprocessing, numerical feature extraction, Canny edge detection, traditional machine learning models, evaluation, and representation improvement.

## TASKS COMPLETED

🔹 Part A: Image Feature Extraction and Classification

Image Preprocessing: Loaded asphalt images using OpenCV, resized them to 128 × 128, and converted them to grayscale.

Feature Extraction: Extracted mean brightness, contrast, minimum/maximum intensity, median intensity, dark-pixel ratio, and bright-pixel ratio using NumPy.

Canny Features: Applied Canny edge detection and calculated edge count and edge density.

Classification: Trained Logistic Regression and Random Forest models.

Evaluation: Compared Accuracy, Precision, Recall, F1-score, Confusion Matrix, Training Time, and Prediction Time.

🔹 Part B: Email Spam Classification

Dataset Preparation: Loaded the email dataset, checked spam/non-spam distribution, handled missing values, and removed the Email No. identifier.

Feature Representation: The provided dataset was already represented using numerical word-frequency features and did not contain raw email text.

Classification: Following the instructor's guidance, the existing numerical features were directly used with Logistic Regression.

Evaluation: Measured Accuracy, Precision, Recall, F1-score, Confusion Matrix, Training Time, and Prediction Time.

Note: CountVectorizer and TF-IDF were not applied because raw email text was not available in the provided dataset.

🔹 Part C: Representation Improvement

Improvement: Applied StandardScaler to normalize the numerical email features.

Comparison: Compared the original and normalized representations using Accuracy, Precision, Recall, F1-score, Training Time, Prediction Time, and number of features.

## Final Observations

Image features based on pixel intensity and Canny edges were used for traditional machine learning classification.

The email dataset was already numerically represented, so it was directly used for Logistic Regression.

Feature normalization was tested as an improvement and compared with the original representation.

No CNNs, deep-learning models, or pretrained image embeddings were used.

## Tools and Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- OpenCV
- Scikit-learn
- Google Colab

## Repository Structure

202618049_Lab_06/

├── Lab_06_ML.ipynb       # Main runnable notebook
├── canny_edge.png        # Canny edge visualization
├── image_features.csv    # Extracted image features
└── README.md             # Project details and observations
