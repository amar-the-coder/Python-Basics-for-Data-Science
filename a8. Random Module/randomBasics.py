import random
# randint
a = random.randint(1,7) # any number betwwen one and 7
print(a)

#randrange
b = random.randrange(1,3) # here stop is exclusive
print(b)

# random.random (0.000 <= 1.000)
c= round(random.random(),1)
print(c)

# random.uniform
d = random.uniform(1,3)

# random.choice
list_1 = [108,23,-4,89,12,34]
e = random.choice(list_1)


