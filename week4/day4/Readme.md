# Day 4 - Feature Engineering & Hyperparameter Tuning ⚙️📊

## Overview

The fourth day of Week 4 focused on understanding **Feature Engineering** and **Hyperparameter Tuning**, and how these techniques can improve Machine Learning model performance.

The goal was to learn how to create more informative features, apply appropriate transformations, distinguish between parameters and hyperparameters, and systematically search for better model configurations using **GridSearchCV** and cross-validation.

---

## Topics Covered

### Feature Engineering

I learned that **Feature Engineering** is the process of creating, transforming, or selecting input features to provide a Machine Learning model with more useful information.

The topics included:

* Understanding what Feature Engineering is.
* Learning why better features can sometimes improve model performance more than choosing a more complex model.
* Understanding how domain knowledge can be used to create meaningful features.
* Learning how transforming existing data can make patterns easier for a model to learn.
* Understanding that good features can improve both model performance and generalization.

The main idea is:

**Better Features → Better Information → Better Learning**

Feature Engineering is therefore an important part of building effective Machine Learning models.

---

### Common Feature Engineering Techniques

I learned several common techniques for engineering features.

The topics included:

* **Feature Creation:** Combining existing columns to create a more informative feature.
* **Binning:** Converting continuous values into meaningful ranges or groups.
* **One-Hot Encoding:** Converting categorical variables into numerical columns.
* **Datetime Extraction:** Extracting useful information such as day, month, or day of the week from dates.
* **Scaling:** Transforming numerical features to comparable ranges.

Examples include:

```python
price_per_sqm = price / area
```

and extracting information such as:

```text
order_date → day_of_week, month
```

The important idea is that the original columns may not always contain the most useful representation of the information.

---

### Why Feature Engineering Matters

I learned that **Feature Engineering can sometimes matter more than Model Choice**.

The topics included:

* Understanding that a sophisticated model cannot compensate for poor or uninformative features.
* Learning that meaningful features can expose patterns that were difficult for the model to discover.
* Understanding the importance of domain knowledge when creating features.
* Learning that improving the input representation can significantly improve predictions.

This can be summarized as:

**Better Data Representation → Easier Learning**

Therefore, before immediately switching to a more complicated model, it is often useful to ask whether the features themselves can be improved.

---

### Hyperparameters vs. Parameters

I learned the difference between **parameters** and **hyperparameters**.

The topics included:

* Understanding that parameters are learned automatically by the model during training.
* Understanding that hyperparameters are selected before training.
* Learning that model parameters are determined from the training data.
* Learning that hyperparameters control how the model learns.
* Understanding that finding good hyperparameters is a search problem.

Examples of parameters include:

* Regression coefficients.
* Model weights.

Examples of hyperparameters include:

* `max_depth` in a Decision Tree or Random Forest.
* `n_estimators` in a Random Forest.
* `k` in k-NN.
* `alpha` in Ridge or Lasso.

The main difference is:

**Parameters → Learned by the model**

**Hyperparameters → Set by us before training**

---

### Hyperparameter Tuning

I learned that hyperparameter tuning is the process of searching for better values of a model's hyperparameters.

The topics included:

* Understanding why manually trying hyperparameters is inefficient.
* Defining a set of possible hyperparameter values.
* Testing different combinations systematically.
* Using cross-validation to evaluate each configuration.
* Selecting the configuration that performs best according to the chosen metric.

Instead of guessing:

```text
max_depth = 5
max_depth = 10
max_depth = 15
```

we can allow a search method to evaluate several possibilities systematically.

This makes the tuning process more structured and reproducible.

---

### GridSearchCV

I learned how **GridSearchCV** can automatically search through a predefined hyperparameter grid while using cross-validation.

The topics included:

* Understanding what a parameter grid is.
* Defining multiple possible values for each hyperparameter.
* Combining hyperparameter search with cross-validation.
* Training and evaluating every combination.
* Finding the best-performing configuration.
* Accessing the best parameters using `best_params_`.
* Accessing the best cross-validated score using `best_score_`.
* Accessing the best trained model using `best_estimator_`.

A basic implementation is:

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [5, 10, None]
}

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring="f1"
)

grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_score_)

best_model = grid.best_estimator_
```

---

### Understanding the Grid Search Cost

I learned that the computational cost of GridSearchCV increases as the number of hyperparameter combinations increases.

For example:

```text
2 n_estimators values × 3 max_depth values × 5 folds
= 30 model fits
```

This means that a larger grid can require significantly more training time.

The important idea is:

**More combinations → More model fits → More computational cost**

Therefore, the search space should be designed carefully.

---

### RandomizedSearchCV

I learned that **RandomizedSearchCV** can be useful when the hyperparameter search space becomes large.

The topics included:

* Understanding the limitation of very large GridSearchCV searches.
* Learning that RandomizedSearchCV samples a specified number of combinations.
* Understanding that it does not need to test every possible combination.
* Learning that it can be significantly faster for large search spaces.
* Understanding the trade-off between search coverage and computational cost.

The main difference is:

**GridSearchCV → Tests every combination**

**RandomizedSearchCV → Tests a selected number of combinations**

RandomizedSearchCV is therefore useful when the possible hyperparameter combinations become too large for an exhaustive search.

---

### Hands-On Lab: Feature Engineering & Hyperparameter Tuning

I practiced applying Feature Engineering and Hyperparameter Tuning to a Machine Learning dataset.

The practical task included:

* Creating at least two new engineered features.
* Justifying why each engineered feature could provide useful information.
* Defining a hyperparameter grid for a model from Week 3.
* Using a Random Forest model for hyperparameter tuning.
* Running `GridSearchCV` with 5-fold cross-validation.
* Finding the best hyperparameter combination.
* Reporting the best parameters.
* Reporting the best cross-validated score.
* Comparing the tuned model with the untuned baseline model.
* Identifying which engineered feature had the greatest impact.
* Identifying which hyperparameter had the greatest impact.
* Documenting the reasoning and results using Markdown and score evidence.

---

## Tools Used

* Scikit-learn (`GridSearchCV`, `RandomizedSearchCV`, `RandomForestClassifier`)
* Pandas
* Jupyter Notebook

---

## Key Takeaways

By the end of this day, I learned how **Feature Engineering** can improve Machine Learning models by creating more informative representations of the original data.

I learned several common feature engineering techniques, including **feature creation, binning, one-hot encoding, datetime extraction, and scaling**.

I also learned the important difference between **parameters and hyperparameters**. Parameters are learned by the model during training, while hyperparameters are selected before training.

I practiced using **GridSearchCV** to systematically search through different hyperparameter combinations while applying **5-fold cross-validation**.

I learned how to use `best_params_`, `best_score_`, and `best_estimator_` to identify and retrieve the best configuration found during the search.

Finally, I learned why **RandomizedSearchCV** can be more efficient than GridSearchCV when the hyperparameter search space becomes large.

These concepts provide an important foundation for building more reliable and optimized Machine Learning pipelines and will be used in the next stage of **model tuning and pipeline optimization**.
