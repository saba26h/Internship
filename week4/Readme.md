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

## Day 2 - Cross-Validation 🔄📊

The second day focused on understanding Cross-Validation and why it can provide a more reliable performance estimate than using a single validation split.

I learned how k-fold cross-validation works, how to use `cross_val_score()`, how to interpret the mean and standard deviation of the scores, and why stratified k-fold is important for classification problems.

**Topics Covered:**

* Understanding why cross-validation can provide a more reliable estimate than a single validation split.
* Understanding how k-fold cross-validation works.
* Dividing training data into multiple folds.
* Using one fold for validation and the remaining folds for training.
* Understanding that every data point is used for validation exactly once.
* Understanding that every data point is used for training `k - 1` times.
* Using `cross_val_score()` for cross-validation.
* Using 5-fold cross-validation.
* Interpreting the mean of the cross-validation scores.
* Interpreting the standard deviation of the scores across folds.
* Understanding why a high mean with a low standard deviation indicates more stable performance.
* Understanding why stratified k-fold is important for classification.
* Understanding how stratified k-fold preserves the original class balance across folds.
* Comparing the cross-validated estimate with the single-split score from Day 1.

---

## Day 3 - Bias-Variance & Diagnosing Model Fit ⚖️📈

The third day focused on understanding the bias-variance trade-off, distinguishing between underfitting and overfitting, and diagnosing model fit using training and validation performance.

I learned how model complexity affects bias and variance, how to identify underfitting and overfitting from the train-vs-validation score gap, and how to reduce overfitting by simplifying the model or applying regularization.

**Topics Covered:**

* Understanding underfitting and overfitting.
* Understanding underfitting as high bias.
* Understanding overfitting as high variance.
* Understanding how model complexity affects bias and variance.
* Understanding the bias-variance trade-off.
* Diagnosing underfitting using low training and validation scores.
* Diagnosing overfitting using a large train-validation score gap.
* Identifying good model fit when training and validation scores are both high with a small gap.
* Deliberately creating an overfitted Decision Tree.
* Deliberately creating an underfitted Decision Tree.
* Comparing training and validation scores to diagnose model fit.
* Reducing model complexity to fix overfitting.
* Understanding regularization as a technique for reducing overfitting.
* Learning about Ridge (L2) regularization.
* Learning about Lasso (L1) regularization.
* Understanding how the `alpha` parameter controls regularization strength.
* Documenting model diagnoses and fixes using score evidence.

---

## Day 4 - Feature Engineering & Hyperparameter Tuning ⚙️📊

The fourth day focused on understanding **Feature Engineering** and **Hyperparameter Tuning**, and how these techniques can improve Machine Learning model performance.

I learned how to create more informative features, apply appropriate transformations, distinguish between parameters and hyperparameters, and systematically search for better model configurations using `GridSearchCV` and cross-validation.

**Topics Covered:**

* Understanding Feature Engineering and its role in Machine Learning.
* Learning why better features can sometimes improve model performance more than choosing a more complex model.
* Creating new features from existing columns.
* Understanding feature creation and transformation.
* Using binning to group continuous variables into meaningful ranges.
* Understanding one-hot encoding for categorical variables.
* Extracting useful information from datetime features.
* Understanding the role of scaling in Feature Engineering.
* Understanding the difference between parameters and hyperparameters.
* Learning that parameters are learned by the model during training.
* Learning that hyperparameters are selected before training.
* Understanding common hyperparameters such as `max_depth`, `n_estimators`, `k`, and `alpha`.
* Understanding hyperparameter tuning as a systematic search problem.
* Defining a hyperparameter grid.
* Using `GridSearchCV` for automated hyperparameter tuning.
* Combining GridSearchCV with 5-fold cross-validation.
* Using `best_params_` to identify the best hyperparameter combination.
* Using `best_score_` to obtain the best cross-validated score.
* Using `best_estimator_` to retrieve the best trained model.
* Understanding how the number of hyperparameter combinations affects computational cost.
* Learning how `RandomizedSearchCV` can be used for larger search spaces.
* Comparing the tuned model with an untuned baseline.
* Identifying which engineered features and hyperparameters had the greatest impact on performance.
* Documenting the feature engineering and tuning process using Markdown and score evidence.

---

# Week 4 Checklist ✅

## Day 1 - Train / Validation / Test Splits

* [x] A notebook demonstrating a 60/20/20 train/validation/test split, model tuning using the validation set, and final evaluation on the test set.

## Day 2 - Cross-Validation

* [x] A notebook demonstrating k-fold and stratified k-fold cross-validation using `cross_val_score()`.

## Day 3 - Bias-Variance Trade-off

* [x] A notebook demonstrating the bias-variance trade-off and diagnosing overfitting and underfitting.

## Day 4 - Feature Engineering & Hyperparameter Tuning

* [x] A notebook demonstrating feature engineering and hyperparameter tuning using `GridSearchCV`.

## Day 5 - Scikit-learn Pipelines & Mini-Project

* [ ] A complete Machine Learning mini-project using Scikit-learn Pipelines and a tuned end-to-end workflow.

---

# Week 4 Progress

During Day 1, I learned how to create a 60/20/20 train/validation/test split and use each set correctly for training, tuning, and final evaluation.

During Day 2, I learned how to use cross-validation with multiple folds, interpret the mean and standard deviation of the scores, and understand the importance of stratified folds for classification.

During Day 3, I learned how to distinguish between underfitting and overfitting using training and validation scores, understand the bias-variance trade-off, and apply model complexity reduction and regularization to improve model fit.

During Week 4, I learned how to validate and diagnose Machine Learning models using train/validation/test splits, cross-validation, and bias-variance analysis.

I also practiced feature engineering and systematic hyperparameter tuning using GridSearchCV, preparing for the final Pipeline-based mini-project.

Overall, Week 4 has helped me move from simply training Machine Learning models toward **validating, diagnosing, improving, and systematically optimizing models** before building a complete end-to-end pipeline.
