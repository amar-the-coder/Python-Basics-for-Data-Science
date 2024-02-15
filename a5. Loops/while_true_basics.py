# while true
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break
else:
    print("In the else block")
print("out of loop")

# question ask user to enter the number and if he hit zero print the sum
total = 0
number = int(input("enter a number ( 0 to quit ) "))
while number != 0:
    total = total + number
    number = int(input("enter a number ( 0 to quit ) "))
print("The total of the entered numbers is: ", total)
