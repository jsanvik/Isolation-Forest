import random
import numpy as np
import pandas as pd

# In the training stage, iTrees are constructed by recursively partitioning a subsample X′ until all instances are isolated. 
# Each iTree is constructed using a subsample X′ randomly selected without replacement from X , X′ ⊂ X


# Algorithm 1 : iForest(X , t, ψ)
# Inputs: X - input data (pandas DataFrame), t - number of trees (int), ψ - subsampling size (int)
# Output: a set of t iTrees
def iForest(X, t = 100, s = 256): # Paper uses default 100 trees and 2^8 subsampling size
    forest = {} # Initialize Forest (list of t iTrees)
    for i in range(t):
        x = X.sample(s) # X′ ← sample(X , ψ)
        forest = forest.add(iTree(x)) # Forest ← Forest ∪ iTree(X ′)
    return forest


# Algorithm 2 : iTree(X′)
# Inputs: X ′ - input data
# Output: an iTree
def iTree(X):
    if len(X.index) <= 1: # if X′ cannot be divided then
        # return exNode{Size ← |X′|}
        return exNode{Size ← |X|} #TODO: What does this mean?
    else:
        # let Q be a list of attributes in X′
        # randomly select an attribute q ∈ Q
        q = random.choice(X.columns.to_list())
        # randomly select a split point p between the max and min values of attribute q in X′
        p = random.randrange(X[q].min(), X[q].max())
        Xl = X[X[q] <= p] # Xl ← filter(X′, q < p)
        Xr = X[X[q] > p] # Xr ← filter(X′, q ≥ p)

        iTreeDict = {
                "left": Xl, 
                "right": Xr, 
                "splitAtt": q,
                "splitValue": p
                }
        return iTreeDict



# Algorithm 3 : PathLength(x, T, hlim, e)
# Inputs : x - an instance, T - an iTree, hlim - height limit, e - current path length; to be initialized to zero when first called
# Output: path length of x
def PathLength(x, T, hlim, e):
    # if T is an external node or e ≥ hlim then
    #   return e + c(T.size) {c(.) is defined in Equation 1}
    # end if
    # a ← T.splitAtt
    # if xa < T.splitValue then
    #   return PathLength(x, T.left, hlim, e + 1)
    # else {xa ≥ T.splitValue}
    #   return PathLength(x, T.right, hlim, e + 1)
    # end if
    pass