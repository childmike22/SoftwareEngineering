def remove_empty_strings(lst):
	return [x for x in lst if x != '']


print(remove_empty_strings(['where', '', 'are', '', 'you', 'from', '']))
