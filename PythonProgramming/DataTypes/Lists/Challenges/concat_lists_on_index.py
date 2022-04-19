
def concat_lists_index_wise(lst1, lst2):
	list3 = [i+j for i,j in zip(lst1, lst2)]
	return list3

print(concat_lists_index_wise(['Wh', 'ar', 'y', 'fro'], ['ere', 'e', 'ou', 'm']))
