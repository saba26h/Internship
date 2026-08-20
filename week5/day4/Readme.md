# Day 4 - t-SNE & Anomaly Detection 🔍📊

## Overview

The fourth day of Week 5 moved from dimensionality reduction with PCA into visualization with t-SNE and anomaly detection, focusing on how high-dimensional data can be explored through local structure and how unusual data points can be identified without requiring labeled examples.

The goal was to understand how t-SNE differs from PCA, why t-SNE is especially useful for visualizing local neighborhoods and revealing clusters, learn what anomaly detection is and why it is often unsupervised, understand how Isolation Forest identifies unusual points, and develop judgment for interpreting detected anomalies and the relationship between anomaly detection and clustering.

---

## Topics Covered

### t-SNE for Visualization

I learned how t-SNE (t-distributed Stochastic Neighbor Embedding) transforms high-dimensional data into a lower-dimensional representation designed mainly for visualization.

The topics included:

* Understanding that t-SNE focuses on preserving local neighborhoods rather than global variance.
* Learning that points that are close together in high-dimensional space are encouraged to remain close in the 2D representation.
* Understanding that t-SNE can reveal clusters visually, even when the original data is not linearly separable.
* Using `TSNE(n_components=2, perplexity=30, random_state=42)` to reduce high-dimensional data to two dimensions.
* Producing a 2D scatter plot and coloring points using known cluster labels when available.
* Understanding that t-SNE is mainly a visualization technique and should not normally be used as input features for a machine learning model.

---

### PCA vs. t-SNE

I learned the key differences between PCA and t-SNE and when each method is more appropriate.

The topics included:

* Understanding that PCA preserves global structure and variance, while t-SNE focuses on local neighborhoods.
* Learning that PCA can be used for both dimensionality reduction and visualization, while t-SNE is mainly intended for visualization.
* Understanding that PCA is generally faster and more suitable for large datasets.
* Learning that t-SNE can be computationally expensive, especially as the dataset grows.
* Recognizing that PCA components have meaningful directions based on combinations of the original features, while t-SNE axes do not have a direct interpretable meaning.
* Understanding that t-SNE results can change depending on parameters such as perplexity and random state.

| PCA                                      | t-SNE                                  |
| ---------------------------------------- | -------------------------------------- |
| Preserves global structure / variance    | Preserves local neighborhoods          |
| Compression + visualization              | Mainly visualization                   |
| Faster                                   | Slower on large datasets               |
| Components have interpretable directions | Axes have no meaningful interpretation |
| Useful for modeling and visualization    | Mainly useful for exploring structure  |

---

### What Anomaly Detection Is

I learned how anomaly detection identifies data points that differ significantly from the normal pattern of a dataset.

The topics included:

* Understanding that anomalies are observations that behave differently from the majority of the data.
* Learning that anomaly detection can be used for applications such as fraud detection, system failures, defects, and unusual behavior.
* Understanding why anomaly detection is often unsupervised.
* Recognizing that anomalies are usually rare and therefore often do not have reliable labels.
* Learning that an anomaly detection model can learn the general pattern of normal observations and identify points that deviate from it.
* Connecting anomaly detection to the fraud-detection capstone project option from the course outline.

---

### Isolation Forest

I learned how Isolation Forest detects anomalies by measuring how easily individual points can be separated from the rest of the dataset.

The topics included:

* Understanding that anomalies are often easier to isolate because they are located away from dense groups of normal observations.
* Learning that Isolation Forest randomly partitions the data and measures how quickly points become isolated.
* Understanding that points requiring fewer splits to become isolated are more likely to be anomalies.
* Using `IsolationForest(contamination=0.05, random_state=42)` to detect unusual observations.
* Learning that `fit_predict()` returns `-1` for anomalies and `1` for normal observations.
* Understanding the `contamination` parameter as an estimate of the expected fraction of anomalies in the dataset.

---

### Anomaly Detection and Clustering

I learned how anomaly detection connects to the clustering techniques covered earlier in Week 5.

The topics included:

* Understanding that clustering and anomaly detection can both identify unusual or isolated observations.
* Recognizing that DBSCAN's noise points can be viewed as a simple form of anomaly detection.
* Understanding that DBSCAN identifies points that do not belong to dense regions, while Isolation Forest isolates unusual points through random partitioning.
* Learning that different unsupervised techniques can identify different types of unusual structure.
* Connecting the anomaly detection results back to the clusters and structure explored during the previous days.

---

## Machine Learning Workflow

The workflow practiced during this day was:

**High-Dimensional Dataset → Apply t-SNE to 2D → Visualize Local Structure → Compare with PCA → Run Isolation Forest → Identify Anomalies → Count Flagged Points → Inspect Selected Anomalies → Hypothesize Why They Were Flagged → Document Findings**

The goal throughout was to use t-SNE to understand the structure of high-dimensional data visually, while using Isolation Forest to identify observations that behave differently from the normal pattern.

---

## Hands-On Lab: Visualization & Anomaly Detection

* **Step 1:** Apply t-SNE to reduce a high-dimensional dataset to 2D and create a scatter plot, coloring points by cluster when labels are available.
* **Step 2:** Compare the t-SNE visualization with the PCA visualization from Day 3 and document what each method reveals about the data.
* **Step 3:** Run Isolation Forest on the dataset using an appropriate `contamination` value.
* **Step 4:** Count and report how many observations were flagged as anomalies.
* **Step 5:** Inspect two flagged observations and examine their feature values to hypothesize why they were identified as anomalies.
* **Step 6:** Document the findings in Markdown, including the difference between t-SNE and PCA and the interpretation of the detected anomalies.

---

## Tools Used

* Python
* Scikit-learn (`TSNE`, `IsolationForest`)
* Matplotlib
* Jupyter Notebook

---

## Key Takeaways

By the end of this day, I learned how t-SNE provides a different perspective on high-dimensional data by focusing on local neighborhoods rather than preserving global variance like PCA.

I understood that t-SNE is mainly a visualization tool, that its axes do not have meaningful interpretations, and that its results can change depending on parameters such as perplexity and random state. I also learned that PCA is generally more appropriate when dimensionality reduction is needed for modeling, while t-SNE is better suited for visually exploring local structure and possible clusters.

I also learned the purpose of anomaly detection and why it is often unsupervised, since unusual observations are usually rare and not pre-labeled. Using Isolation Forest, I learned how anomalies can be detected based on how quickly they can be isolated from the rest of the data, and how the `contamination` parameter controls the expected proportion of anomalies.

These concepts extend the toolkit from the previous days: where clustering identifies groups of similar observations and PCA reduces dimensionality while preserving global variance, t-SNE helps visualize local structure and Isolation Forest identifies observations that do not fit the normal pattern. Together, these unsupervised techniques provide different ways to explore, visualize, and understand high-dimensional datasets.
