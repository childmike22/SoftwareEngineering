# Dictionary
# "unordered collection of key value pairs"
# commonly used when we have enormous amounts of data 

# basic creation
dict1 = {'key': 'value'}
print(type(dict1))
print(dict1.items())


team_abbr = {'GSW': 'Golden State Warriors', 
'ATL': 'Atlanta Hawks', 
'LAL': 'Los Angeles Lakers', 
'NYK': 'New York Knicks'}

# accessing elements
print(team_abbr['LAL'])


# access elemts using .get()
print(team_abbr.get('LSW', 'Not Found'))


# changing elements
team_abbr['GSW'] = 'I just changed this!'
print(team_abbr['GSW'])

# adding elements
team_abbr['PHX'] = 'Phoenix Suns'

# removing elements (using del)
del team_abbr['GSW']
print(team_abbr)

# removing elements (using pop())
just_removed = team_abbr.pop('PHX')
print(f"JUST REMOVED: {just_removed}")
print(team_abbr)


# you can remove all items using clear
# team_abbr.clear()
print(team_abbr)



# DICTIONARY METHODS (with examples)

fake_person = {'name': 'fake person', 
'age': 36, 
'hometown': 'Brooklyn', 
'favorite_songs': ['I Will Survive', 'Photograph', 'September'],
'countries_visited': ['Germany', 'USA', 'Mexico', 'Belgium', 'Canada']}

print(fake_person['countries_visited'])

# 1) clear
# will remove all elements from a dict - essentially making it a blank dict
fake_person.clear()
print(fake_person)


# 2) copy 
# will create a copy of my original dictionary 
# important to note - this is very different from doing an = sign 
orig_dict = {'name': 'james'}
copy_dict = orig_dict.copy()
copy_dict['name'] = 'new_name'
print(copy_dict)
print(orig_dict)

# lets see what happens if we just do an = (instead of copy)
new_dict = {'key': 'value'}
newer_dict = new_dict
newer_dict.clear()

print(newer_dict, new_dict)


# from keys
# create a new dictionary from existing keys 
print(team_abbr)
subset_teams = ['ATL', 'NYK']
print(team_abbr.fromkeys(subset_teams, 'same value'))

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updating the value
value.append('this will be added to all values')
print(vowels)

keys2 = {'a', 'e', 'i', 'o', 'u'}
value2 = [1]

new_dict = {key:list(value2) for key in keys2}

print(new_dict)
value2.append('this wont appear in new_dict')
print(new_dict)

# keys: get the keys of a dict
demo_dictionary = {'this is a key': 'this is a value',
					'another key': 'another value!'}

print(demo_dictionary.keys())
demo_dictionary['adding this as another key'] =  'new value here'
print(demo_dictionary.keys())


# popitem
# abides by the LIFO rule (last in first out) - returns the last (key, value pair)
print(demo_dictionary.popitem())


# set default
city_abbreviations = {'Seattle': 'SEA',
						'San Francisco': 'SF', 
					'Los Angeles': 'LA'}

print(city_abbreviations['Los Angeles'])

new_york = city_abbreviations.setdefault('New York', 'NYC')
print(new_york)

# pop - returns and removes an element from a dictionary given the specified key 
san_fran = city_abbreviations.pop('San Francisco')
print(san_fran)
print(city_abbreviations)


# values - simple (all values in a specified dictionary)
abbreviations = city_abbreviations.values()
print(abbreviations)
print(type(abbreviations))


# update - takes either a dictionary or set of key/value pair (usually a tupe) and adds it to an existing dictionary 
subjects = {'Math': 'MTH', 
			'History': 'HST', 
			'English': 'ENG'}

print(subjects)

# update with a dictionary type object
subjects.update({'Science': 'SCI'})
print(subjects)


# update with a tuple 
subjects.update([('Physical Education', 'PE'), ('Finance', 'FNCE')])

print(subjects)
