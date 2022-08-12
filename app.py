def intersection(set1, set2):
    comb = set1 + set2
    set = []
    for i in comb:
        if (i in set1) and (i in set2):
            comb.remove(i)
            set.append(i)
    return set


def union(set1, set2):
    set = set1 + set2
    for i in set:
        if (i in set1) and (i in set2):
            set.remove(i)
    return set


def symmetric_difference(set1, set2):
	# set1 and set2 are lists
	# return the symmetric difference
    pass

print(intersection([1,2,3],[3,4,5]))