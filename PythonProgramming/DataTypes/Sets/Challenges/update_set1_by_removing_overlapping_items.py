# 8) remove overlapping items from set1
# "Exercise 8: Update set1 by adding items from set2, except common items"

first = {10, 20, 30, 40, 50}
second = {30, 40, 50, 60, 70}

first.symmetric_difference_update(second)
print(first)
