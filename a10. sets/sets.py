set_1 = {10, True, 'Jenny', 111}
set_2 = {1,2,10,-10,0,53,1}
set_3 = {10, True, 'Jenny', 111}
# They are unordered collection of elements & in this basically duplicates are not allowed.
# since they are unordered, so indexing are not possible.

set_3 = {} # we can't create a empty set in this way because it will create a empty dictionary.

# so the solution is for empty set.
set_3 = set()


# now the important things for sets.

# add elements in sets
set_1.add(99)
print(set_1)

# for finding the length
print(len(set_1))

# for removing the element
# set_1.remove(68)
# print(set_1)  but in remove function if element in not present in set then it will throw an error.

# so tackle this thing we a another function called discard. if element is not present even then it will not throw an
# error

# for clear all the elements we have
set_3.clear()

# pop - it will not just delete but also return it.
set_4 = {10, True, 'Jenny', 1111}
print(set_4.pop())
print(set_4)

# we can add a tuple in set

set_5 ={'amarjeet','vanshaj', 'sheetal', 'shivika', 'ayesha', 'vishal', 'mandeep'}
set_5.add(('king', 'queen'))
print(set_5)
