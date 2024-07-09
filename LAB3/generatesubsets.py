def generate_subsets(n):
    subsets = []
    for i in range(2**n): 
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(j)
        subsets.append(subset)
    return subsets