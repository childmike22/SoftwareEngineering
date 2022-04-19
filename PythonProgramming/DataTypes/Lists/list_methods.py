# methods of lists in python (with examples!)

# 1) Append
# used to add an element(s) to the end of a list

sports = ['baseball', 'football', 'soccer']
sports.append('golf')

print(sports)

# apend a new list
other_sports = ['tennis', 'basketball']
sports.append(other_sports)
print(sports)



# 2) Extend
# used to add multiple other items to the end of a list
datatypes = ['list', 'tuple']
other_dtypes = ('string', 'int', 'float')

datatypes.extend(other_dtypes)
print(datatypes)
print(datatypes[3])

# Insert
# used to insert an element into a specified location
sodas = ['Coke', 'Pepsi', 'Fanta']
sodas.insert(1, 'Sprite')
print(sodas)


# 4) Remove
# remove a specific element from a list
# only removes the FIRST instance of it
cities = ['San Diego', 'San Francisco', 'Oakland', 'Los Angeles']
cities.remove('San Diego')

print(cities)

# 5) Count
colleges = ['UCLA', 'USC', 'Stanford', 'USC', 'USC', 'UCLA']
num_ucla = colleges.count('UCLA')
print(num_ucla)

# create a dictionary with counts of items in a list!
new_dict = {}
for item in colleges:
	if item in new_dict:
		new_dict[item] += 1
	else: 
		new_dict[item] = 1

print(new_dict)


# 6) Pop
# return and remove a specified item (if no position given, selects the last item in a list)
musicians = ['Jay Z', 'Drake', 'Taylor Swift', 'Billie Eilish']
print(musicians.pop())
print(musicians)

# remove and return a specified position
jayz = musicians.pop(0)
print(jayz)

print(musicians)



# 7) Reverse
# simply reverses the order of a list

new_list = ['now', 'normal', 'look', 'should', 'this']
new_list.reverse()
print(new_list)

# reverse order using slicing
systems = ['macOS', 'Windows', 'Linux']
systems_reverese = systems[::-1]
print(systems_reverese)

# access elements in reverse
for item in systems[::-1]:
	print(item)

# or

for item in reversed(systems):
	print(item)


# 8) Sort

# list of numbers
numbers = [77, 34, -90, 229, 221]
numbers.sort()
print(numbers)

#sort in descending
numbers.sort(reverse=True)
print(numbers)


names = ['ted', 'alexander', 'nancy', 'al', 'arthur']
print(names)

# sort alphabetically
names.sort()
print(names)

# sort based off length
names.sort(key=len)
print(names)


# 9) Copy (using copy)
orig_list = ['miguel', 24.5, 'apples', -88]
copy_list = orig_list.copy()
copy_list[0] = 'overwriting the first item'

print(orig_list)
print(copy_list)


# copy using shallow slicing
wine_list = ['red', 'white']
sliced_wine_list = wine_list[:]

sliced_wine_list.append('rose')
print(wine_list)
print(sliced_wine_list)


# copying using =. An option, but usually a bad idea
# changes on copied list will impact the original one 
list1 = [22, 99]
list2 = list1
list2.append('adding this')
print(list1)
print(list2)



# 9) clear
# removes all elements from a list

brands = ['nike', 'addidas', 'reebok']
brands.clear()
print(brands)


# empty a list using del
magic = ['now', 'its', 'gone']
del magic[:]
print(magic)
