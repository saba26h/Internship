# Day 3 - Dimensionality Reduction with PCA 🔻📉

## Overview

The third day of Week 5 moved from clustering into dimensionality reduction, focusing on Principal Component Analysis (PCA) as a way to compress a high-dimensional dataset into a much smaller set of features while keeping as much of the original information as possible.

The goal was to understand the curse of dimensionality and why it makes high-dimensional data harder to work with, learn how PCA finds new axes that capture the most variance in the data, learn how to read the explained variance ratio to judge how much information is retained, and develop judgment for deciding how many components to keep and when PCA is (or isn't) the right tool.

---

## Topics Covered

### The Curse of Dimensionality

I learned that as the number of features in a dataset grows, several real problems start to appear.

The topics included:

* Understanding that real datasets often have dozens or hundreds of features.
* Learning that high dimensionality makes data sparse, since the same number of samples has to cover a much larger space.
* Understanding that distances between points lose meaning as dimensionality increases.
* Recognizing that models overfit more easily when there are too many features relative to the data.
* Learning that data cannot be visualized directly beyond three dimensions.

---

### What PCA Does

I learned how PCA finds new axes, called principal components, that capture the directions of greatest variance in the data.

The topics included:

* Understanding that the first principal component captures the most variance in the data.
* Learning that each following component captures the next most variance, at a right angle to the ones before it.
* Understanding that keeping only the first few components reduces dimensionality while retaining most of the information.
* Learning that each component is a combination of the original features, built on the same linear-algebra operations from Week 2.
* Using `StandardScaler` to scale the data and `PCA(n_components=...)` with `fit_transform()` to produce the reduced representation.

---

### Explained Variance Ratio

I learned how to measure exactly how much information PCA keeps after reduction.

The topics included:

* Understanding that the explained variance ratio shows how much of the data's total information each component keeps.
* Learning that summing the explained variance ratios of the kept components tells you how much information was retained overall.
* Understanding that PCA requires scaled data, since it is variance-based and an unscaled high-range feature would otherwise appear artificially important.
* Using `pca.explained_variance_ratio_` for the per-component values and `.sum()` for the total variance retained.

---

### Choosing the Number of Components

I learned how to decide, in a principled way, how many components to keep.

The topics included:

* Understanding that the number of components is a trade-off between how much dimensionality is reduced and how much information is kept.
* Learning that a common rule of thumb is to keep enough components to retain about 95% of the total variance.
* Understanding that plotting cumulative explained variance against the number of components makes this choice visual and easy to justify.

---

### When (and When Not) to Use PCA

I learned what PCA is useful for, and what it costs.

The topics included:

* Understanding that PCA can compress features to speed up and stabilize downstream models.
* Learning that PCA can reduce overfitting by removing redundant or correlated features.
* Understanding that PCA can reduce data to 2D or 3D so it can be plotted and inspected visually.
* Recognizing the trade-off that the new components are combinations of features, so they lose the direct interpretability the original columns had.

---

## Machine Learning Workflow

The workflow practiced during this day was:

**High-Dimensional Dataset → Scale with StandardScaler → Fit PCA on All Components → Plot Cumulative Explained Variance → Choose Number of Components for ~95% Variance → Reduce to 2 Components → Visualize & Color by Known Group → Document What Was Preserved and What Was Lost**

As with the PCA method itself, the goal throughout was to keep as much of the original signal as possible while working with far fewer dimensions.

---

## Hands-On Lab: Reducing Dimensions with PCA

* **Step 1:** Scale a high-dimensional provided dataset with `StandardScaler`.
* **Step 2:** Fit PCA and plot the cumulative explained variance against the number of components.
* **Step 3:** Choose the number of components that retains ~95% of the variance and justify it.
* **Step 4:** Reduce the data to 2 components and produce a 2D scatter plot, coloring points by a known group if available.
* **Step 5:** Document what the reduction preserved and what it cost in Markdown.

---

## Tools Used

* Python
* Scikit-learn (PCA)
* StandardScaler
* Matplotlib
* Jupyter Notebook

---

## Key Takeaways

By the end of this day, I learned why high-dimensional data is hard to work with, and how PCA addresses that by finding a small number of new axes that capture most of the variance in the original features.

I understood that PCA requires scaled data to work correctly, that the explained variance ratio is the key number for judging how much information is retained, and that the choice of how many components to keep is a deliberate trade-off, guided by rules like the 95% variance threshold rather than an arbitrary pick. I also learned that reducing data down to 2 components is mainly a visualization tool, useful for inspecting structure and known groupings, even though it retains far less variance than the component count chosen for modeling.

These concepts extend the toolkit from Day 1 and Day 2: where clustering methods find structure in the data as it is, PCA changes the representation of the data itself, which is often a useful step before or alongside clustering and modeling on high-dimensional data.
