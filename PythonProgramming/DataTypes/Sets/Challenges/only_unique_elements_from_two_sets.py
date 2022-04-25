# 3) Get only unique items from 2 sets
# "Write a Python program to return a new set with unique items from both sets by removing duplicates."
# can use union or set (s1 or s2)
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

combo_set = set(set1 | set2)
# also works: print(set1.union(set2))
print(combo_set)
