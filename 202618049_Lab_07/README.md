DS605 Fundamentals of Machine Learning

Name: Twinkle Chauhan

Student ID: 202618049

Lab 07: Image Representation, PCA, Eigenfaces & Face Recognition

 Image Dataset: ORL Face Dataset (400 grayscale face images of 40 subjects)


## 📌 Project Overview

This project explores image representation, Principal Component Analysis (PCA), eigenfaces, image reconstruction, and face recognition using the ORL Face Dataset.

The objective is to understand how high-dimensional facial images can be represented in a lower-dimensional feature space while retaining important information. The project also evaluates different face recognition techniques and compares their recognition accuracy and storage requirements.

All experiments are implemented in Python using NumPy for PCA calculations and Scikit-learn for traditional machine learning classifiers.

## 🎯 Objectives

- Represent grayscale face images as numerical feature vectors.
- Implement PCA using NumPy linear algebra.
- Compare covariance-based eigendecomposition with Singular Value Decomposition (SVD).
- Analyze explained variance and select principal components.
- Visualize eigenfaces and reconstruct facial images.
- Compare face recognition using raw pixels and PCA features.
- Evaluate K-Nearest Neighbors (KNN) and Support Vector Machine (SVM).
- Investigate the trade-off between dimensionality, storage, reconstruction quality, and recognition accuracy.

## 🔬 Methodology

### Part A: Image Representation

- Loaded and inspected grayscale face images.
- Examined image dimensions and pixel intensity values.
- Flattened each image into a 10,304-dimensional feature vector.
- Constructed the feature matrix and subject labels.
- Created a reproducible, subject-wise training and testing split.

### Part B: PCA, Eigenfaces & Compression

- Calculated the mean face and centered the training data.
- Obtained principal directions using covariance-based eigendecomposition and SVD.
- Compared the results obtained from both methods.
- Calculated explained variance and cumulative explained variance.
- Determined the minimum number of principal components required to retain at least 90% of the training-data variance.
- Visualized eigenfaces.
- Projected images into PCA space and reconstructed sample faces.
- Evaluated reconstruction quality using Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR).
- Compared the estimated storage requirements of the original pixel representation and the PCA representation.

### Part C: Face Recognition Using Similarity

- Used Euclidean distance to identify the closest stored training face.
- Evaluated nearest-neighbor recognition using raw pixel features.
- Evaluated nearest-neighbor recognition using PCA features.
- Compared recognition accuracy.
- Inspected sample predictions and incorrectly recognized faces.

### Part D: Traditional Machine Learning

Trained and evaluated two classifiers using PCA features:

- **K-Nearest Neighbors (KNN):** Predicts a subject using the labels of nearby training samples.
- **Support Vector Machine (SVM):** Uses an RBF kernel to classify face representations.

The classifiers were compared with the nearest-neighbor similarity baseline. Additional validation experiments examined the effect of retaining different numbers of PCA components.

## 📊 Results and Analysis

The notebook and generated result files support analysis of:

- Explained variance and dimensionality reduction.
- Eigenfaces and principal directions.
- Image reconstruction quality.
- Storage requirements before and after PCA.
- Raw-pixel versus PCA-based nearest-neighbor recognition.
- KNN and SVM recognition accuracy.
- The effect of the number of PCA components on validation accuracy.

The actual numerical results are recorded in the generated CSV files and notebook outputs. These results can be used to identify which representation and classifier performed best in the experiments.

## 📂 Dataset

**Dataset:** ORL Face Dataset

| Property | Details |
|---|---|
| Number of subjects | 40 |
| Images per subject | 10 |
| Total images | 400 |
| Image type | Grayscale |
| Image dimensions | 112 × 92 pixels |
| Original features per image | 10,304 |
| Training images | 320 |
| Testing images | 80 |

Each image is converted into grayscale and flattened into a vector containing 10,304 pixel values. A subject-wise split ensures that every subject is represented in both the training and testing sets.

**Dataset setup:** The dataset is not included in this repository. Download the ORL Face Dataset separately and extract it so that the subject folders `s1` through `s40` are inside a folder named `Dataset`.

## 🛠️ Technologies Used

- Python
- Google Colab
- NumPy
- Matplotlib
- Pillow (PIL)
- Pandas
- Scikit-learn

**Implementation note:** PCA and the associated eigenface calculations are performed using NumPy linear algebra rather than Scikit-learn's PCA implementation.

## 📁 Repository Structure

```text
202618049_Lab_07/
│
├── 202618049_Lab_07.ipynb
├── README
├── pca_representations.npz
├── recognition_comparison.csv
├── ml_comparison.csv
└── component_tuning_results.csv
```

### File Descriptions

| File | Description |
|---|---|
| `202618049_Lab_07.ipynb` | Complete notebook containing the implementation, experiments, visualizations, and analysis |
| `pca_representations.npz` | Saved PCA representations, labels, mean face, principal directions, and explained-variance information |
| `recognition_comparison.csv` | Comparison of raw-pixel and PCA-based nearest-neighbor recognition |
| `ml_comparison.csv` | Comparison of nearest-neighbor, KNN, and SVM recognition results |
| `component_tuning_results.csv` | Validation results for different numbers of PCA components |
| `README` | Project documentation and instructions |

## 💡 Key Learning Outcomes

- Understanding image representation and high-dimensional features.
- Implementing PCA with NumPy linear algebra.
- Understanding eigenfaces and explained variance.
- Reconstructing images from reduced-dimensional representations.
- Measuring reconstruction quality and estimating storage savings.
- Implementing Euclidean-distance-based face recognition.
- Evaluating KNN and SVM using PCA features.
- Comparing dimensionality reduction and recognition performance.

## 📝 Conclusion

This project demonstrates the use of PCA for reducing the dimensionality of facial images and representing them through eigenfaces. It explores how much information can be retained in a compact feature representation and how PCA features can be used for face recognition.

The experiments compare raw-pixel nearest-neighbor matching, PCA-based nearest-neighbor matching, KNN, and SVM. Together, they provide practical insight into the relationship between dimensionality reduction, image reconstruction, storage efficiency, and recognition performance.
