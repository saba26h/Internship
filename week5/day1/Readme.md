# Day 1 - Unsupervised Learning & K-Means 🤖📊

## Overview

The first day of Week 5 focused on understanding unsupervised learning and how the K-Means clustering algorithm discovers structure in data without any labels.

The goal was to understand how unsupervised learning differs from supervised learning, how K-Means partitions data through its centroid-assignment loop, how to choose the right number of clusters using the elbow method and the silhouette score, and why scaling matters before clustering.

---

## Topics Covered

### Supervised vs. Unsupervised Learning

I learned how unsupervised learning differs fundamentally from the supervised learning covered in Weeks 3-4.

The topics included:

* Understanding that supervised learning uses labeled data (X and y) to predict a known target.
* Understanding that unsupervised learning works with no labels at all (X only).
* Learning that the goal shifts from predicting a known answer to discovering hidden structure in the data.
* Understanding examples of unsupervised tasks: clustering, dimensionality reduction, anomaly detection.
* Learning that unsupervised evaluation has no ground truth to compare against — it relies on internal metrics and judgment instead.

---

### What Clustering Does

I learned the goal and intuition behind clustering as an unsupervised technique.

The topics included:

* Understanding that clustering groups data points so that points in the same group are similar to each other and different from points in other groups.
* Learning how clustering answers questions like "what natural customer segments exist?" without anyone predefining those segments.
* Understanding that, because there are no labels, the algorithm finds structure purely from the shape of the data.

---

### K-Means, Step by Step

I learned how the K-Means algorithm partitions data into a chosen number of clusters.

The topics included:

* Understanding that K-Means requires the number of clusters, k, to be chosen in advance.
* Learning the three-step loop: place k centroids at random, assign each point to its nearest centroid, then move each centroid to the mean position of its assigned points.
* Understanding that this assignment/update loop repeats until the centroids stop moving.
* Using `KMeans()` with `n_clusters`, `random_state`, and `n_init` to fit a model.
* Using `fit_predict()` to obtain cluster labels and `cluster_centers_` to inspect the final centroid positions.

---

### Choosing k: the Elbow Method

I learned how to use the elbow method to pick a reasonable value of k.

The topics included:

* Understanding that K-Means needs k chosen in advance, and the right k is rarely obvious.
* Running K-Means across a range of k values and recording each model's inertia (total within-cluster distance).
* Understanding that inertia always falls as k rises, but the rate of improvement drops sharply at the right k.
* Plotting inertia against k and reading the resulting "elbow" as the recommended k.

---

### Choosing k: the Silhouette Score

I learned how to use the silhouette score as a quantitative check to confirm the elbow.

The topics included:

* Understanding that the silhouette score measures how well each point sits inside its own cluster versus the nearest other cluster.
* Learning that the score ranges from -1 to +1, with a higher average score meaning better-defined clusters.
* Using `silhouette_score()` to compute this metric for a set of cluster labels.
* Comparing scores across candidate k values to make a data-driven choice alongside the elbow method.

---

### Scaling Before Clustering

I learned why feature scaling is essential before running K-Means.

The topics included:

* Understanding that K-Means clusters points based on distance.
* Learning that an unscaled large-range feature (like income) would dominate a small-range feature (like age) in the distance calculation.
* Applying the same `StandardScaler` discipline used in Week 4 before fitting K-Means.

---

## Machine Learning Workflow

The workflow practiced during this day was:

**Dataset → Scale Features → Run K-Means Across a Range of k → Elbow Method → Silhouette Score → Fit Final Model with Chosen k → Visualize & Interpret Clusters**

No labels are used at any point during training — the algorithm discovers structure entirely on its own.

---

## Hands-On Lab: K-Means Clustering

* **Step 1:** Load and scale a provided dataset (numeric features only) with `StandardScaler`.
* **Step 2:** Run K-Means for k from 1 to 10 and plot inertia to find the elbow.
* **Step 3:** Compute the silhouette score for the top two candidate k values and pick the best.
* **Step 4:** Fit the final K-Means model with the chosen k, and visualize the clusters on a 2D scatter plot.
* **Step 5:** Interpret what each cluster represents in a Markdown cell.

---

## Tools Used

* Python
* Scikit-learn
* Pandas
* Matplotlib
* Jupyter Notebook

---

## Key Takeaways

By the end of this day, I learned how unsupervised learning discovers structure in data that has no labels, and how K-Means specifically does this through a repeating centroid-assignment loop.

I understood that choosing k is not automatic — the elbow method gives a visual estimate, and the silhouette score gives a quantitative way to confirm or override that estimate. I also learned that scaling features before clustering is essential, since K-Means relies entirely on distance and an unscaled feature can dominate the result.

These concepts provide an important foundation for clustering, unsupervised pattern discovery, and evaluating models when there is no ground-truth label to check against.
