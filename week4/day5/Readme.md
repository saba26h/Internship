# Day 5 - Scikit-learn Pipelines & Tuned Mini-Project ⚙️🔗

## Overview

The fifth day of Week 4 focused on understanding **Scikit-learn Pipelines**, **ColumnTransformer**, and how to build a complete Machine Learning workflow that combines preprocessing, feature engineering, model training, hyperparameter tuning, and evaluation into a single leak-free process.

The goal was to learn how pipelines prevent data leakage, how to preprocess different feature types appropriately, how to tune an entire workflow using **GridSearchCV**, and how to structure Machine Learning projects using professional and reproducible practices.

---

## Topics Covered

### Why Pipelines Exist

I learned that performing preprocessing and modeling as separate manual steps can introduce **data leakage**.

The topics included:

* Understanding how data leakage occurs.
* Learning that scaling data before splitting can leak information from the test set.
* Understanding how preprocessing during cross-validation can accidentally use validation data.
* Learning that pipelines automatically apply preprocessing in the correct order.
* Understanding that pipelines create a leak-free workflow.
* Learning that preprocessing and modeling can be combined into a single object.

The main idea is:

**Preprocessing + Modeling → One Pipeline → No Data Leakage**

---

### Building a Pipeline

I learned how to create a Machine Learning pipeline using Scikit-learn's `Pipeline` class.

The topics included:

* Understanding the structure of a Pipeline.
* Chaining preprocessing and modeling steps together.
* Training the entire workflow using a single `fit()` call.
* Generating predictions using a single `predict()` call.
* Understanding how pipelines simplify Machine Learning workflows.
* Learning that every step is executed automatically in sequence.

A basic implementation is:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(random_state=42)),
])

pipe.fit(X_train, y_train)
pipe.predict(X_test)
```

The important idea is:

**One Object → Multiple Steps → Cleaner Workflow**

---

### Why Pipelines Prevent Data Leakage

I learned that pipelines automatically prevent common sources of data leakage.

The topics included:

* Understanding that preprocessing is fit only on the training data.
* Learning that test data is transformed using previously learned parameters.
* Understanding how cross-validation works correctly within a pipeline.
* Learning that each fold receives its own preprocessing.
* Understanding that validation data is never used when fitting transformations.
* Learning why this produces more reliable evaluation results.

The key benefit is:

**Training Data Only → Fit Transformations → Reliable Evaluation**

---

### ColumnTransformer for Mixed Data

I learned how to use **ColumnTransformer** when working with datasets that contain both numerical and categorical features.

The topics included:

* Understanding that different feature types require different preprocessing methods.
* Scaling numerical variables using `StandardScaler`.
* Encoding categorical variables using `OneHotEncoder`.
* Applying multiple transformations within a single preprocessing workflow.
* Understanding how ColumnTransformer organizes preprocessing steps.
* Learning how it integrates directly into a Pipeline.

The basic implementation is:

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

pre = ColumnTransformer([
    ("num", StandardScaler(), numeric_cols),
    ("cat", OneHotEncoder(), categorical_cols),
])
```

The important idea is:

**Numeric Features → Scaling**

**Categorical Features → Encoding**

**ColumnTransformer → Handles Both Together**

---

### Building a Complete Pipeline with ColumnTransformer

I learned how to combine a ColumnTransformer with a Machine Learning model inside a single Pipeline.

The topics included:

* Creating a preprocessing stage.
* Adding a model stage.
* Combining both stages into one workflow.
* Automating preprocessing and prediction.
* Creating a reusable Machine Learning pipeline.
* Building a professional workflow structure.

The basic implementation is:

```python
pipe = Pipeline([
    ("pre", pre),
    ("model", RandomForestClassifier())
])
```

This allows preprocessing and model training to be managed through one unified object.

---

### Tuning a Whole Pipeline

I learned that **GridSearchCV** can tune an entire pipeline instead of tuning only the model.

The topics included:

* Understanding how pipeline parameters are referenced.
* Learning the double-underscore (`__`) notation.
* Searching multiple hyperparameter combinations.
* Combining tuning with cross-validation.
* Selecting the best-performing configuration.
* Understanding how end-to-end optimization works.

The parameter naming format is:

```python
model__parameter_name
```

For example:

```python
param_grid = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [5, 10]
}
```

The important idea is:

**Pipeline + GridSearchCV → End-to-End Optimization**

---

### GridSearchCV for Pipeline Optimization

I learned how GridSearchCV evaluates multiple pipeline configurations using cross-validation.

The topics included:

* Defining a parameter grid.
* Training every parameter combination.
* Applying 5-fold cross-validation.
* Comparing validation performance.
* Selecting the best configuration automatically.
* Retrieving the best model and parameters.

The basic implementation is:

```python
grid = GridSearchCV(
    pipe,
    param_grid,
    cv=5,
    scoring="f1"
)

grid.fit(X_train, y_train)
```

---

### The Week 4 Mini-Project

I learned how to combine all concepts from Week 4 into a single Machine Learning workflow.

The project included:

* Applying EDA-informed Feature Engineering.
* Building a ColumnTransformer for mixed feature types.
* Creating a complete Pipeline.
* Using GridSearchCV for hyperparameter tuning.
* Applying 5-fold cross-validation.
* Evaluating the final tuned model on a held-out test set.
* Comparing tuned performance against a baseline model.
* Building a professional and leak-free workflow.

The main idea is:

**Feature Engineering + Pipeline + GridSearchCV + Cross-Validation = Professional Machine Learning Workflow**

---

### Hands-On Lab: Tuned End-to-End Pipeline

I practiced building and tuning a complete Machine Learning pipeline.

The practical task included:

* Building a Pipeline with a ColumnTransformer.
* Scaling numerical features.
* Encoding categorical features.
* Incorporating engineered features from Day 4.
* Tuning the full pipeline using GridSearchCV.
* Applying 5-fold cross-validation.
* Evaluating the tuned model on a held-out test set.
* Comparing the tuned model against a baseline model.
* Documenting results and evaluation metrics.
* Preparing the finished notebook for GitHub submission.

---

## Tools Used

* Scikit-learn (`Pipeline`, `ColumnTransformer`, `GridSearchCV`)
* Pandas
* Jupyter Notebook
* Git
* GitHub

---

## Key Takeaways

By the end of this day, I learned how **Scikit-learn Pipelines** can combine preprocessing and modeling into a single workflow while preventing data leakage.

I learned why pipelines are important, how they automatically apply preprocessing in the correct order, and how they produce more reliable evaluation results.

I practiced using **ColumnTransformer** to preprocess numerical and categorical features differently within the same dataset.

I also learned how to tune an entire pipeline using **GridSearchCV** and **5-fold cross-validation**, allowing preprocessing and modeling decisions to be optimized together.

Finally, I completed a tuned end-to-end Machine Learning workflow that combined **Feature Engineering, ColumnTransformer, Pipeline construction, Hyperparameter Tuning, Cross-Validation, and Model Evaluation** into a professional and reproducible process.

These concepts provide an important foundation for building leak-free Machine Learning systems and preparing for larger real-world Machine Learning projects.
