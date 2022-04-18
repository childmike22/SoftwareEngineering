# lists in Python

# creating lists
programming_languages = ['JavaScript', 'Java', 'Python', 'C++']

# accessing elements
print(programming_languages[2])

# accessing elements (negative indexing)
print(programming_languages[-1])

# list slicing
java_and_python = programming_languages[1:3]
print(java_and_python)

# add elements (using append)
programming_languages.append('Rust')
print(programming_languages)

# add elements (using extend)
programming_languages.extend(['Go', 'Solidity'])
print(programming_languages)


# add element (to a specific position using insert)s
programming_languages.insert(3, 'Rubby') # intentionally misspelled
print(programming_languages)


# updating an element
programming_languages[3] = 'Ruby'
print(programming_languages)

# programming_languages[3:] = ['sup']
# print(programming_languages)

# trial = [x if x not in ('Python', 'JavaScript') else 'REMOVE' for x in programming_languages]
# print(trial)


# combining lists using the + symbol
other_languages = ['C', 'Bash']
programming_languages = programming_languages + other_languages
print(programming_languages)

# multiply (using *)
print(programming_languages * 4)

programming_languages[5:5] = [22,33,44]
print(programming_languages)


# delete list items (using del)
programming_languages.insert(4, 'fake_programming_language')
print(programming_languages)
del programming_languages[4]
print(programming_languages)

del programming_languages[5:8]
print(programming_languages)



# accessing and removing elements using pop
bash = programming_languages.pop()
print(bash)
print(programming_languages)

# pop at a specified location
java = programming_languages.pop(1)
print(java)
print(programming_languages)


# removing elements using blank lists
print(programming_languages[5:7])
programming_languages[5:7] = []
print(programming_languages)
