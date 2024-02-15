number = int(input("enter the number for which you want to calculate the factorial "))
factorial = 1
for i in range(1,number+1):
    factorial = factorial*i
print(factorial)

## logic 2
number = int(input("enter the number for which you want to calculate the factorial "))
factorial = 1
for i in range(number,0,-1):
    factorial = factorial*i
print(factorial)