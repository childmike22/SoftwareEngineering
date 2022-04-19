# replace all instances


def replace_all_instances(lst, num_to_replace, replacing_num_with):
	return [replacing_num_with if x == num_to_replace else x for x in lst]


print(replace_all_instances(['New York City', 'SF', 'New York City', 'MIA', 'ATL', 'MIL', 'MIN', 'New York City'], 'New York City', 'NYC'))
