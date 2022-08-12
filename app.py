def intersection(set1, set2):
	# set1 and set2 are lists
	# return the intersection
    pass

# EASY WAY...
# def union(set1, set2):
#     ul = set1 + set2
#     result = set(ul)
#     return result

def union(set1, set2):
    ul = set1 + set2
    for i in ul:
        if (i in set1) and (i in set2):
            ul.remove(i)
    return ul

def symmetric_difference(set1, set2):
	# set1 and set2 are lists
	# return the symmetric difference
    pass

print(union(["a", "b", "c"], ["d", "e", "f"]))