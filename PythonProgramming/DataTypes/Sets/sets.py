# "set is an unordered collection of items
# every set element is unique. no duplicates

# create a set
# won't allow duplicates
set1 = {99, 2, 2, 23, 2, 90, 127}
print(set1)


# add an element (using add)
set1.add(44)
print(set1)


# add multiple elemends (using update)
set1.update([22, 89, 943])
print(set1)


# add a list and a set
set1.update([-45, 7], {88, 109})
print(set1)


# removing elements from sets
nums = {1, 44, -98, -98, -98, 23}
print(nums)

# remove using remove (if I try to remove -98 again with remove, I will be thrown an error)
nums.remove(-98)
print(nums)


# remove using discard
nums.discard(23)
print(nums)
nums.discard(23)  # wont throw me an error evrn though 23 is no longer in the set
print(nums)


# clear and pop methods
name = set('lebronjamesssssssssss')
print(name)

element = name.pop()

print(element)

print(name)

# clear my entire set
name.clear()
print(len(name))




# Set Operations 

# (using union or |)

s1 = {22, 33, 90}
s2 = {33, 77, 99, 102}

print(s1.union(s2))
# or
print(s1 | s2)

print(s1 | s2 == s1.union(s2))


# intersection (or &)
print(s1.intersection(s2))
print(s1 & s2)

print(s1 & s2 == s1.intersection(s2))

# difference (or -)
print(s1 - s2)
print(s2 - s1)

print(s1.difference(s2))


# symmetric difference of both (or ^)
not_overlapped = s1 ^ s2
print(not_overlapped)

print(s1.symmetric_difference(s2))
