# Q: Keep on asking the user for a number. Keep on print the square of that number.
# If the use enters 0, then break out of the loop.

while True:
    num = int(input("enter the number and 0 to quit "))

    if num==0:
        print(" Quit ")
        break

    print("the square of the {} is :{}".format(num,num**2))