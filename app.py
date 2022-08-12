def intersection(set1, set2):
    comb = set1 + set2
    set = []
    for i in comb:
        if (i in set1) and (i in set2):
            comb.remove(i)
            set.append(i)
    return set


def union(set1, set2):
    comb = set1 + set2
    for i in comb:
        if (i in set1) and (i in set2):
            comb.remove(i)
    set = comb
    return set


def symmetric_difference(set1, set2):
    comb = set1 + set2
    xor = [i for i in comb if not ((i in set1) and (i in set2))]
    return xor

print(symmetric_difference([1,2,3],[3,4,5]))