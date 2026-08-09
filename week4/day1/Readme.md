# Day 1 - Train / Validation / Test Splits 🤖📊

## Overview

The first day of Week 4 focused on understanding the importance of using separate training, validation, and test sets when building Machine Learning models.

The goal was to understand why a validation set is needed in addition to a test set, how to create a correct three-way split, how to tune a model using the validation set, and why the test set should only be used for the final evaluation.

---

## Topics Covered

### The Problem with Tuning Against a Single Test Set

I learned why using the test set during model tuning can lead to misleading evaluation results.

The topics included:

* Understanding the purpose of a test set.
* Learning why the test set should remain unseen during model selection.
* Understanding how repeatedly checking test performance can influence model decisions.
* Learning how tuning against the test set can lead to overly optimistic results.
* Understanding the importance of keeping evaluation data separate from the tuning process.

---

### Three-Way Data Split

I learned how to divide a dataset into training, validation, and test sets.

The topics included:

* Understanding the purpose of the training set.
* Understanding the purpose of the validation set.
* Understanding the purpose of the test set.
* Creating a 60/20/20 train/validation/test split.
* Using `train_test_split()` to create the different subsets.
* Using a fixed `random_state` to make the split reproducible.
* Checking the shapes of the resulting datasets.

---

### Training Set

I learned how the training set is used during the Machine Learning process.

The topics included:

* Training the model using the training data.
* Understanding that the model learns patterns from the training set.
* Using `fit()` to train the model.
* Keeping the validation and test sets separate from the training process.

---

### Validation Set and Model Tuning

I learned how the validation set is used to select the best model configuration.

The topics included:

* Understanding the purpose of a validation set.
* Testing different hyperparameter values.
* Evaluating each model using the validation set.
* Selecting the best hyperparameter based on validation performance.
* Understanding why the validation set can be used multiple times during tuning.
* Keeping the test set completely separate during the tuning process.

---

### Hyperparameter Tuning

I learned how to tune a Machine Learning model by changing one hyperparameter and comparing its performance.

The topics included:

* Understanding what hyperparameters are.
* Testing different values of a model setting.
* Comparing validation scores between different configurations.
* Selecting the best-performing configuration.
* Applying the selected configuration to the final model.

For the practical task, Logistic Regression can be tuned using the `C` parameter, while other models can use their own hyperparameters such as `max_depth` in Decision Trees or `n_estimators` in Random Forest.

---

### Final Model Evaluation

I learned how to evaluate the final model using the test set after completing the tuning process.

The topics included:

* Training the final model using the selected hyperparameter.
* Making predictions on the test set.
* Calculating the final evaluation score.
* Using the test set exactly once for final evaluation.
* Understanding why the final test score provides a better estimate of performance on unseen data.

---

### Avoiding Data Leakage

I learned why information from the test set should not be used during model development.

The topics included:

* Understanding the concept of data leakage.
* Keeping the test set isolated during training and tuning.
* Preventing test information from influencing model selection.
* Understanding how data leakage can produce unreliable evaluation results.
* Following a clean separation between training, validation, and test data.

---

## Machine Learning Workflow

The workflow practiced during this day was:

**Dataset → Train / Validation / Test Split → Train Models → Tune Using Validation → Select Best Model → Final Test Evaluation**

The test set remains untouched until the final evaluation.

---

## Tools Used

* Python
* Scikit-learn
* Pandas
* Jupyter Notebook
* VS Code

---

## Key Takeaways

By the end of this day, I learned how to create and use a three-way train/validation/test split for Machine Learning experiments.

I understood that the training set is used to train the model, the validation set is used to tune and select the best model configuration, and the test set is reserved for the final evaluation.

I also learned why tuning against the test set can lead to overly optimistic results and why keeping the test set unseen until the end is important for obtaining a reliable evaluation of the final model.

These concepts provide an important foundation for model selection, hyperparameter tuning, and reliable Machine Learning evaluation.
