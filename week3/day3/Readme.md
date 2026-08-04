# Day 3 - Logistic Regression & Classification Metrics 🤖📊

## Overview

The third day focused on understanding Logistic Regression as a classification algorithm and learning how to evaluate classification models using different metrics.

The goal was to understand how Logistic Regression predicts class probabilities, why accuracy alone can be misleading on imbalanced datasets, and how to use evaluation metrics such as confusion matrix, precision, recall, F1-score, and AUC-ROC.

---

## Topics Covered

### Logistic Regression for Classification

I learned the fundamentals of Logistic Regression and how it is used for classification problems.

The topics included:

* Understanding why Logistic Regression is a classification model despite its name.
* Learning how weighted sums are converted into probabilities using the sigmoid function.
* Understanding class probabilities between 0 and 1.
* Learning how classification decisions are made using probability thresholds.
* Using LogisticRegression from Scikit-learn for building classification models.

---

### Why Accuracy Alone Is Misleading

I learned why accuracy is not always a reliable metric for evaluating classification models.

The topics included:

* Understanding accuracy as a classification evaluation metric.
* Learning how imbalanced datasets can make accuracy misleading.
* Understanding why models that always predict the majority class can achieve high accuracy.
* Recognizing the need for additional evaluation metrics.

---

### Confusion Matrix

I learned how to analyze classification results using the confusion matrix.

The topics included:

* Understanding True Positive (TP), True Negative (TN), False Positive (FP), and False Negative (FN).
* Learning how the confusion matrix summarizes model predictions.
* Using confusion_matrix() from Scikit-learn to evaluate classification results.
* Understanding different types of classification errors.

---

### Precision, Recall, and F1-score

I learned how to measure classification performance using different evaluation metrics.

The topics included:

* Understanding Precision and what it measures.
* Understanding Recall and what it measures.
* Learning the trade-off between Precision and Recall.
* Understanding F1-score as a balance between Precision and Recall.
* Using classification_report() from Scikit-learn to calculate evaluation metrics.

---

### AUC-ROC

I learned how AUC-ROC is used to evaluate classification models independently of a specific classification threshold.

The topics included:

* Understanding the idea of ROC curves.
* Learning what AUC represents.
* Understanding how AUC measures the ability of a model to distinguish between classes.
* Using roc_auc_score() to calculate AUC-ROC.

---

## Tools Used

* Python
* Scikit-learn
* Pandas
* Matplotlib
* Jupyter Notebook

---

## Key Takeaways

By the end of this day, I learned how Logistic Regression works as a classification algorithm, understood how to evaluate classification models using different metrics, and learned why relying only on accuracy is not sufficient.

These concepts provide the foundation for building, evaluating, and improving classification models in Machine Learning.
