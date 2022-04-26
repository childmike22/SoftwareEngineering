# 7) Check to see if sets have common elements (if they do, return them)
operating_systems_1 = {'Mac', 'Windows', 'Linux'}
operating_systems_2 = {'Unix', 'Windows'}

if operating_systems_1.isdisjoint(operating_systems_2):
	print("There are no overlapping items!")
else: 
	overlap = operating_systems_2 & operating_systems_1
	print(f"The following items exist in both sets: \n{overlap}")
