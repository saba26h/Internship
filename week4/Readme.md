# Week 4 - Model Validation, Selection & Optimization 🤖📊

## Overview

During the fourth week of the internship, I started learning more advanced techniques for validating, selecting, and improving Machine Learning models.

The focus of this week is understanding how to obtain more reliable estimates of model performance, compare different model configurations, diagnose overfitting and underfitting, perform feature engineering, tune hyperparameters, and build complete Machine Learning pipelines using Scikit-learn.

Throughout this week, I will learn how to use train/validation/test splits, cross-validation techniques, bias-variance concepts, feature engineering, hyperparameter tuning, and Scikit-learn Pipelines to develop more reliable and optimized Machine Learning models.

---

# Completed Days

## Day 1 - Train / Validation / Test Splits 🤖📊

The first day focused on understanding why a single train/test split is not always sufficient for reliable Machine Learning model development.

I learned how to divide a dataset into training, validation, and test sets, how each dataset is used during the Machine Learning workflow, and why the test set should remain untouched until the final evaluation.

**Topics Covered:**

* Understanding the purpose of training, validation, and test sets.
* Creating a 60/20/20 train/validation/test split.
* Understanding the role of the training set in model learning.
* Understanding the role of the validation set in model selection and tuning.
* Understanding the role of the test set in final model evaluation.
* Using `train_test_split()` from Scikit-learn.
* Using a fixed `random_state` to achieve reproducible results.
* Training a Machine Learning model using the training set.
* Tuning one model setting using the validation set only.
* Evaluating the final model on the test set exactly once.
* Understanding why tuning against the test set can produce overly optimistic results.
* Understanding why a single train/test split provides a limited estimate of model performance.

---

# Week 4 Checklist ✅

## Day 1 - Train / Validation / Test Splits

* [x] A notebook demonstrating a 60/20/20 train/validation/test split, model tuning using the validation set, and final evaluation on the test set.

## Day 2 - Cross-Validation

* [ ] A notebook demonstrating k-fold and stratified k-fold cross-validation using `cross_val_score()`.

## Day 3 - Bias-Variance Trade-off

* [ ] A notebook demonstrating the bias-variance trade-off and diagnosing overfitting and underfitting.

## Day 4 - Feature Engineering & Hyperparameter Tuning

* [ ] A notebook demonstrating feature engineering and hyperparameter tuning using `GridSearchCV`.

## Day 5 - Scikit-learn Pipelines & Mini-Project

* [ ] A complete Machine Learning mini-project using Scikit-learn Pipelines and a tuned end-to-end workflow.

---

# Week 4 Progress

During Day 1, I learned how to create a 60/20/20 train/validation/test split and use each set correctly for training, tuning, and final evaluation.

I also practiced tuning a model using the validation set and learned why the test set must remain unseen until the final evaluation.
