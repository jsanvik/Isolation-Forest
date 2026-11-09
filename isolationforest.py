import random
import numpy as np
import pandas as pd
import math
import statistics
from pathlib import Path
import os

# In the training stage, iTrees are constructed by recursively partitioning a subsample X′ until all instances are isolated. 
# Each iTree is constructed using a subsample X′ randomly selected without replacement from X , X′ ⊂ X


# Algorithm 1 : iForest(X , t, ψ)
# Inputs: X - input data (pandas DataFrame), t - number of trees (int), ψ - subsampling size (int)
# Output: a set of t iTrees
def iForest(X, t = 100, s = 2**8): # Paper uses default 100 trees and 2^8 subsampling size
    forest = [] # Initialize Forest (list of t iTrees)
    for i in range(t):
        x = X.sample(s) # X′ ← sample(X , ψ)
        forest.append(iTree(x)) # Forest ← Forest ∪ iTree(X ′)
    return forest


# Algorithm 2 : iTree(X′)
# Inputs: X ′ - input data
# Output: an iTree
def iTree(X):
    if len(X.index) <= 1: # if X′ cannot be divided then
        # return exNode{Size ← |X′|}
        return {
            "type": "external",
            "size": len(X)}
    else:
        # let Q be a list of attributes in X′
        # randomly select an attribute q ∈ Q
        q = random.choice(X.columns.to_list())
        # randomly select a split point p between the max and min values of attribute q in X′
        p = random.uniform(X[q].min(), X[q].max())
        Xl = X[X[q] < p] # Xl ← filter(X′, q < p)
        Xr = X[X[q] >= p] # Xr ← filter(X′, q ≥ p)

        iTreeDict = {
                "type": "internal",
                "left": iTree(Xl), 
                "right": iTree(Xr), 
                "splitAtt": str(q),
                "splitValue": p
                }
        return iTreeDict



# Algorithm 3 : PathLength(x, T, hlim, e)
# Inputs : x - an instance, T - an iTree, hlim - height limit, e - current path length; to be initialized to zero when first called
# Output: path length of x
def PathLength(x, T, hlim, e = 0): # Current path length to be initialized to zero when first called
    # if T is an external node or e ≥ hlim then
    if T["type"] == "external" or e >= hlim:
        return e + c(T["size"])
    #   return e + c(T.size) {c(.) is defined in Equation 1} (Need to implement c(.))
    # end if
    # a ← T.splitAtt
    a = T["splitAtt"]
    # if xa < T.splitValue then

    if x[a] < T["splitValue"]:
        return PathLength(x, T["left"], hlim, e + 1)
    #return PathLength(x, T.left, hlim, e + 1)
    # else {xa ≥ T.splitValue}
    else:
        return PathLength(x, T["right"], hlim, e + 1)
    #   return PathLength(x, T.right, hlim, e + 1)
    # end 

# c(.) from equation 1
def c(n):
    if n > 2:
        H = np.log(n - 1) + 0.5772156649
        return 2 * H - (2 * (n - 1) / n)
    elif n == 2:
        return 1
    else:
        return 0

# The anomaly score s of an instance x is defined as:
# s(x, ψ) = 2 ** ( -(E(h(x))/c(ψ)) )
# where E(h(x)) is the average of h(x) from a collection of iTrees.

# Inputs: X - an instance (Pandas Dataframe) T - collection of iTrees (list) (int) ψ (s) - subsampling size (int)
def anomaly_score(x, T, s = 2**8):
    # E(h(x)) is the average of h(x) from a collection of iTrees.
    e = statistics.mean([PathLength(x, T, hlim) for T in forest]) # E(h(x)) is the average h(x) from a collection of itrees
    return 2 ** (-e/c(s))

if __name__ == "__main__":

    RANDOM_SEED = 4660

    # Set random seed
    random.seed(RANDOM_SEED)

    # Read in dataset
    dataset = "wood" # options: "hbk", "wood"
    directory = Path.home()/"Downloads"

    data = pd.read_csv(directory / f"{dataset}.csv", index_col=0)
    hlim = 1000 # TODO: What tree height limit should be chosen?
    
    anomaly_threshold = 0.53 # TODO: What anomaly threshold should be chosen?

    # (i) If instances return s very close to 1, then they are definitely anomalies,
    # (ii) If instances have s much smaller than 0.5, then they are quite safe to be regarded as normal instances, and
    # (iii) If all the instances return s ≈ 0.5, then the entire sample does not really have any distinct anomaly.

    # Build forest
    forest = iForest(data, s=2**3) # 100 trees, 2^3 sampling size (default 2^8 too large for our datasets)

    # Get anomaly scores for points
    anomaly_scores = [] # List of all anomaly scores (to be added to DataFrame)
    for index, x in data.iterrows():
        # print(x)
        x = pd.Series(x, index=data.columns)
        score = anomaly_score(x, forest, s=2**3)
        anomaly_scores.append(score)

    anomalies = [1 if score >= anomaly_threshold else 0 for score in anomaly_scores] # 1 if anomaly else 0 (to be added to DataFrame)
    
    data["Anomaly Score"] = anomaly_scores
    data["Anomaly_pred"] = anomalies

    # Known actual anomalies
    if dataset == "wood": # [4, 6, 8, 19]
        data["Anomaly_actual"] = [1 if i+1 in [4, 6, 8, 19] else 0 for i, score in enumerate(anomaly_scores)]
    elif dataset == "hbk": # First 14 observations are anomalies
        data["Anomaly_actual"] = [1 if i+1 in list(range(1, 15)) else 0 for i, score in enumerate(anomaly_scores)]
        
    print("ANOMALY SCORES:")
    
    for idx, row in data.iterrows():
        print(idx, row["Anomaly Score"])

    print(data)
    print("Predicted anomalies:", data[data["Anomaly_pred"] == 1].index.to_list())
    print("Actual anomalies:", data[data["Anomaly_actual"] == 1].index.to_list())


    print("\n","END OF PROGRAM")