# 🫀 Cardiac Patient Monitoring System

## AI & Machine Learning Internship — Week 5, Day 5
### Project Planning & Continuation Roadmap

**Prepared by:** [Your Name]
**Program:** BinX Tech — AI & Machine Learning Internship
**Stage:** Phase 2 → Phase 3 Transition

---

## 1. Project Overview

The **Cardiac Patient Monitoring System** is the project I picked up in **Week 4** of the internship. The first three weeks covered the general foundations (Python/Pandas, statistics, EDA practice), but this specific project — the cardiac dataset, the cleaning, the EDA, the supervised models, the evaluation, the feature engineering, and the pipelines — was all built during Week 4. In Week 5 I extended that same project with the unsupervised learning stage.

So by Day 5, the project covers the full path:

**Raw Data → Cleaning → EDA → Supervised Models → Evaluation → Feature Engineering → Pipelines (Week 4) → Unsupervised Learning (Week 5) → Documentation**

The dataset and the goal haven't changed since Week 4 — only the techniques applied to it grew from one week to the next.

---

## 2. Problem Statement

> How can patient health and clinical characteristics be used to predict the presence of a cardiac condition, and can feature engineering improve the performance of machine learning models for this classification task?

Cardiovascular disease is a serious health concern, and flagging patients who may be at higher risk earlier can support better medical decisions. This project treats that as a binary classification problem (heart disease vs. no heart disease) and, in Week 5, also asks a second question that supervised learning alone can't answer: **does the data contain natural groupings, a lower-dimensional structure, or unusual patients that are worth a closer look — independent of the target label?**

---

## 3. Objective

* Understand and clean the cardiac dataset.
* Explore relationships between clinical features and the target.
* Build and compare supervised classification models.
* Evaluate models with consistent, appropriate metrics.
* Engineer additional features and test whether they help.
* Wrap preprocessing + modeling into reusable Scikit-learn pipelines.
* Tune hyperparameters and pick a final model using validation data only.
* Extend the analysis with **unsupervised learning**: clustering, dimensionality reduction, and anomaly detection — all done without touching the `HeartDisease` label during training.
* Document what was found, what it means, and what it doesn't mean.

---

## 4. Scope

**In scope:** Python, NumPy/Pandas, EDA, visualization, correlation analysis, supervised classification (Logistic Regression, Random Forest), train/validation/test splitting, cross-validation, classification metrics, feature engineering, Scikit-learn pipelines, hyperparameter tuning, K-Means, DBSCAN, hierarchical clustering, PCA, t-SNE, Isolation Forest, Git/GitHub.

**Out of scope:** clinical diagnosis or treatment advice, identifiable patient data, deep learning, MLOps/production deployment, techniques not covered in the curriculum.

---

## 5. Dataset

**Heart Disease Prediction Dataset** — 918 observations, 11 original input features, 1 binary target (`HeartDisease`: 0 = No Disease, 1 = Disease).

Features span numerical (Age, RestingBP, Cholesterol, MaxHR, Oldpeak), binary (FastingBS), and categorical (Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope) variables.

For the unsupervised stage specifically, only the numeric predictors were used (6 columns after preprocessing), since clustering, PCA, and t-SNE all rely on numeric distance/variance and shouldn't be fed the target label.

---

## 6. Data Quality Handling

Zero values in `RestingBP` and `Cholesterol` were identified as invalid rather than real measurements during EDA and were converted to missing values, then median-imputed **inside** the pipeline — not manually — so no information leaks from validation/test data into training. For the unsupervised stage, the same numeric features were re-checked for missing values before scaling; any gaps were filled with the median before clustering.

---

## 7. Summary of Week 4 (Already Completed)

This is where the Cardiac Patient Monitoring System actually started. Everything below was built in Week 4, in one continuous stretch, before the unsupervised extension in Week 5:

| Stage | What was done |
|---|---|
| Data understanding & cleaning | Loaded the dataset, identified invalid zero values in `RestingBP` and `Cholesterol`, converted them to missing and handled them via median imputation inside the pipeline |
| EDA | Studied distributions, correlations, and class balance across all features and the target |
| Supervised problem definition | Defined `HeartDisease` as the binary classification target, split train/validation/test with stratification |
| Model comparison | Trained and compared Logistic Regression vs. Random Forest, selected Random Forest based on validation performance |
| Feature engineering | Created 4 new features (`AgeGroup`, `HRReserve`, `HighBP`, `MaxHR_pct`) |
| Pipelines & tuning | Built Scikit-learn pipelines for both the original and engineered feature sets, tuned Random Forest with `GridSearchCV`, and selected the final model using the validation set, evaluating once on the held-out test set |

