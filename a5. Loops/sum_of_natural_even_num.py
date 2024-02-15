# logic 1 ::

num = int(input("enter the number!! "))
sum = 0
for i in range(0, num + 1, 2):
    sum += i
print("the sum of even numbers of the {} natural numbers is {}".format(num, sum))

# logic 2 ::

num = int(input("enter the number!! "))
sum = 0
for i in range(0, num + 1):
    if i%2==0:
        sum += i

print("the sum of even numbers of the {} natural numbers is {}".format(num, sum))
