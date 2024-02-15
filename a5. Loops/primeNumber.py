
num = int(input("enter the number for which you want to check "))
isPrime = True
if num<0:
    print("you have enter negative values. They are not prime")

else:
    for i in range(2, num):  # it will give error for negative values
    # we can also take stop counter as num

        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        if num == 1 or num == 0:
            print(f"{num} is neither prime or composite")
        else:
            print(f"{num} is prime Number")

    else:
        print(f"{num} is not prime number")



# # logic 2:
#
# num = int(input("enter the number for which you want to check "))
# count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1
#
# if count == 2:
#     print(f"The {num} is prime")
# else:
#     print(f"The {num} is not prime")




