# other important topics
set_1 = {1,2,3,4,5}
set_2 = {4,10,7,8,-10}

# Disjoint Set -> When two sets are nothing in common, Basically there intersection is null
print(set_1.isdisjoint(set_2))

# now, set_1 is subset of set_2 if every element of set_1 is in set_2
print(set_1.issubset(set_2))

# another way of doing it Set<=Set2
print(set_1<=set_2)

# Superset
print(set_1.issuperset(set_2))

# Set_1 is a superset of set 2 if set_1 contains every element of set_2
# another way of doing this
print(set_1>=set_2)
