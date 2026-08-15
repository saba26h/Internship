# Cardiac Patient Monitoring System

## 1. Project Overview

The **Cardiac Patient Monitoring System** is a supervised machine
learning project that predicts whether a patient is classified as having
heart disease based on cardiovascular and health-related
characteristics.

The project treats the task as a **binary classification problem**. The
workflow covers data inspection, cleaning, exploratory data analysis,
statistical analysis, preprocessing, model training, cross-validation,
feature engineering, model comparison, final evaluation, error analysis,
and model export.

The main objective is to build and evaluate a reproducible machine
learning workflow and to understand which patient-related variables
contribute to the prediction.

> **Important:** The dataset used in this project is synthetic. The
> resulting model is intended for educational and machine learning
> purposes and must not be interpreted as a clinical diagnostic system.

------------------------------------------------------------------------

## 2. Project Objective

The main question addressed by this project is:

> **How can patient health and clinical characteristics be used to
> predict the presence of a cardiac condition, and can feature
> engineering improve the performance of machine learning models for
> this classification task?**

The project aims to:

-   Explore the structure and characteristics of the heart-disease
    dataset.
-   Check data types, unique values, missing values, and class
    distribution.
-   Analyze numerical and categorical variables.
-   Investigate relationships between predictors and the target.
-   Prepare numerical and categorical features for machine learning.
-   Build a Logistic Regression baseline.
-   Build a Random Forest classifier.
-   Compare the models using multiple classification metrics.
-   Use five-fold cross-validation to examine model stability.
-   Create additional engineered features based on relationships between
    existing variables.
-   Compare original and engineered feature sets.
-   Evaluate the final model on an untouched test set.
-   Analyze classification errors using a confusion matrix and other
    evaluation tools.
-   Save the final trained pipeline for future use.

------------------------------------------------------------------------

## 3. Project Structure

``` text
Cardiac_Patient_Monitoring/
│
├── data/
│   └── heart (1).csv
│
├── models/
│   └── final_model.pkl
│
├── notebooks/
│   └── cardiac_patient_monitoring.ipynb
│
├── outputs/
│
├── src/
│   ├── engineered_features.py
│   ├── evaluate.py
│   └── __pycache__/
│
└── README.md
```

------------------------------------------------------------------------
### Main Project Components

| Path | Purpose |
|-------|----------|
| `data/heart (1).csv` | Dataset used for analysis and model training |
| `models/final_model.pkl` | Saved trained model pipeline |
| `notebooks/cardiac_patient_monitoring.ipynb` | Main notebook containing analysis, visualizations, model training, evaluation, and documentation |
| `src/engineered_features.py` | Feature engineering functions |
| `src/evaluate.py` | Model evaluation functions and metrics |
| `outputs/` | Generated results, figures, exported files, and evaluation outputs |
| `README.md` | Project documentation, setup instructions, and usage guide |

------------------------------------------------------------------------

## 4. Dataset

The dataset contains **918 observations and 12 variables**.

The notebook inspection confirms that all 918 rows are non-null across
the dataset, with no missing values detected during the initial data
inspection.

The dataset contains numerical and categorical information related to
cardiovascular health. Examples of the variables used in the project
include:

### Numerical Features

-   `Age`
-   `RestingBP`
-   `Cholesterol`
-   `FastingBS`
-   `MaxHR`
-   `Oldpeak`

### Categorical Features

-   `Sex`
-   `ChestPainType`
-   `RestingECG`
-   `ExerciseAngina`
-   `ST_Slope`

The remaining variable is the binary target representing the
heart-disease outcome.

The target distribution contains:

-   **508 positive cases**
-   **410 negative cases**

This corresponds to approximately:

-   **55.3% positive**
-   **44.7% negative**

------------------------------------------------------------------------

## 5. Data Preparation

The notebook follows a structured preprocessing workflow.

### 5.1 Data Inspection

The dataset is first loaded and inspected to understand:

-   Dataset dimensions
-   Column names
-   Data types
-   Missing values
-   Number of unique values
-   Descriptive statistics
-   Target distribution

### 5.2 Missing Values

The initial inspection found no missing values.

The project still includes missing-value handling inside the
preprocessing pipelines to make the machine learning workflow more
robust.

For numerical variables, the preprocessing pipeline uses median
imputation when required.

For categorical variables, the preprocessing pipeline uses the most
frequent category when required.

### 5.3 Numerical Feature Processing

Numerical features are processed using:

1.  Missing-value imputation
2.  Standard scaling

`StandardScaler` is used for the numerical pipeline so that numerical
variables are placed on a comparable scale.

### 5.4 Categorical Feature Processing

Categorical features are processed using:

1.  Most-frequent-value imputation
2.  One-hot encoding

