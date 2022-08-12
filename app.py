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
    set = []
    for i in comb:
        if (i in set1) and (i not in set2):
            set.append(i)
        if (i in set2) and (i not in set1):
            set.append(i)
    return set