# Week 5 - Unsupervised Learning 🤖📊

## Overview

During the fifth week of the internship, I started learning about unsupervised learning — building models from data that has no labels.

The focus of this week is understanding how to cluster data using K-Means, DBSCAN, and hierarchical clustering, reduce high-dimensional data using PCA and t-SNE, detect anomalies in unlabeled data, and select a Phase 3 capstone project with a completed Sprint 1 plan.

Throughout this week, I learned how to choose the number of clusters using the elbow method and the silhouette score, compare different clustering algorithms, interpret explained variance from PCA, visualize high-dimensional data with t-SNE, detect anomalies with Isolation Forest, and plan a full end-to-end capstone project.

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

## Day 3 - Dimensionality Reduction with PCA 🔻📉

The third day focused on moving from clustering into dimensionality reduction, using Principal Component Analysis (PCA) to compress a high-dimensional dataset into a much smaller set of features while keeping as much of the original information as possible.

I learned the curse of dimensionality and why it makes high-dimensional data harder to work with, how PCA finds new axes that capture the most variance in the data, how to read the explained variance ratio to judge how much information is retained, and how to decide how many components to keep and when PCA is (or isn't) the right tool.

**Topics Covered:**

* Understanding that real datasets often have dozens or hundreds of features, and that high dimensionality makes data sparse, makes distances lose meaning, and makes models overfit more easily.
* Understanding that data cannot be visualized directly beyond three dimensions, which is one of the reasons dimensionality reduction is useful.
* Understanding that PCA finds new axes, called principal components, that capture the directions of greatest variance in the data.
* Learning that the first component captures the most variance, each following component captures the next most at a right angle to the ones before it, and each component is a combination of the original features, built on the same linear-algebra operations from Week 2.
* Using `StandardScaler` to scale the data and `PCA(n_components=...)` with `fit_transform()` to produce the reduced representation.
* Understanding the explained variance ratio: how much of the data's total information each component keeps, and that summing it over the kept components gives the total variance retained.
* Understanding that PCA requires scaled data, since it is variance-based and an unscaled high-range feature would otherwise appear artificially important.
* Using `pca.explained_variance_ratio_` for the per-component values and `.sum()` for the total variance retained.
* Understanding how to choose the number of components by plotting cumulative explained variance against the number of components, and using a threshold such as ~95% variance to justify the choice.
* Understanding PCA's three main uses — compressing features, reducing overfitting, and reducing data to 2D/3D for plotting — and the trade-off that the new components lose the direct interpretability of the original columns.
* Completing a hands-on lab: scaling a high-dimensional dataset, plotting cumulative explained variance, choosing and justifying a component count for ~95% variance, reducing the data to 2 components for a colored 2D scatter plot, and documenting in Markdown what the reduction preserved and what it cost.

---

## Day 4 - t-SNE & Anomaly Detection 🔍🌲

The fourth day focused on visualizing high-dimensional data with t-SNE and detecting unusual observations with Isolation Forest, closing out the unsupervised learning portion of Week 5.

I learned how t-SNE differs from PCA by preserving local neighborhoods instead of global variance, why its axes carry no direct meaning and are only useful for visual inspection, what anomaly detection is and why it is usually unsupervised, and how Isolation Forest flags anomalies by measuring how quickly a point can be isolated from the rest of the data.

**Topics Covered:**

* Understanding t-SNE as a dimensionality-reduction technique built specifically for visualization, rather than for feeding into a model.
* Understanding that t-SNE preserves local neighborhoods, keeping points that were close together in high dimensions close together in 2D, unlike PCA which preserves global variance.
* Using `TSNE(n_components=2, perplexity=...)` with `fit_transform()` to produce a 2D embedding.
* Comparing PCA and t-SNE side by side: PCA is fast and its components have interpretable directions; t-SNE is slower and its axes only reflect relative position, not a fixed meaning.
* Understanding that t-SNE's output changes with its settings and is meant for looking at the data, not for downstream modeling.
* Understanding anomaly detection as finding points that differ significantly from the norm, and why it is often unsupervised since anomalies are rare and rarely pre-labeled.
* Learning the Isolation Forest algorithm: anomalies are easier to isolate than normal points because they sit apart from the dense mass of the data, so fewer random partitions are needed to isolate them.
* Using `IsolationForest(contamination=...)` with `fit_predict()`, where `-1` marks an anomaly and `1` marks a normal point.
* Understanding the `contamination` parameter as an estimate of the expected fraction of anomalies, and how DBSCAN's noise points (Day 2) are a related, simpler form of anomaly detection.
* Completing a hands-on lab: reducing a high-dimensional dataset to 2D with t-SNE and plotting it by cluster, comparing the t-SNE plot with the Day 3 PCA plot, running Isolation Forest and reporting the number of flagged points, and inspecting two flagged points to hypothesize why they were flagged.

---

## Day 5 - Phase 3 Project Selection & Sprint 1 Planning 🚀

The fifth and final day of Week 5 shifted from technique to planning: choosing my Phase 3 capstone project and setting up its first sprint before Phase 3 begins.

I learned what Phase 3 involves, reviewed the six possible capstone project types, and went through what the "Definition of Done" and Sprint 1 planning actually require before any new work starts.

**Topics Covered:**

* Understanding Phase 3 as the applied core of the program: one complete AI/ML project built end-to-end, from raw data to a deployed product, across four one-week sprints.
* Reviewing the six capstone project options (Customer Churn Prediction, House Price Prediction, Sentiment Analysis Tool, Image Classifier, Recommendation System, Fraud Detection Model) and what each one involves.
* Understanding the professional baseline every capstone must meet: a documented notebook covering EDA → preprocessing → modeling → evaluation, a trained model with reported metrics, a working deployment, a clean GitHub repo, and a short technical write-up.
* Understanding Sprint 1 planning: choosing the first backlog tasks (dataset selection, EDA, baseline model), estimating effort, and setting a clear sprint goal.
* Understanding that every backlog task needs written acceptance criteria before work starts — the notebook runs without errors, work is committed to the right feature branch, a pull request is opened for review, results are documented, and metrics are compared to the baseline.

Since the Cardiac Patient Monitoring System is already my ongoing project — started in Week 4 and extended with unsupervised learning in Week 5 — I used Day 5 to formally continue that same project into Phase 3, rather than picking one of the six new capstone options. I restated the project's problem statement and Definition of Done, and wrote a Sprint 1 backlog covering the remaining documentation and cleanup tasks before the project moves into Phase 3.

---

# Week 5 Checklist ✅

## Day 1 - Unsupervised Learning & K-Means
* [x] A notebook demonstrating K-Means clustering with elbow-method and silhouette analysis, and interpreted clusters.

## Day 2 - DBSCAN & Hierarchical Clustering
* [x] A clustering-comparison notebook (K-Means vs. DBSCAN vs. hierarchical) with a method recommendation.

## Day 3 - Dimensionality Reduction with PCA
* [x] A PCA notebook with a cumulative explained-variance plot and a justified component count.

## Day 4 - t-SNE & Anomaly Detection
* [x] A t-SNE and anomaly-detection notebook with a 2D visualization and Isolation Forest results.

## Day 5 - Phase 3 Project Selection & Sprint 1 Planning
* [x] A signed-off Phase 3 project selection, problem statement, and Sprint 1 plan with backlog and acceptance criteria.

---

# Week 5 Folder Structure

```text
week5/
│
├── day1/
│   ├── kmeans_hands-on-lab.ipynb
│   ├── creditcard_45k.csv
│   └── Readme.md
│
├── day2/
│   ├── DBSCAN___Hierarchical_Clustering.ipynb
│   └── Readme.md
│
├── day3/
│   ├── PCA_hands_on_lab.ipynb
│   └── Readme.md
│
├── day4/
│   ├── Day4_tSNE_Anomaly_Detection.ipynb
│   └── Readme.md
│
├── day5/
│   └── Readme.md
│
└── Readme.md
```

---

# Week 5 Progress

During Day 1, I learned how unsupervised learning discovers structure in unlabeled data.
I used K-Means with the elbow method and silhouette score to choose the right number of clusters.

During Day 2, I learned why K-Means alone isn't enough for every dataset.
I built and compared DBSCAN and hierarchical clustering against it, detecting density-based clusters/noise and reading a dendrogram.

During Day 3, I learned why high-dimensional data is hard to work with and how PCA addresses that.
I scaled the data, chose a component count for ~95% variance, and reduced it to 2 components to visualize it.

During Day 4, I learned how t-SNE reveals local structure that PCA can miss, and used it alongside Isolation Forest to flag unusual observations in the data.

During Day 5, I closed out Phase 2 by formally continuing the Cardiac Patient Monitoring System into Phase 3, writing out its Sprint 1 backlog and acceptance criteria.