`OneHotEncoder` converts categorical values into numerical indicator
features that machine learning models can use.

### 5.5 Pipeline-Based Processing

Preprocessing is placed inside a scikit-learn `Pipeline` and
`ColumnTransformer`.

This is important because the transformations are learned from the
appropriate training data instead of being calculated globally before
model validation. This helps reduce the risk of data leakage.

------------------------------------------------------------------------

## 6. Exploratory Data Analysis

The notebook performs exploratory analysis before model training.

The analysis includes:

-   Distribution analysis of numerical variables.
-   Categorical feature distributions.
-   Target-class distribution.
-   Correlation analysis.
-   Relationships between numerical predictors and the target.
-   Feature-level investigation.

The analysis found that:

-   `MaxHR` had the strongest negative linear correlation with the
    target among the numerical predictors.
-   `Oldpeak` had the strongest positive linear correlation with the
    target among the numerical predictors.

The exploratory analysis is used to understand the dataset before
selecting and evaluating machine learning models.

------------------------------------------------------------------------

## 7. Train, Validation, and Test Strategy

The project separates the data into development and test data and then
uses a validation split within the development data.

The general workflow is:

``` text
Dataset
   │
   ├── Development Data
   │       │
   │       ├── Training Data
   │       │
   │       └── Validation Data
   │
   └── Test Data
```

The validation data is used for model comparison and feature-engineering
decisions.

The final test set is kept separate and is used for the final
evaluation.

The final test set contains **184 observations**.

------------------------------------------------------------------------

## 8. Machine Learning Models

Two main supervised classification models are evaluated.

### 8.1 Logistic Regression

Logistic Regression is used as the baseline model.

It is appropriate for binary classification and provides a relatively
simple and interpretable reference point.

The model uses the same preprocessing structure as the other models so
that comparisons focus on the classifier rather than differences in data
preparation.

The Logistic Regression configuration uses:

``` text
max_iter = 1000
random_state = 42
```

### 8.2 Random Forest

Random Forest is used as the more flexible comparison model.

The Random Forest configuration includes:

``` text
n_estimators = 200
class_weight = "balanced"
n_jobs = -1
random_state = 42
```

The model is useful because it can capture nonlinear relationships and
interactions between variables that a linear model may not represent as
effectively.

------------------------------------------------------------------------

## 9. Evaluation Metrics

The project evaluates classification performance using several metrics.

### Accuracy

Accuracy measures the proportion of all predictions that are correct.

``` text
Accuracy = Correct Predictions / Total Predictions
```

### Precision

Precision measures how many of the observations predicted as positive
are actually positive.

A higher precision means fewer false-positive predictions.

### Recall

Recall measures how many of the actual positive cases are correctly
identified.

Recall is particularly important when missing positive cases is an
important concern.

### F1-Score

F1-score combines precision and recall into a single metric.

It is useful when both false positives and false negatives matter.

### ROC-AUC

ROC-AUC measures how well the model separates the two classes across
different classification thresholds.

A higher ROC-AUC indicates stronger ranking/separation ability.

### Confusion Matrix

The confusion matrix separates predictions into:

-   True Positives
-   True Negatives
-   False Positives
-   False Negatives

This gives a more detailed view of the types of mistakes made by the
model.

------------------------------------------------------------------------

## 10. Model Comparison

## 10. Model Comparison

On the recorded validation split, Random Forest performed better than Logistic Regression.

| Metric | Logistic Regression | Random Forest | Change |
|---|---:|---:|---:|
| Accuracy | 0.803 | 0.850 | +0.048 |
| Precision | 0.802 | 0.831 | +0.029 |
| Recall | 0.852 | 0.914 | +0.062 |
| F1-Score | 0.826 | 0.871 | +0.044 |
| ROC-AUC | 0.904 | 0.910 | +0.005 |

The largest improvement was in **Recall**, increasing from approximately
**85.2% to 91.4%**.

This indicates that the Random Forest identified more of the actual
positive cases in the validation split.

The improvement in ROC-AUC was smaller than the improvement in the
threshold-based metrics, but it still indicates slightly better
class-ranking performance.

------------------------------------------------------------------------

## 11. Cross-Validation

Five-fold cross-validation is used to check whether model performance is
consistent across multiple data splits.

Instead of relying on only one validation split, the development data is
divided into five folds.

Each fold is used as a validation fold once while the remaining folds
are used for training.

The project evaluates:

-   Accuracy
-   Precision
-   Recall
-   F1-Score
-   ROC-AUC

The average score and variability across folds provide additional
information about model stability.

This is important because a single validation split can produce a score
that is influenced by the specific observations assigned to that split.

------------------------------------------------------------------------

