# Week 3 - Machine Learning Fundamentals: Supervised Learning 🤖🚀

## Overview

During the third week of the internship, I started building the fundamental concepts required for Machine Learning model development.

The focus of this week is understanding supervised learning concepts, learning how Machine Learning models learn from labeled data, and becoming familiar with the Scikit-learn API used to build, train, and evaluate models.

Throughout this week, I learned how to prepare datasets, split data for training and testing, build different supervised learning models, evaluate their performance using appropriate metrics, compare multiple classification algorithms, and apply complete Machine Learning pipelines on real datasets.

---

# Completed Days

## Day 1 - Supervised Learning Concepts & Scikit-learn API 🤖

The first day focused on understanding the fundamentals of supervised learning and the general workflow used to build Machine Learning models.

I learned how models learn patterns from labeled datasets, how data is prepared for training, and how the Scikit-learn API provides a consistent way to implement Machine Learning workflows.

**Topics Covered:**

* Understanding the concept of Supervised Learning.
* Understanding labeled datasets and how models learn from examples.
* Differentiating between features (X) and target variables (y).
* Understanding the difference between Regression and Classification problems.
* Learning the general Machine Learning workflow.
* Splitting datasets into training and testing sets.
* Using `train_test_split()` from Scikit-learn.
* Understanding the importance of train/test split for model evaluation.
* Using `random_state` to achieve reproducible results.
* Understanding the Scikit-learn API structure.
* Creating and initializing Machine Learning models.
* Using the `fit()` method for model training.
* Using the `predict()` method for generating predictions.
* Understanding the common workflow shared between different Scikit-learn models.

---

## Day 2 - Linear Regression & Model Evaluation 📈

The second day focused on understanding Linear Regression and the process of building and evaluating regression models.

I learned how Linear Regression predicts continuous values, how models learn relationships between features and targets, and how to evaluate regression model performance using different metrics.

**Topics Covered:**

* Understanding the concept of Linear Regression.
* Learning how Linear Regression fits the best line through data.
* Understanding predictions using weights and bias.
* Training Linear Regression models using Scikit-learn.
* Using the `fit()` method for model training.
* Using the `predict()` method for generating predictions.
* Understanding and interpreting model coefficients.
* Understanding the role of the intercept (bias).
* Identifying the influence of features on predictions.
* Understanding regression evaluation metrics.
* Calculating Mean Absolute Error (MAE).
* Calculating Root Mean Squared Error (RMSE).
* Calculating R² score.
* Comparing model performance against a baseline model.
* Understanding whether a model provides meaningful improvements over simple predictions.

---

## Day 3 - Logistic Regression & Classification Metrics 📊

The third day focused on understanding Logistic Regression as a classification algorithm and learning how to evaluate classification models using different performance metrics.

I learned how Logistic Regression predicts class probabilities, how classification models are evaluated, and why accuracy alone is not always sufficient for measuring model performance.

**Topics Covered:**

* Understanding Logistic Regression as a classification algorithm.
* Learning how weighted sums are converted into probabilities using the sigmoid function.
* Understanding class probabilities and prediction thresholds.
* Training Logistic Regression models using Scikit-learn.
* Using `predict()` for generating class predictions.
* Using `predict_proba()` for obtaining class probabilities.
* Understanding why accuracy can be misleading on imbalanced datasets.
* Learning the structure of the confusion matrix.
* Understanding True Positive (TP), True Negative (TN), False Positive (FP), and False Negative (FN).
* Calculating and interpreting Precision.
* Calculating and interpreting Recall.
* Understanding the trade-off between Precision and Recall.
* Calculating F1-score for balanced model evaluation.
* Understanding AUC-ROC and its importance for classification evaluation.
* Using `confusion_matrix()` and `classification_report()` from Scikit-learn.
* Calculating AUC-ROC using `roc_auc_score()`.

---

## Day 4 - Decision Trees, Random Forests, SVM & k-Nearest Neighbors 🌳🌲

The fourth day focused on understanding different supervised learning classification algorithms and learning how to compare their performance fairly using the same dataset and evaluation metric.

I learned how Decision Trees, Random Forests, Support Vector Machines (SVM), and k-Nearest Neighbors (k-NN) make predictions, how each algorithm differs from the others, and how to evaluate multiple models to identify the most suitable classifier for a given dataset.

**Topics Covered:**

* Learning why Decision Trees are easy to interpret but prone to overfitting.
* Understanding how Random Forest combines multiple Decision Trees to improve performance.
* Interpreting feature importance values generated by Random Forest.
* Understanding how Support Vector Machines find the optimal decision boundary.
* Understanding how k-Nearest Neighbors classifies samples using the nearest neighbors.
* Training Decision Tree, Random Forest, SVM, and k-NN models using Scikit-learn.
* Comparing multiple classifiers using the same train/test split.
* Evaluating all models using the Weighted F1-Score.
* Identifying the best-performing model for the dataset.
* Interpreting Random Forest feature importance to understand which features contributed most to the predictions.

---

# Week 3 Checklist ✅

## Day 1 - Supervised Learning Concepts & Scikit-learn API

* [x] A notebook demonstrating supervised learning concepts, feature/target separation, train/test split, and basic Scikit-learn workflow.

## Day 2 - Linear Regression

* [x] A notebook demonstrating linear regression model training, prediction, coefficients, and regression evaluation metrics.

## Day 3 - Logistic Regression & Classification

* [x] A notebook covering logistic regression, classification concepts, confusion matrix, and classification evaluation metrics.

## Day 4 - Decision Trees, Random Forests, SVM & k-Nearest Neighbors

* [x] A notebook comparing Decision Tree, Random Forest, SVM, and k-NN classifiers using the same train/test split and the Weighted F1-Score, including feature importance analysis and model comparison.

## Day 5 - Supervised Learning Mini-Project

* [ ] A complete Machine Learning pipeline applied to a real dataset, including data preparation, model training, evaluation, and analysis.

---

# Week 3 Progress

During this week, I started learning the foundations of Machine Learning by focusing on supervised learning concepts and understanding how models learn from labeled data.

I learned the main workflow used in Machine Learning projects, starting from preparing datasets and separating features from targets, to splitting data into training and testing sets for evaluation.

I also became familiar with the Scikit-learn API and its standard workflow for building models using methods such as `fit()` for training and `predict()` for making predictions.

Additionally, I learned how Linear Regression models work, how they generate predictions using learned parameters, and how to evaluate regression models using MAE, RMSE, and R² metrics.

Furthermore, I learned how Logistic Regression is used for classification tasks, how models generate class probabilities, and how classification performance can be evaluated using confusion matrix, Precision, Recall, F1-score, and AUC-ROC.

In addition, I learned how different supervised learning algorithms make classification decisions and how to compare them fairly using the same training and testing datasets. I explored Decision Trees, Random Forests, Support Vector Machines (SVM), and k-Nearest Neighbors (k-NN), understood their strengths and limitations, evaluated their performance using the Weighted F1-Score, and interpreted Random Forest feature importance to identify the most influential features in the dataset.

Understanding these concepts provides the foundation required for developing regression and classification models, evaluating their performance, comparing different algorithms, and building complete Machine Learning pipelines in future tasks.
