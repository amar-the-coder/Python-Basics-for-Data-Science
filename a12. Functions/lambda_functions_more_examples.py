# in python, we make functions like this:
def add(a, b):
    result = a + b
    return result


print('Add Using Simple def')
print(add(5, 4))

# we can do this easily by lambda
add_l = lambda a, b: a + b
print("add using lambda")
print(add_l(3, 4))

# we can also implement using one argument
print('''we can also implement using one argument''')
add_l_new = lambda x: x + 100
print(add_l_new(50))

# in python, we do not have to assign a variable to lambda
print('printing lambda without assigning')
print(
    f'Here i Simple print the product of a and b using lambda without assigning in a variable ---- {(lambda a, b: a * b)(15, 30)}')

# we can also use keyword arguments:
product = lambda x, y, z: x * y * z
print(product(z=8, x=9, y=4))

# we can also use default arguments here
add__ = lambda x, y=15, z=20: x + y + z
print(add__(20))

# with *args
addition = lambda *args: sum(args)
print(addition(20, 2, 40, 50))

# lambda as argument
higher_order_function = lambda x, func: x + func(x)
higher_order_function(20, lambda x: x * x)

# even or odd -----
print((lambda x: (x % 2 and 'odd' or 'even'))(120))

# substring question
Sub_string = lambda string: string in 'welcome to python functions tutorial'
print(Sub_string('wel'))

# --------------------------------Filter
num = [10, 40, 56, 27, 33, 15, 70]
greater = list(filter(lambda numb: numb > 30, num))
print(greater)

# num divisble by 4
divide = list(filter(lambda x: (x % 4 == 0), num))
print(divide)

#--------------------Map

double_the_num = list(map(lambda x : x*2, num))
print(double_the_num)
print(f' The Double of the each element of the list is :  {list(map(lambda x: x*2,num))}') # in one line

list_1 = [2,5,10,6,4,12]
cube = list(map(lambda x:x*x*x,list_1))
cube_ = list(map(lambda x:pow(x,3),list_1)) # another way of doing this

print(cube_)

# convert the list elements into int

num_ = ['2','3','5','6']

# one method is iterate through a loop

# method 2 in just one line by using map function

print(list(map(int,num_)))


# --------------------------------end