## 12. Feature Engineering

The project tests whether additional features can provide useful
information to the models.

The engineered numerical features include:

-   `Cholesterol_Age_Ratio`
-   `MaxHR_Age_Ratio`
-   `BP_Age_Ratio`
-   `Heart_Stress`

These features attempt to represent relationships between existing
cardiovascular measurements rather than relying only on the original
variables independently.

Feature engineering is evaluated experimentally rather than being
assumed to improve the model.

------------------------------------------------------------------------

## 13. Feature Engineering Findings

An important result of the experiment is that feature engineering **did
not improve validation performance**.

The original Random Forest performed slightly better than the engineered
Random Forest on the recorded validation comparison.

Therefore, the project does not claim that feature engineering
automatically improved the model.

This is an important machine learning finding:

> Adding more features does not necessarily make a model better.

Engineered variables can introduce additional information, but they can
also add noise, redundancy, or relationships that do not generalize well
to the validation data.

------------------------------------------------------------------------

## 14. Final Test Evaluation

The final code retrains the engineered Random Forest using the development data and evaluates it on the untouched test set.

The recorded final test results are:

| Metric | Final Test Score |
|---|---:|
| Accuracy | **0.902** |
| Precision | **0.896** |
| Recall | **0.931** |
| F1-Score | **0.913** |
| ROC-AUC | **0.942** |

The final model correctly classified approximately **90.2% of the 184
test observations**.

For the `Heart Disease` class:

| Metric | Score |
|---|---:|
| Precision | 0.90 |
| Recall | 0.93 |
| F1-Score | 0.91 |
| Support | 102 |

For the `No Heart Disease` class:

| Metric | Score |
|---|---:|
| Precision | 0.91 |
| Recall | 0.87 |
| F1-Score | 0.89 |
| Support | 82 |

The stronger recall for the heart-disease class means the final model
identified most of the actual positive cases in the test set.

------------------------------------------------------------------------

## 15. Important Model-Selection Note

There is an important methodological distinction in the project.

The recorded validation comparison shows that the **original Random
Forest** performed slightly better than the engineered Random Forest.

However, the final workflow later retrains and evaluates the
**engineered Random Forest** on the untouched test set.

Therefore:

-   The project should **not** claim that feature engineering improved
    validation performance.
-   The final test score should be presented as the performance of the
    final engineered Random Forest on the held-out test set.
-   Validation results and final test results should not be treated as
    the same experiment.
-   The higher final test score does not by itself prove that feature
    engineering caused the improvement.

This distinction is documented in the notebook to keep the
model-selection narrative accurate.

------------------------------------------------------------------------

## 16. Outputs and Saved Model

The project saves the final trained pipeline as:

``` text
models/final_model.pkl
```

The saved object contains the preprocessing steps and classifier
together.

This means future predictions can use the same:

-   Numerical imputation
-   Numerical scaling
-   Categorical encoding
-   Expected feature preparation
-   Random Forest classifier

The project also exports evaluation and feature-importance results to
the `outputs/` directory.

------------------------------------------------------------------------

## 17. Installation and Setup

### Prerequisites

The project requires:

-   Python
-   Jupyter Notebook
-   NumPy
-   pandas
-   Matplotlib
-   Seaborn
-   scikit-learn
-   joblib

### Create a Virtual Environment

From the project root:

``` bash
python -m venv .venv
```

Activate it on Windows:

``` bash
.venv\Scripts\activate
```

Activate it on macOS/Linux:

``` bash
source .venv/bin/activate
```

### Install Dependencies

``` bash
pip install numpy pandas matplotlib seaborn scikit-learn joblib jupyter
```

------------------------------------------------------------------------

## 18. How to Run the Project

### Step 1: Open the Project Folder

Open a terminal in the project root:

``` text
Cardiac_Patient_Monitoring/
```

### Step 2: Activate the Virtual Environment

Windows:

``` bash
.venv\Scripts\activate
```

macOS/Linux:

``` bash
source .venv/bin/activate
```

### Step 3: Start Jupyter from the `notebooks` Directory

The notebook is designed around the project directory structure and uses
the parent directory as the project root.

Therefore, start Jupyter from the `notebooks` folder:

``` bash
cd notebooks
jupyter notebook
```

Then open:

``` text
cardiac_patient_monitoring.ipynb
```

### Step 4: Run the Notebook

Run the notebook cells from top to bottom.

The notebook workflow is:

