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

## Day 2 - DBSCAN & Hierarchical Clustering 🌐🌳

The second day focused on moving beyond K-Means to two alternative clustering approaches — DBSCAN and hierarchical clustering — and understanding when each one is the better fit for a dataset.

I learned the limitations of K-Means, how DBSCAN discovers clusters through density and flags outliers as noise, how to build and read a hierarchical clustering dendrogram, and how to choose the right clustering method for a given dataset's shape.

**Topics Covered:**

* Understanding the limitations of K-Means: needing k in advance, assuming round/similarly-sized clusters, and forcing every point into a cluster.
* Understanding DBSCAN as a density-based method that groups points packed closely together.
* Learning that DBSCAN labels points in sparse regions as noise instead of forcing them into a cluster.
* Understanding that DBSCAN discovers the number of clusters automatically and can find arbitrarily shaped clusters.
* Using `DBSCAN()` with `eps` and `min_samples`, and `fit_predict()` to obtain labels, where `-1` marks noise/outlier points.
* Understanding the roles of `eps` (neighbor distance) and `min_samples` (density threshold), and DBSCAN's sensitivity to `eps` and varying densities.
* Understanding hierarchical clustering: starting with every point as its own cluster and repeatedly merging the two closest until all points join one cluster.
* Learning how to read a dendrogram and "cut" it at a chosen height to obtain a chosen number of clusters.
* Using `linkage()` from `scipy.cluster.hierarchy` with a method such as `"ward"`, and `dendrogram()` to visualize the result.
* Comparing K-Means, DBSCAN, and hierarchical clustering, and matching each to the dataset shapes it handles best.
* Completing a hands-on lab: running DBSCAN and reporting clusters/noise points, building a dendrogram and choosing a cut height, comparing all three methods on the same data, and stating in Markdown which method best fits the dataset's shape.

---

# Week 5 Checklist ✅

## Day 1 - Unsupervised Learning & K-Means
* [x] A notebook demonstrating K-Means clustering with elbow-method and silhouette analysis, and interpreted clusters.

## Day 2 - DBSCAN & Hierarchical Clustering
* [x] A clustering-comparison notebook (K-Means vs. DBSCAN vs. hierarchical) with a method recommendation.

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
│   ├── DBSCAN___Hierarchical_Clustering.ipynb
│   └── Readme.md
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

During Day 2, I learned why K-Means alone isn't enough for every dataset, and built and compared DBSCAN and hierarchical clustering against it — running DBSCAN to detect density-based clusters and noise, and building a dendrogram to view the data's nested cluster structure.
