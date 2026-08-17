# Day 2 - DBSCAN & Hierarchical Clustering 🌐🌳

## Overview

The second day of Week 5 focused on moving beyond K-Means to two alternative clustering approaches — DBSCAN and hierarchical clustering — and understanding when each one is the better fit for a dataset.

The goal was to understand the limitations of K-Means, learn how DBSCAN discovers clusters through density and flags outliers as noise, learn how to build and read a hierarchical clustering dendrogram, and develop judgment for choosing the right clustering method for a given dataset's shape.

---

## Topics Covered

### Why K-Means Isn't Always Enough

I learned that K-Means, despite being useful, comes with real limitations that motivate other approaches.

The topics included:

* Understanding that K-Means requires k to be chosen in advance.
* Learning that K-Means assumes clusters are round and similarly sized.
* Understanding that K-Means forces every point into a cluster, even clear outliers.
* Recognizing that irregularly shaped or noisy data can produce misleading K-Means results.

---

### DBSCAN: Density-Based Clustering

I learned how DBSCAN groups data based on density rather than distance to a centroid.

The topics included:

* Understanding that DBSCAN (Density-Based Spatial Clustering) groups points that are packed closely together.
* Learning that DBSCAN labels points in sparse regions as noise instead of forcing them into a cluster.
* Understanding that DBSCAN discovers the number of clusters automatically — no k required.
* Learning that DBSCAN can find arbitrarily shaped clusters, unlike K-Means.
* Using `DBSCAN()` with the `eps` and `min_samples` parameters, and `fit_predict()` to obtain cluster labels, where a label of `-1` marks noise/outlier points.

---

### DBSCAN Parameters: eps and min_samples

I learned how DBSCAN's two key parameters control its behavior.

The topics included:

* Understanding that `eps` controls how close two points must be to count as neighbors.
* Understanding that `min_samples` controls how many neighbors a point needs to start a dense cluster.
* Learning that DBSCAN is sensitive to the choice of `eps` and can struggle with clusters of varying density.

---

### Hierarchical Clustering and Dendrograms

I learned how hierarchical clustering builds a nested tree of clusters instead of a single flat partition.

The topics included:

* Understanding that hierarchical clustering starts with every point as its own cluster and repeatedly merges the two closest clusters until all points join one cluster.
* Learning that the result is visualized as a dendrogram, a tree diagram showing how clusters merge.
* Understanding that you can "cut" the dendrogram at any height to obtain any number of clusters.
* Learning that hierarchical clustering needs no k in advance and reveals the nested structure of the data.
* Using `linkage()` from `scipy.cluster.hierarchy` with a method such as `"ward"`, and `dendrogram()` to visualize the result.

---

### Choosing the Right Clustering Method

I learned how to match a clustering method to a dataset's characteristics.

The topics included:

* Understanding that K-Means works best for round, similarly-sized clusters when k is roughly known, but forces outliers into clusters and needs k in advance.
* Understanding that DBSCAN works best for irregular shapes and data with noise/outliers, but is sensitive to `eps` and struggles with varying densities.
* Understanding that hierarchical clustering works best when nested structure or a dendrogram view is wanted, but can be slow on very large datasets.

---

## Machine Learning Workflow

The workflow practiced during this day was:

**Dataset (from Day 1) → Run DBSCAN → Inspect Clusters & Noise Points → Build Hierarchical Dendrogram → Choose a Cut Height → Compare K-Means, DBSCAN & Hierarchical Results → Interpret Which Method Fits Best**

As with Day 1, no labels are used — each method discovers structure entirely from the shape and density of the data.

---

## Hands-On Lab: Comparing Clustering Methods

* **Step 1:** Run DBSCAN on the Day 1 dataset and report how many clusters and noise points it found.
* **Step 2:** Build a hierarchical clustering dendrogram and choose a cut height, noting the resulting cluster count.
* **Step 3:** Compare the K-Means, DBSCAN, and hierarchical results on the same data.
* **Step 4:** In a Markdown cell, state which method best fits this dataset's shape and why.

---

## Tools Used

* Python
* Scikit-learn (DBSCAN)
* SciPy (dendrogram)
* Matplotlib
* Jupyter Notebook

---

## Key Takeaways

By the end of this day, I learned why K-Means alone isn't enough for every dataset, and how DBSCAN and hierarchical clustering address its main weaknesses in different ways.

I understood that DBSCAN finds clusters through density, automatically determines the number of clusters, and explicitly separates out noise instead of forcing every point into a group. I also learned that hierarchical clustering builds a full nested tree of merges, visualized as a dendrogram, which can be cut at any height to produce a chosen number of clusters without needing k in advance.

These concepts round out the clustering toolkit from Day 1, giving me a framework for choosing between K-Means, DBSCAN, and hierarchical clustering based on a dataset's shape, size, and the presence of noise or outliers.
