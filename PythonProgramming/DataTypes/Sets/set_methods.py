# set methods

new_set = {99, 99, 99, 2, 3, -5, 89}
print(new_set)
print(type(new_set))


# 1) add - add elements to a set
new_set.add(44)
print(new_set)


# 2) add tuples to a set
new_set.add((7, 93))
print(new_set)


# 3) copy - returns a shallow copy
copy_set = new_set.copy()

copy_set.add(('this', 'is', 'a', 'tuple', 44))
print(copy_set)

print(new_set)


# 4) clear - remove all elements from a set
print(copy_set)
copy_set.clear()
print(copy_set)


# 5) difference - returns the different elements between sets (use .difference or -)
s1 = {5,9,10}
s2 = {5,9,12, 90}

print(s1.difference(s2))
print(s1 - s2)

print(s2 - s1)


# 6) difference_update - updates the first set to contain only the different values from second set (look at the difference in s1 between the difference_update call)

print(s1)
s1.difference_update(s2)

print(s1)


# 7) discard - takes a single element and removes it from a set (if it occurs)
coins = {'quarter', 'nickel', 'penny'}
print(coins)
coins.discard('penny')
coins.discard('dime') # not in the initial set
print(coins)


# 8) intersection - find the overlapping element in 2 sets
init_set = {1, 44, 9}
other_set = {33, 44, 7}

print(init_set.intersection(other_set))



# 9) intersection update - updates first set to be the intersection elements with the other set
init_set.intersection_update(other_set)
print(init_set)


# 11) isdisjoint - returns true if there are no overlapping elements between set 1 and set 2 (false if there are)
west_coast_states = {'CA', 'NV', 'OR'}
east_coast_states = {'CT', 'NY', 'MA'}

other_west_coast_states = {'OR', 'UT', 'CO'}

print(west_coast_states.isdisjoint(east_coast_states)) # should be true (no overlapping states here)

print(west_coast_states.isdisjoint(other_west_coast_states)) # should be false (OR is an overlap)



# 11) issubset - returns true if all elements in a set are present in another set
cities = {'New York', 'San Francisco', 'Chicago'}
cities2 = {'New York'}

print(cities2.issubset(cities))


# 12) pop - returns an arbitrary element from a set and returns it
random_city = cities.pop()
print(random_city)



# 13) symmetric_difference - returns the sym diff between two sets - can also use the ^ symbol
colors = {'blue', 'green', 'yellow'}
colors2 = {'blue', 'green', 'orange'}

print(colors.symmetric_difference(colors2)) # yellow and orange (non overlapping colors) 

print(colors.symmetric_difference(colors2) == colors ^ colors2) # true 



# 14) symmetric_difference_update - 'finds the symmetric difference of two sets and updates the set calling it.'
colors.symmetric_difference_update(colors2) # will make colors = {'yellow', 'orange'} (overlapping elements)

print(colors)



# 15) union - returns a new set with distinct elements from both sets (can also use the | symbol)
print(cities.union(cities2))

print(cities | cities2)

print(cities2 | cities == cities.union(cities2))




# 16) update - updates a set with new items from other iterables
batman_movies = {'The Dark Knight', 'The Dark Knight Rises'}
batman_movies.update(['Joker', 'Batman Begins'])
print(batman_movies)
