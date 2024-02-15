tuple1 = (10,1,-10,15,20)
tuple2 = ("Jenny", "Ram", "Shyam")
tuple3 = (10,"Jenny", True,10.10)

# They are just same as lists:
# all functions works fine

tuple_1 = (12,6,-8,'jenny',True,12,6)
tuple_2 = (45,67,90)
tuple_3 = (tuple_1, tuple_2)

print(tuple_3)

# But if
tuple_4 = tuple_1 + tuple_2
print(len(tuple_4))

# for finding max = print(max(tuple_2))
# for finding count = print(count(tuple_2))
# for finding index = print(index(tuple_2))

list_1 = [1,2,3,5]
print(tuple(list_1)) #type conversion

# note:-
tuple_6 = (10,)*5
print(tuple_6)

# tuples are immutable so we can't change them.

tuple1[0] =5 # it will throw an error because it tuples are immutable so can't change them
print(tuple1)



