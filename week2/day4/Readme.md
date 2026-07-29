# Day 4 - Exploratory Data Analysis (EDA) Part 1: Distributions & Outliers 📊

## Overview

The fourth day focused on understanding the importance of Exploratory Data Analysis (EDA) and how it helps in understanding datasets before applying Machine Learning models.

The goal was to learn how to explore data distributions, visualize numerical and categorical variables, detect outliers, and identify potential data quality issues using statistical visualization techniques.

---

## Topics Covered

### What EDA Is and Why It Comes First

I learned why Exploratory Data Analysis is an essential first step in any Machine Learning project.

The topics included:

* Understanding the purpose of EDA before building models.
* Learning how EDA helps discover patterns, relationships, and data problems.
* Understanding why poor data understanding can negatively affect model performance.

---

### Seaborn for Statistical Visualization

I learned how to use Seaborn as a powerful visualization library built on top of Matplotlib.

The topics included:

* Creating statistical visualizations using Seaborn.
* Working with Pandas DataFrames directly.
* Understanding how visualization helps interpret dataset behavior.
* Using different plots to analyze numerical and categorical variables.

---

### Univariate Analysis

I learned how to analyze one variable at a time to understand its distribution and characteristics.

The topics included:

* Performing univariate analysis on numerical variables.
* Understanding the distribution of features using visualizations.
* Using histograms to analyze the frequency and shape of numerical data.
* Using count plots to analyze categorical variables.

---

### Data Distribution Visualization

I learned how different plots reveal different aspects of the dataset.

The topics included:

* Creating histograms using `sns.histplot()` to understand numerical distributions.
* Creating box plots using `sns.boxplot()` to analyze spread and detect outliers.
* Creating count plots using `sns.countplot()` to analyze categorical frequencies.
* Creating KDE plots using `sns.kdeplot()` to visualize smooth data distributions.

---

### Outlier Detection Using IQR Method

I learned how to identify and analyze outliers using statistical methods.

The topics included:

* Understanding what outliers are and why they matter.
* Detecting outliers visually using box plots.
* Calculating the Interquartile Range (IQR).
* Finding lower and upper bounds for detecting abnormal values.
* Deciding whether to remove, transform, or keep detected outliers based on their meaning.

---

## Tools Used

* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib
* Jupyter Notebook
* VS Code

---

## Key Takeaways

By the end of this day, I learned how to perform Exploratory Data Analysis to understand datasets before applying Machine Learning algorithms.

I understood how visualization techniques help reveal data distributions, identify patterns, and detect possible problems such as missing values and outliers.

I also learned how the IQR method can be used to detect abnormal observations and make better decisions about data preprocessing.

These EDA techniques are essential for preparing high-quality datasets and building reliable Machine Learning models.
