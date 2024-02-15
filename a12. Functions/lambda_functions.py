# in python, we usually define functions like this
# def twice(x):
#     return x * 2
#
#
# print(twice(4))

# but instead of doing this we can also do this:
twice = lambda x: x * 2
print(twice(2))

# lambda functions with multiple arguments
avg = lambda x, y, z: (x + y + z) / 3
print(avg(3, 5, 10))

# how to pass a lambda function as a argument
cube = lambda x: x * x * x


def fun(fx, value):
    return 6 + fx(value)


print(fun(cube, 2))
# instead of writing the above line we can aslo write like this
print(fun(lambda x: x * x * x, 2))


# map ---------------------------

# suppose i want to cube of the elements in a list:

# one method is this right ---
def cube_(x):
    return x * x * x


l = [1, 2, 4, 6, 4, 3]
newl = []
for item in l:
    newl.append(cube_(item))
print('using simple method : ')
print(newl)

# we can also do it in the following way using map:

newl = list(map(cube_, l))
print('using map function but using cube : ')
print(newl)
# now one more thing why to write the cube function -- use lambda here
newl = list(map(lambda x: x * x * x, l))
print('using map function but without using cube function doing cube using lambda : ')
print(newl)

# Filter ---------------------------------

# we mainly use filter for filtering
print('basic filtering using function')


def filter_fun(a):
    return a > 4


new_filter_l = list(filter(filter_fun,l))
print('filtering using filter function')
print(new_filter_l)

# Reduce --------------------------------------------

from functools import reduce

numbers = [1,2,3,4,5]

# calculate sum using reduce function
def my_sum(x,y):
    return x+y

sum_of_list = reduce(my_sum,numbers)
print(sum_of_list)



