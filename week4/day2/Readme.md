# Day 2 - Cross-Validation 🔄📊

## Overview

The second day of Week 4 focused on understanding **Cross-Validation** and why it can provide a more reliable performance estimate than using a single validation split.

The goal was to understand how k-fold cross-validation works, how to use `cross_val_score`, how to interpret the mean and standard deviation of the scores, and why stratified k-fold is important for classification problems.

---

## Topics Covered

### Why Cross-Validation Beats a Single Validation Split

I learned why relying on one validation split can produce a performance estimate that may be lucky or unlucky depending on how the data was divided.

The topics included:

* Understanding the limitation of using one validation split.
* Understanding how cross-validation uses multiple validation folds.
* Learning why multiple folds provide a more stable performance estimate.
* Understanding why one single split should not dominate the evaluation.
* Learning how averaging scores across folds provides a more trustworthy estimate.

---

### How k-Fold Cross-Validation Works

I learned how k-fold cross-validation divides the training data into `k` equal parts called folds.

The topics included:

* Dividing the training data into `k` folds.
* Using one fold for validation.
* Using the other `k - 1` folds for training.
* Repeating the process until every fold has been used for validation.
* Understanding that every data point is used for validation exactly once.
* Understanding that every data point is used for training `k - 1` times.
* Understanding why no data is wasted.
* Learning that `k = 5` or `k = 10` are common choices.

For `k = 5`, the process works as follows:

| Round | Trains On        | Validates On |
| ----- | ---------------- | ------------ |
| 1     | Folds 2, 3, 4, 5 | Fold 1       |
| 2     | Folds 1, 3, 4, 5 | Fold 2       |
| 3     | Folds 1, 2, 4, 5 | Fold 3       |
| 4     | Folds 1, 2, 3, 5 | Fold 4       |
| 5     | Folds 1, 2, 3, 4 | Fold 5       |

---

### `cross_val_score`

I learned how to use `cross_val_score` from Scikit-learn to perform cross-validation.

The topics included:

* Using `cross_val_score` to evaluate a model.
* Using `cv=5` to perform 5-fold cross-validation.
* Using `scoring="f1"` to evaluate the model using F1 score.
* Understanding that the function produces one score for each fold.
* Calculating the mean of the scores.
* Calculating the standard deviation of the scores.

The basic process is:

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_train, y_train, cv=5, scoring="f1")

print(scores)
print(scores.mean())
print(scores.std())
```

---

### Mean and Standard Deviation

I learned how the mean and standard deviation help interpret the results of cross-validation.

The topics included:

* Understanding the mean as the overall performance estimate.
* Understanding the standard deviation as the amount of variation across folds.
* Understanding that a high mean with a low standard deviation indicates stable performance.
* Understanding that a high mean with a high standard deviation may mean that the model performs well on some folds but not others.

The mean shows **how well the model performs overall**, while the standard deviation shows **how much the performance changes between folds**.

---

### Stratified k-Fold for Classification

I learned why stratified k-fold is important when working with classification problems, especially when the classes are imbalanced.

The topics included:

* Understanding the problem with plain k-fold for classification.
* Understanding that different folds can accidentally have different class proportions.
* Learning how stratified k-fold preserves the original class balance.
* Understanding why maintaining class balance across folds matters.
* Learning that Scikit-learn applies stratified k-fold automatically when cross-validating a classifier.

This directly addresses the imbalance problem raised in Week 3.

---

### Hands-On Lab: Cross-Validating a Model

I practiced applying cross-validation to a model from Week 3.

The practical task included:

* Taking a Week 3 model and evaluating it using 5-fold cross-validation.
* Using `cross_val_score`.
* Reporting the mean of the scores.
* Reporting the standard deviation of the scores.
* Comparing the cross-validated estimate with the single-split score from Day 1.
* Explaining any difference between the two results.
* Confirming that stratified folds are used for the classification task.
* Explaining why stratification matters for the classification data.

---

## Tools Used

* Scikit-learn (`cross_val_score`, `StratifiedKFold`)
* Pandas
* Jupyter Notebook

---

## Key Takeaways

By the end of this day, I learned how k-fold cross-validation can provide a more reliable performance estimate than using a single validation split.

I understood that the data is divided into multiple folds, with each fold being used for validation while the remaining folds are used for training.

I also learned how to use `cross_val_score` and how to interpret the mean and standard deviation of the scores across folds.

Finally, I learned why stratified k-fold is important for classification because it preserves the original class balance across the folds.

These concepts provide an important foundation for evaluating Machine Learning models more reliably and understanding the stability of their performance.
