# 9) remove non-overlapping items from set1

init_nums = {10, 20, 30, 40, 50}
other_nums = {30, 40, 50, 60, 70}

init_nums.intersection_update(other_nums)

# init_nums = init_nums & other_nums    also works
print(init_nums)
