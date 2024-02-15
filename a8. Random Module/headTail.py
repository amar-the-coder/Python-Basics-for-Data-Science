import random

# first way
side = random.randint(1,2)
if side == 1:
    print("Head")
else:
    print("Tail")

# another way
list_1 = ["Heads","Tail"]
flip_side = random.choice(list_1)
print(flip_side)


