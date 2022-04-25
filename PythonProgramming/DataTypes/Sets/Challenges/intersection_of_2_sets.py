# 2) Return a new set of identical items from two sets
states = {'NYC', 'CA', 'CO'}
states2 = {'WA', 'WV', 'CO'}


# find the intersection using .intersection or &
overlapping_states = states & states2
# overlapping_states = states.intersection(states2)  (also works)
print(overlapping_states)