---

## 8. Week 5 — Unsupervised Learning Extension (This Week's Work)

All clustering/PCA/t-SNE work below was run on the **standardized numeric features only** (6 columns, missing values median-imputed first), completely independent of the target label.

### 8.1 Day 1 — K-Means Clustering

* Ran the elbow method across `k = 1..10` on the scaled numeric matrix.
* Compared silhouette scores for `k = 2..10` and took the two strongest candidates: **k = 3** (silhouette = 0.2138) and **k = 4** (silhouette = 0.2080).
* Selected **k = 3** as the final number of clusters (higher silhouette score, consistent with the elbow shape).
* Final cluster sizes: **361 / 206 / 351** patients.
* Visualized the 3 clusters on a 2D PCA projection (the clustering itself used all 6 scaled features; PCA here is only for plotting).

### 8.2 Day 2 — DBSCAN & Hierarchical Clustering

* Ran DBSCAN (`eps = 0.8`, `min_samples = 5`) on the same scaled features → found **8 density-based clusters** and flagged **459 points as noise** (roughly half the dataset), which shows the data doesn't separate into a small number of dense, well-defined regions the way DBSCAN expects.
* Built a Ward-linkage hierarchical clustering dendrogram, then cut the tree at **3 clusters** to match K-Means for a fair comparison.
* Compared all three methods side by side:

| Method | Clusters | Noise Points | Silhouette Score |
|---|---|---|---|
| K-Means | 3 | 0 | 0.2138 |
| DBSCAN | 8 | 459 | 0.0405 |
| Hierarchical | 3 | 0 | 0.1770 |

* **Conclusion:** K-Means gave the best-separated clusters for this dataset. DBSCAN's high noise count and low silhouette suggest the cardiac data doesn't have the tight, uneven-density groupings DBSCAN is best at finding — it's better suited to data with clearer density gaps.

### 8.3 Day 3 — PCA (Dimensionality Reduction)

* Fit a full PCA on the 6 scaled numeric features and plotted the cumulative explained variance.
* Reaching **~95%+ variance required all 6 components** (variance retained = 1.0 at 6 components) — since the numeric feature set is already small, there wasn't much redundancy left to compress out.
* For visualization purposes, a separate 2-component PCA was fit, retaining **46.93% of the variance** — useful for a 2D scatter plot, but a reminder that a lot of information is necessarily lost when squeezing 6 dimensions into 2.
* Plotted the 2D projection colored by the actual `HeartDisease` label (used only for visual reference, not for fitting PCA).

### 8.4 Day 4 — t-SNE & Anomaly Detection

* Ran t-SNE (`perplexity = 30`) on the same scaled features and compared it side-by-side with the PCA 2D plot, both colored by the K-Means cluster labels — t-SNE tends to show tighter, more separated groupings since it preserves local neighborhoods rather than global variance.
* Ran Isolation Forest with `contamination = 0.05`, flagging **46 out of 918 patients (≈5%)** as anomalies.
* Inspected the two most extreme flagged points (lowest isolation scores):

| Age | RestingBP | Cholesterol | FastingBS | MaxHR | Oldpeak |
|---|---|---|---|---|---|
| 58 | 132.0 | 458.0 | 1 | 69 | 1.0 |
| 56 | 200.0 | 288.0 | 1 | 133 | 4.0 |

* Both show unusual combinations (e.g. very high cholesterol with a low max heart rate; very high resting BP with a large Oldpeak) rather than a single extreme value — a reminder that "anomaly" here means statistically unusual, not necessarily a data error or a confirmed medical condition.

---

## 9. Day 5 — Project Planning Statement

Day 5 isn't a fresh project-selection day for me — the Cardiac Patient Monitoring System is already my ongoing project, so today is about documenting where it stands and what's left before Phase 3.

**Decision:** Continue the existing Cardiac Patient Monitoring System into Phase 3, rather than starting one of the six new capstone options from scratch.

---

## 10. Definition of Done

**Data**
- [x] Dataset included and documented
- [x] Target variable clearly defined
- [x] Data-quality issues identified and handled via pipeline
- [x] Preprocessing is reproducible

