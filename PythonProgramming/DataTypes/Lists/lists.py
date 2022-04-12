cookies = ['sugar', 'oatmeal', 'chocolate chip']
ice_cream = ['vanilla', 'strawberry']

print(cookies + ice_cream)

# tuples
# immutable - can't add or remove elements

ages = [21, 22, 24, 25]
bill_age, bob_age, sally_age, nancy_age = ages
print(bob_age)


# sets
# can be created from a list
# only unique elements

names = ['nancy', 'nancy', 'mike', 'jeff', 'nancy']
set_names = set(names)
print(len(names))
print(len(set_names))

set_names.discard('mike')
print(set_names)

cookies_i_ate = set(['chocolate chip', 'sugar', 'peanut butter'])
cookies_you_ate = set(['brownie', 'sugar'])

print(f"UNION: {cookies_i_ate.union(cookies_you_ate)}")
print(f"INTERSECTION: {cookies_i_ate.intersection(cookies_you_ate)}")

print(f"I ATE BUT YOU DIDNT: {cookies_i_ate.difference(cookies_you_ate)}")
