# Day 4 - Decision Trees, Random Forests, SVM & k-Nearest Neighbors 🌳🤖

## Overview

The fourth day focused on understanding different supervised machine learning classification algorithms and learning how to compare their performance fairly using the same dataset and evaluation metric.

The goal was to understand how Decision Trees, Random Forests, Support Vector Machines (SVM), and k-Nearest Neighbors (k-NN) make predictions, identify their strengths and limitations, and compare multiple classifiers to determine which model performs best for a given classification problem.

---

## Topics Covered

### Decision Trees

I learned how Decision Trees make classification decisions by creating a sequence of decision rules based on the input features.

The topics included:

* Understanding how Decision Trees split data into smaller subsets.
* Learning how predictions are made using a tree-like structure.
* Understanding why Decision Trees are easy to interpret.
* Learning why deep trees are prone to overfitting.
* Using `DecisionTreeClassifier` from Scikit-learn to build classification models.

---

### Random Forests

I learned how Random Forest improves the performance of a single Decision Tree by combining multiple trees into one ensemble model.

The topics included:

* Understanding the concept of ensemble learning.
* Learning how Random Forest combines the predictions of multiple Decision Trees.
* Understanding how Random Forest reduces overfitting.
* Learning how feature importance identifies the most influential features.
* Using `RandomForestClassifier` from Scikit-learn to build ensemble models.

---

### Support Vector Machines (SVM)

I learned how Support Vector Machines classify data by finding the optimal decision boundary between different classes.

The topics included:

* Understanding the concept of the maximum margin.
* Learning how SVM separates different classes.
* Understanding the purpose of kernel functions for nonlinear classification.
* Learning when SVM performs well and its computational limitations.
* Using `SVC()` from Scikit-learn to build Support Vector Machine models.

---

### k-Nearest Neighbors (k-NN)

I learned how the k-Nearest Neighbors algorithm classifies new samples based on the labels of their closest neighbors.

The topics included:

* Understanding the nearest-neighbor voting process.
* Learning the effect of choosing different values of **k**.
* Understanding why k-NN performs prediction at runtime instead of during training.
* Learning the advantages and limitations of k-NN.
* Using `KNeighborsClassifier()` from Scikit-learn to build k-NN models.

---

### Comparing Classification Models

I learned how different machine learning algorithms can be compared fairly using the same training and testing datasets and the same evaluation metric.

The topics included:

* Understanding the importance of using the same train/test split.
* Learning how to compare multiple classifiers using the Weighted F1-Score.
* Understanding the "No Free Lunch" principle.
* Learning how to identify the best-performing model for a specific dataset.
* Interpreting Random Forest feature importance to understand which features contributed most to the predictions.

---

## Tools Used

* Python
* Scikit-learn
* Pandas
* Jupyter Notebook

---

## Key Takeaways

By the end of this day, I learned how Decision Trees, Random Forests, Support Vector Machines, and k-Nearest Neighbors work as classification algorithms. I also learned how to compare multiple machine learning models fairly using the same evaluation metric and how to interpret feature importance to better understand model predictions.

These concepts provide a strong foundation for selecting, evaluating, and comparing supervised machine learning models for different classification tasks.