``` text
Load Data
    ↓
Inspect Data
    ↓
Clean and Prepare Data
    ↓
Exploratory Data Analysis
    ↓
Analyze Relationships
    ↓
Split Data
    ↓
Build Preprocessing Pipeline
    ↓
Train Logistic Regression
    ↓
Train Random Forest
    ↓
Compare Models
    ↓
Five-Fold Cross-Validation
    ↓
Feature Analysis
    ↓
Feature Engineering
    ↓
Compare Original vs Engineered Features
    ↓
Train Final Model
    ↓
Evaluate Test Set
    ↓
Error Analysis
    ↓
Save Results
    ↓
Save Final Model
```

### Step 5: Check Generated Files

After successful execution, check:

``` text
models/
```

for:

``` text
final_model.pkl
```

and:

``` text
outputs/
```

for the generated result files.

------------------------------------------------------------------------

## 19. Running the Saved Model

The saved model is stored as a complete scikit-learn pipeline.

It can be loaded using `joblib`:

``` python
import joblib

model = joblib.load("models/final_model.pkl")
```

A new input record must contain the same expected feature structure used
by the final pipeline.

The saved pipeline applies the required preprocessing before generating
a prediction.

------------------------------------------------------------------------

## 20. Reproducibility

The project uses:

``` text
random_state = 42
```

in the relevant data-splitting and model-training steps.

This helps make the experiment reproducible when the same environment,
data, and workflow are used.

The use of pipelines also helps ensure that preprocessing is
consistently applied during training, validation, cross-validation, and
prediction.

------------------------------------------------------------------------

## 21. Limitations

This project has several important limitations.

### Synthetic Dataset

The dataset is synthetic and does not represent real clinical patient
data.

Therefore, the observed performance cannot be interpreted as real-world
medical performance.

### Not a Clinical Diagnostic System

The model was developed for educational machine learning purposes.

It has not been clinically validated and should not be used to diagnose
patients or make medical decisions.

### Unusual Numerical Values

Some numerical variables contain values that may be unusual or
unrealistic in a real clinical setting.

Such values can affect:

-   Distributions
-   Correlations
-   Feature importance
-   Model behavior
-   Final predictions

### Categorical Imbalance

Some categorical variables contain categories that occur much more
frequently than others.

This can influence model learning and evaluation.

### Limited Test Set

The final test set contains only **184 observations**.

Therefore, the final metrics should not be treated as universally
representative of future datasets.

### Feature Engineering Did Not Improve Validation Results

The engineered features did not improve validation performance in the
recorded experiment.

This demonstrates that feature engineering is not guaranteed to improve
a model.

### Validation/Test Selection Distinction

The validation comparison favored the original Random Forest, while the
final test evaluation used the engineered Random Forest.

This means the model-selection process must be interpreted carefully and
the two stages should not be presented as evidence that feature
engineering improved validation performance.

### Real-World Generalization

Additional validation on independent real-world datasets would be
required before considering any real-world application.

------------------------------------------------------------------------

## 22. Key Findings

The main findings of the project are:

1.  The dataset contains 918 observations and 12 variables.
2.  The target contains 508 positive cases and 410 negative cases.
3.  No missing values were detected during the initial data inspection.
4.  `MaxHR` showed the strongest negative linear correlation with the
    target among the numerical predictors.
5.  `Oldpeak` showed the strongest positive linear correlation among the
    numerical predictors.
6.  Random Forest outperformed Logistic Regression on the recorded
    validation comparison.
7.  Random Forest improved all five validation metrics compared with
    Logistic Regression.
8.  The largest validation improvement was in Recall.
9.  Five-fold cross-validation was used to examine model consistency.
10. Feature engineering created four additional numerical features.
11. The engineered models did not improve validation performance.
12. The final engineered Random Forest achieved 90.2% Accuracy and 94.2%
    ROC-AUC on the recorded test set.
13. The final model achieved 93.1% Recall for identifying the
    heart-disease class.
14. The model is an educational machine learning system and is not
    clinically validated.

------------------------------------------------------------------------

## 23. Conclusion

This project demonstrates a complete supervised machine learning
workflow for binary heart-disease classification.

The workflow begins with data inspection and exploratory analysis,
continues through preprocessing and model training, and ends with model
comparison, cross-validation, feature engineering, final test
evaluation, error analysis, and model export.

Random Forest was the strongest model in the original validation and
cross-validation comparisons.

Feature engineering was also tested, but the engineered feature set did
not improve validation performance.

The final test evaluation of the engineered Random Forest produced
strong recorded metrics, including:

-   **90.2% Accuracy**
-   **89.6% Precision**
-   **93.1% Recall**
-   **91.3% F1-Score**
-   **94.2% ROC-AUC**

The main methodological lesson is that adding engineered features does
not automatically improve model performance. Model selection should be
based on measured validation evidence, while final test performance
should be reported separately.

Because the dataset is synthetic and the model has not been clinically
validated, the results demonstrate a machine learning methodology rather
than a medical diagnostic capability.