**Exploratory Analysis**
- [x] Descriptive statistics
- [x] Distribution and class-balance analysis
- [x] Correlation/relationship analysis
- [x] Meaningful visualizations

**Supervised Learning**
- [x] Classification problem clearly defined
- [x] Baseline + comparison classifiers
- [x] Consistent evaluation methodology + cross-validation
- [x] Confusion matrix, accuracy/precision/recall/F1/ROC-AUC reported

**Feature Engineering & Pipelines**
- [x] Engineered features documented (4 new features)
- [x] Scikit-learn pipelines for preprocessing + modeling
- [x] Hyperparameter tuning (GridSearchCV)
- [x] Final model selected on validation data only

**Unsupervised Learning**
- [x] K-Means with elbow + silhouette analysis
- [x] DBSCAN and hierarchical clustering, compared against K-Means
- [x] PCA with cumulative explained variance and component selection
- [x] t-SNE visualization compared with PCA
- [x] Isolation Forest anomaly detection with interpretation
- [x] Results interpreted, not just reported

**Documentation**
- [x] Notebook has clear Markdown explanations throughout
- [ ] README finalized (this file)
- [ ] Limitations section written up
- [ ] Final notebook re-run top to bottom for reproducibility
- [ ] Committed to GitHub

---

## 11. Remaining Backlog (Sprint Going Into Phase 3)

| ID | Task | Priority | Output |
|---|---|---|---|
| S1 | Write up limitations & interpretation notes | High | Final documentation section |
| S2 | Finalize and clean this README | High | Complete project overview |
| S3 | Re-run notebook top to bottom | High | Confirmed reproducibility |
| S4 | Commit and push to GitHub | High | Version-controlled project |
| S5 | Prepare short technical walkthrough | Medium | Demo-ready explanation |

---

## 12. Acceptance Criteria

* Every notebook cell runs without errors, top to bottom.
* Preprocessing lives inside pipelines — no manual leakage from val/test into train.
* Every result (cluster count, silhouette score, variance retained, anomaly count) is interpreted in Markdown, not left as a bare number.
* Method choices (e.g. why K-Means over DBSCAN here) are justified against the actual metrics, not assumed.
* README and notebook stay in sync with what was actually run.

---

## 13. GitHub Workflow

```text
Work on a task
      ↓
Run & validate notebook
      ↓
Document findings in Markdown
      ↓
Commit with a clear message
      ↓
Push to GitHub
```

---

## 14. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Data leakage during preprocessing | All learned transforms (scaling, imputation) live inside pipelines / are fit only on training data |
| Overfitting | Cross-validation + validation-based model selection + single held-out test evaluation |
| Misreading clustering results | Cross-checked K-Means against DBSCAN and hierarchical, used silhouette score rather than trusting one method alone |
| Treating anomalies as errors | Flagged points were inspected individually and described as "unusual," not automatically wrong |
| Scope creep | Kept the unsupervised stage limited to what Week 5 actually covers, tied back to the same cardiac dataset |

---

## 15. Current Status

| Area | Status |
|---|---|
| Data cleaning & EDA | ✅ Done |
| Supervised models & evaluation | ✅ Done |
| Feature engineering & pipelines | ✅ Done |
| Hyperparameter tuning & final model | ✅ Done |
| K-Means | ✅ Done — k=3, silhouette 0.2138 |
| DBSCAN | ✅ Done — 8 clusters, 459 noise points |
| Hierarchical clustering | ✅ Done — cut at 3 clusters |
| PCA | ✅ Done — 6 components for 95%+ variance, 2D view retains 46.93% |
| t-SNE | ✅ Done — compared against PCA |
| Anomaly detection | ✅ Done — 46/918 flagged, top 2 inspected |
| Final documentation & GitHub push | 🔄 In progress |

---

## 16. What's Next (Phase 3)

```text
Finish documentation & README
        ↓
Re-run notebook for reproducibility
        ↓
Push final version to GitHub
        ↓
Carry the cardiac project forward into Phase 3 sprints
```

---

## Final Note

This project has been built the same way since Week 4 — one dataset, one goal, with each new technique bolted on as it was taught. The unsupervised stage in Week 5 didn't replace the supervised work from Week 4; it answered a different question about the same patients: whether there's meaningful structure in the data beyond the labeled outcome. K-Means turned out to fit this dataset best among the three clustering methods tried, PCA showed the numeric features don't compress much further than they already are, and Isolation Forest flagged a small, plausible set of unusual patients worth a second look — not proven errors, just worth noting.
