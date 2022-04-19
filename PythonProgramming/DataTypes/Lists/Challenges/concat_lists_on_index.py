# PROMPT: Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, 
# then the 1st index item, and so on till the last element.
# any leftover items will get added at the end of the new list.


def concat_lists_index_wise(lst1, lst2):
	list3 = [i+j for i,j in zip(lst1, lst2)]
	return list3

print(concat_lists_index_wise(['Wh', 'ar', 'y', 'fro'], ['ere', 'e', 'ou', 'm']))
