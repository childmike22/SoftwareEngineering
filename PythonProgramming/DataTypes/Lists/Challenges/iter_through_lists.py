# PROMPT: Given a two Python list. 
# Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.


def iter_through_lists(lst1, lst2):
	for item1, item2 in zip(lst1, lst2[::-1]):
		print(item1, item2)


iter_through_lists([44, 82, 90], [8, 22, 92])
