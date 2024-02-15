size = input("enter the size of the pizza you want (S/M/B)? ")
bill = 0
if size == 'S' or size == 's':
    bill += 100
    print("the price is 100 rs.")

elif size == 'M' or size == 'm':
    bill += 200
    print("Medium pizza price is 200 rs")

else:
    bill += 100
    print("Small pizza is 100 rs")

add_pepperoni = input("Do you want pepperoni (Y/N) ?")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 's' or size == 's':
        bill += 30

    else:
        bill += 50

extra_cheese = input("Do You want extra cheese (Y/N)? ")
if (extra_cheese == 'y' or extra_cheese == 'Y'):
    bill += 20

print(f"your final bill is {bill}")
