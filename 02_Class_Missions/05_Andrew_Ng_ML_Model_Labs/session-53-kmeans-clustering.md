# Session 53 — K-Means Clustering

**Class duration:** 75 minutes  
**Task family:** unsupervised clustering

## Required Mastery

Students must be able to:

1. identify `X` and explain why there is no training label `y`;
2. distinguish clustering from classification;
3. explain a centroid as the mean location of assigned points;
4. perform one assignment step and one centroid-update step by hand;
5. explain the K-means objective as reducing within-cluster squared distance;
6. explain why feature scaling changes clusters;
7. identify sensitivity to initialisation, outliers, non-spherical clusters, and the choice of `k`;
8. interpret clusters without inventing unsupported real-world meanings;
9. implement a baseline with scikit-learn and inspect cluster sizes and centres.

## Core Pattern

```text
choose k and initialise centroids
→ assign each point to the nearest centroid
→ recompute each centroid as a mean
→ repeat until assignments or objective stabilise
→ inspect stability and meaning
```

## 75-Minute Learning Cycle

| Time | Block | Required action |
|---:|---|---|
| 0–8 | Skill Warm-Up | distinguish clustering from classification in short scenarios |
| 8–15 | Talk Robin 1 | explain what a cluster label does and does not mean |
| 15–22 | Entry Check | calculate two Euclidean distances |
| 22–35 | Core Pattern | trace assignment and update steps |
| 35–53 | Guided Practice | complete one K-means iteration on a small 2D dataset |
| 53–67 | Independent Rebuild | run K-means on a new dataset with and without scaling |
| 67–75 | Talk Robin 2 + Evidence | defend `k`, scaling, and one limitation |

## Required Evidence

- task-recognition record;
- hand assignment/update calculation;
- scaled versus unscaled comparison;
- cluster-size and centroid table;
- one stability or limitation note;
- explanation avoiding unsupported cluster names.

## Gate

The student can identify an unlabeled grouping task, perform one K-means iteration, explain the role of scale and `k`, and state why cluster IDs are not known class labels.