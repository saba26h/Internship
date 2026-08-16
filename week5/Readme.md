# Week 5 - Unsupervised Learning 🤖📊

## Overview

During the fifth week of the internship, I started learning about unsupervised learning — building models from data that has no labels.

The focus of this week is understanding how to cluster data using K-Means, DBSCAN, and hierarchical clustering, reduce high-dimensional data using PCA and t-SNE, detect anomalies in unlabeled data, and select a Phase 3 capstone project with a completed Sprint 1 plan.

Throughout this week, I will learn how to choose the number of clusters using the elbow method and the silhouette score, compare different clustering algorithms, interpret explained variance from PCA, visualize high-dimensional data with t-SNE, detect anomalies with Isolation Forest, and plan a full end-to-end capstone project.

---

# Completed Days

## Day 1 - Unsupervised Learning & K-Means 🤖📊

The first day focused on understanding unsupervised learning and how the K-Means clustering algorithm discovers structure in data that has no labels.

I learned how unsupervised learning differs from supervised learning, how K-Means partitions data through its centroid-assignment loop, how to choose the right number of clusters using the elbow method and the silhouette score, and why scaling matters before clustering.

**Topics Covered:**

* Understanding unsupervised learning and how it differs from supervised learning.
* Understanding that unsupervised learning works with no labels (X only) and aims to discover hidden structure.
* Understanding what clustering does and how it groups similar data points without predefined labels.
* Learning the K-Means algorithm: placing centroids, assigning points, and updating centroid positions.
* Using `KMeans()` with `n_clusters`, `random_state`, and `n_init`.
* Using `fit_predict()` to obtain cluster labels and `cluster_centers_` to inspect the final centroids.
* Understanding the elbow method: plotting inertia against k to find the "elbow".
* Understanding the silhouette score as a quantitative measure of cluster quality, ranging from -1 to +1.
* Comparing candidate k values using both the elbow method and the silhouette score.
* Understanding why features must be scaled with `StandardScaler` before clustering.
* Completing a hands-on lab: loading and scaling a dataset, running the elbow method, computing silhouette scores, fitting the final K-Means model, visualizing the clusters, and interpreting what each cluster represents.

---

# Week 5 Checklist ✅

## Day 1 - Unsupervised Learning & K-Means

* [x] A notebook demonstrating K-Means clustering with elbow-method and silhouette analysis, and interpreted clusters.

## Day 2 - DBSCAN & Hierarchical Clustering

* [ ] A clustering-comparison notebook (K-Means vs. DBSCAN vs. hierarchical) with a method recommendation.

## Day 3 - Dimensionality Reduction with PCA

* [ ] A PCA notebook with a cumulative explained-variance plot and a justified component count.

## Day 4 - t-SNE & Anomaly Detection

* [ ] A t-SNE and anomaly-detection notebook with a 2D visualization and Isolation Forest results.

## Day 5 - Phase 3 Project Selection & Sprint 1 Planning

* [ ] A signed-off Phase 3 project selection, problem statement, and Sprint 1 plan with backlog and acceptance criteria.

---

# Week 5 Folder Structure

```text
Week-5/
│
├── Day-1-Unsupervised-Learning-KMeans/
│   ├── kmeans_hands-on-lab.ipynb
│   ├── creditcard_45k.csv
│   └── Readme.md
│
├── Day-2-DBSCAN-Hierarchical-Clustering/
│
├── Day-3-Dimensionality-Reduction-PCA/
│
├── Day-4-tSNE-Anomaly-Detection/
│
├── Day-5-Phase3-Project-Selection-Sprint1-Planning/
│
└── Readme.md
```

---

# Week 5 Progress

During Day 1, I learned how unsupervised learning discovers structure in unlabeled data, and how to use K-Means with the elbow method and silhouette score to choose the right number of clusters.
