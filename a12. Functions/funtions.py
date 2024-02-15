# User defined functions: just a block of code that we can save in memory and use and resue again and again.

# There are 2 parts to
# 1. user defined function.
# 2. definition of the function call
# syntax:
# code1
# code2
# return output

# functions:-

def greet():
    print("hi")
    print("jenny")


greet()
greet()
greet()


# functions with arguments:-
def greet(name):
    print(f"Hi{name}")
    print(f"Are you from cse department")


greet("Jenny")
greet("Ram")


# sum of 2 numbers
def add(a, b):
    c = a + b
    print(f"Sum is {c}")


add(5, 7)


# Types of Arguments

# positional

def greet(name, dept):
    print(f"Hi {name}")
    print(f"Are you from {dept} department")


greet("aman", "ds")


# but here is some catch - if i write like this greet("ds","aman") then there is a nonsense type output.

# to tackle this - we have keyword argument
def greet(name, dept):
    print(f"Hi {name}")
    print(f"Are you from {dept} department")


greet(dept='cs', name='jenny')


# we can also write this ( positional + keyword )
# greet("jenny",dept='cs') positional arguments should follow keyword argument

# we cannot write this
# greet(dept='cs', 'jenny') it will throw an error

# default arguments
def greet(name, subject, dept='cs'):
    print(f"Hi{name}")
    print(f"Do you teach {subject}?")
    print(f"Are you from {dept} department")


greet('jenny', 'python')


# main catch - it will throw an error in the dept because non default argument follow the default argument.
# def greet(name, subject='python',dept):
#     print(f' hi {name}')
#     print(f"Do you know teach {subject}?")
#     print(f"Are you from {dept} department")

# to tackle this we have to write like this:-
def greet(name, dept, subject='python'):
    print(f'hi {name}')
    print(f"Do you know teach {subject}?")
    print(f"Are you from {dept} department")


greet('jenny', 'cs')


# Arbitary
def add(*numbers):
    c = 0
    for i in numbers:
        c += i
    print(f"sum is {c}")


add(1, 2, 3, 4, 5, 6, 7)


# when we pass list as argument
def add(list):
    return sum(list)


list = [1, 2, 3, 4, 5, 6, 7]
add(list)


# -----------------------------------------------------------------------------

# Args & Kwargs

# artitary kwargs
def add(*numbers):
    c = 0
    print(numbers)


# add(1,2,'jenny') this line will throw an error because it will consider jenny as numbers as positional argument

# to tackle this we use **kwargs

def add(a, *numbers):
    c = 0
    print(numbers)
    for i in numbers:
        c += i
        print(f"sum is {c}")


add('', 2, 3, 5)


# ------------------------------------------------------

def info_person(**kwargs):
    for key, value in kwargs.items():
        print(key,value)

info_person(name='ram',age='30',dept='cse')
info_person(name='shyam',dept='cse')

# same as previous first args, then kwargs

# def info_person (*args, **kwargs)
# info_person (1,2,name='ram',age='30',dept='cse')



