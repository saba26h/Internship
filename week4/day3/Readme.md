# Day 3 - Bias-Variance & Diagnosing Model Fit ⚖️📈

## Overview

The third day of Week 4 focused on understanding **Bias-Variance**, distinguishing between underfitting and overfitting, and diagnosing model fit using training and validation performance.

The goal was to understand how model complexity affects bias and variance, how to identify underfitting and overfitting from the train-vs-validation score gap, and how to reduce overfitting by simplifying the model or applying regularization.

---

## Topics Covered

### Underfitting vs. Overfitting

I learned that Machine Learning models can fail mainly in two ways: **underfitting** and **overfitting**.

The topics included:

* Understanding underfitting as a model that is too simple to capture the underlying pattern.
* Understanding overfitting as a model that is too complex and learns the training data too closely.
* Learning that underfitting is associated with high bias.
* Learning that overfitting is associated with high variance.
* Understanding the different symptoms of underfitting and overfitting.
* Learning that the appropriate fix depends on the type of model failure.

The main difference can be summarized as:

| Training Score | Validation Score      | Diagnosis    |
| -------------- | --------------------- | ------------ |
| Low            | Low                   | Underfitting |
| High           | Much lower            | Overfitting  |
| High           | High with a small gap | Good Fit     |

---

### The Bias-Variance Trade-off

I learned how **bias** and **variance** describe two different sources of model error.

The topics included:

* Understanding bias as error caused by overly simple assumptions.
* Understanding variance as sensitivity to the specific training data.
* Learning that simple models usually have higher bias.
* Learning that complex models usually have higher variance.
* Understanding that increasing model complexity can reduce bias but increase variance.
* Understanding that decreasing model complexity can reduce variance but increase bias.
* Learning that the goal is to find a balance between bias and variance.

The main idea is:

**Too simple → High Bias → Underfitting**

**Too complex → High Variance → Overfitting**

The goal is to find a model that is complex enough to learn the underlying pattern but simple enough to generalize well to unseen data.

---

### Diagnosing Model Fit Using the Train-vs-Validation Gap

I learned how to use the difference between training and validation scores to diagnose model fit.

The topics included:

* Evaluating the model on the training data.
* Evaluating the model on the validation data.
* Comparing the training and validation scores.
* Understanding what a large train-validation gap indicates.
* Using the scores as evidence when diagnosing model behavior.
* Identifying whether the model is underfitting, overfitting, or performing well.

The diagnostic rules are:

**Low training score + low validation score = Underfitting**

**High training score + much lower validation score = Overfitting**

**High training score + high validation score with a small gap = Good Fit**

The train-validation gap provides practical evidence about how well the model generalizes to unseen data.

---

### Deliberately Creating Overfitting

I learned how to intentionally create an overfitting situation using a highly complex **Decision Tree**.

The topics included:

* Training an unrestricted Decision Tree.
* Allowing the tree to become highly complex.
* Observing the training score.
* Comparing the training score with the validation score.
* Identifying a large train-validation gap.
* Diagnosing the model as overfitting.
* Understanding that the model has learned the training data too closely.

The expected pattern is:

**High training score + much lower validation score = Overfitting**

This demonstrates **high variance** in practice.

---

### Deliberately Creating Underfitting

I also learned how to intentionally create an underfitting situation using an overly simple **Decision Tree**.

The topics included:

* Limiting the depth of the Decision Tree.
* Restricting the model's ability to learn complex patterns.
* Evaluating the model on the training data.
* Evaluating the model on the validation data.
* Observing that both scores are low.
* Diagnosing the model as underfitting.
* Understanding that the model does not have enough capacity to learn the underlying pattern.

The expected pattern is:

**Low training score + low validation score = Underfitting**

This demonstrates **high bias** in practice.

---

### Fixing Overfitting by Reducing Model Complexity

I learned that one way to fix overfitting is to reduce the complexity of the model.

The topics included:

* Identifying an overfitted Decision Tree.
* Limiting the maximum depth of the tree.
* Training the simpler model again.
* Comparing the new training and validation scores.
* Checking whether the train-validation gap becomes smaller.
* Understanding that a simpler model can generalize better.

The goal is not simply to maximize the training score, but to achieve a better balance between training and validation performance.

---

### Regularization

I learned that **regularization** is a common technique for reducing overfitting by adding a penalty for model complexity.

The topics included:

* Understanding why regularization can reduce overfitting.
* Learning about Ridge Regression.
* Learning about Lasso Regression.
* Understanding the difference between L2 and L1 regularization.
* Understanding how regularization discourages overly large model weights.
* Learning how the `alpha` parameter controls the strength of regularization.

The basic implementation is:

```python
from sklearn.linear_model import Ridge, Lasso

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)
```

---

### Ridge and Lasso Regularization

I learned that **Ridge** uses L2 regularization, while **Lasso** uses L1 regularization.

The topics included:

* Understanding that Ridge shrinks model coefficients toward zero.
* Understanding that Lasso can shrink some coefficients exactly to zero.
* Learning that Lasso can therefore perform a form of feature selection.
* Understanding that both methods help control model complexity.
* Learning that `alpha` determines the strength of the regularization penalty.

A larger `alpha` means stronger regularization and a simpler model.

---

### Hands-On Lab: Diagnosing and Fixing Model Fit

I practiced diagnosing and fixing model fit using a Decision Tree and comparing training and validation scores.

The practical task included:

* Deliberately creating an overfitted Decision Tree.
* Comparing its training and validation scores.
* Identifying the large train-validation gap.
* Diagnosing the model as overfitting.
* Deliberately creating an underfitted Decision Tree.
* Comparing its training and validation scores.
* Diagnosing the model as underfitting.
* Reducing the complexity of the overfitted model.
* Comparing the new scores with the original model.
* Checking whether the train-validation gap became smaller.
* Documenting each diagnosis and fix using Markdown and score evidence.

---

## Tools Used

* Scikit-learn (`DecisionTreeClassifier`, `Ridge`, `Lasso`)
* Pandas
* Matplotlib
* Jupyter Notebook

---

## Key Takeaways

By the end of this day, I learned how to distinguish between **underfitting and overfitting** using training and validation performance.

I understood that underfitting is associated with **high bias**, while overfitting is associated with **high variance**.

I also learned how the **train-validation gap** can be used as a practical tool for diagnosing model fit.

I practiced deliberately creating both underfitting and overfitting cases using Decision Trees and then applying appropriate fixes by reducing model complexity.

Finally, I learned the basics of **regularization**, including Ridge (L2) and Lasso (L1), and how the `alpha` parameter controls the strength of the regularization.

These concepts provide an important foundation for **model tuning and hyperparameter optimization**, which will be explored further using `GridSearchCV`.
