

# Algorithm 1 : iForest(X , t, ψ)
# Inputs: X - input data, t - number of trees, ψ - subsampling size
# Output: a set of t iTrees
def iForest(X, t, s):
    # Initialize Forest
    # for i = 1 to t do
    #       X ′ ← sample(X , ψ)
    #       Forest ← Forest ∪ iTree(X ′)
    #    end for
    # return Forest
    pass


# Algorithm 2 : iTree(X′)
# Inputs: X ′ - input data
# Output: an iTree
def iTree(X):
    # if X ′ cannot be divided then
    #   return exNode{Size ← |X ′|}
    # else
    #   let Q be a list of attributes in X ′
    #   randomly select an attribute q ∈ Q
    #   randomly select a split point p between the max and min values of attribute q in X ′
    #   Xl ← f ilter(X ′, q < p)
    #   Xr ← f ilter(X ′, q ≥ p)
    #   return inNode{Lef t ← iTree(Xl),
    #       Right ← iTree(Xr),
    #       SplitAtt ← q,
    #       SplitValue ← p}
    # end if
    pass



# Algorithm 3 : PathLength(x, T, hlim, e)
# Inputs : x - an instance, T - an iTree, hlim - height limit, e - current path length; to be initialized to zero when first called
# Output: path length of x
def PathLength(x, T, hlim, e):
    # if T is an external node or e ≥ hlim then
    #   return e + c(T.size) {c(.) is defined in Equation 1}
    # end if
    # a ← T.splitAtt
    # if xa < T.splitValue then
    #   return PathLength(x, T.lef t, hlim, e + 1)
    # else {xa ≥ T.splitValue}
    #   return PathLength(x, T.right, hlim, e + 1)
    # end if
    pass