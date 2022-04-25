# 5) Remove items from a set all at once
# remove [10, 20, 30] from the following set - all together at once

new_set = {10, 20, 30, 40, 50}
items_to_remove = {10, 20, 30}

new_set.difference_update(items_to_remove)
print(new_set)
