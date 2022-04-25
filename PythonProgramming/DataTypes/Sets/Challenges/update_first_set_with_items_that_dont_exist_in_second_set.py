# 4) Update the first set with items that don't exist in the second set
# difference update method works here!

s1 = {10, 20, 30}
s2 = {20, 40, 50}

s1.difference_update(s2)
print(s1)
