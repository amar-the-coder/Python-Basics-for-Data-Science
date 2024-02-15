set_1 = {'ram', 'shyam', 'jenny'}
set_2 = {'jenny', 'jiya', 'Akash'}

set_1_ = {'ram', 'shyam', 'jenny'}
set_2_ = {'jenny', 'jiya', 'Akash'}

# union ---------------------------------------------------------------------------
print(f"The union of set1 and set2 is {set_1.union(set_2)}")
print(f"The union of set2 and set1 is {set_2.union(set_1)}")

# another logic
print(
    f"The union of set1 and set2 is {set_1 | set_2}")  # we can give as much paramters in it like set_1 | set 2 | set3...

# we can also pass a tuple in the union, but first it will convert it into set.

print(set_1_.union(('mohan', 'jenny')))

# but the catch is we cannot pass the tuple in this logic way.
# print(set_1 | ('mohan', 'jenny'))

# we can also update the set
# in this we have to remember that it will not work in print statement then we have to first update then print
# or we can also in this way
set_1_.update(['jenny', 'mohan'])
print(set_1_)

# Intersection --------------------------------------------------------

print(f"The Intersection of set1 and set2 {set_1.intersection(set_2)}")

set_3 = {'ankur', 'pradeep'}

print(set_1.intersection(set_2, set_3))

# another way of doing this

print(set_1 & set_2)

# we can also pass a list in this
print(set_1.intersection(['mohan', 'shiva']))

# updating
set_1_.intersection_update(set_2_)
print(set_1_)

set_2_.intersection_update(set_1_)
print(set_2_)

set_2_.intersection_update(['mohan', 'ram'])

# Difference--------------------------------------------------------------

print(set_1.difference(set_2))

# another way of doing this
print(set_1 - set_2)

# we can also pass a list or tuple n difference
print(set_1.difference(('mohan', 'shiva')))

set_one = {'ram', 'shyam', 'jenny'}
set_two = {'jenny', 'jiya', 'akash'}
set_three = {'ankur', 'pradeep', 'ram'}

print(set_one.difference(set_2,set_3))

# updating
set_1.difference(set_2)
print(set_1)

set_2.difference(set_1)
print(set_2)

# Symmetric Difference -----------------------------------------------------------------------

print(set_1.symmetric_difference(set_2)) # here we cannot pass multiple sets

# another way of doing this
print(set_1^set_2) # we can pass multiple here print(set_1 ^ set_2 ^ set_3)

#updating the set:- 
set_2.symmetric_difference_update(set_1)
print(set_2)

# we can pass multiple values
set_1.symmetric_difference_update(('Mohan','Shiva'))
print(set_2)

