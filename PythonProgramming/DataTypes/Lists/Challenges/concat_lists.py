# PROMPT: Use a list comprehension to iterate two lists using a for loop and concatenate the current item of each list.


def list_combinations(lst1, lst2):
	return [x+ ' ' +y for x in lst1 for y in lst2]


print(list_combinations(['New York', 'San Francisco'], ['Knicks', 'Warriors']))
