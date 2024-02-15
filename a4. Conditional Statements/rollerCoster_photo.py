height = int(input("What is your height "))
bill = 0
if height >= 3:
    print("can ride")
    age = int(input("what is your age? "))

    if age < 12:
        bill = 150
        print("Ticket price is 150 rs")

    elif age <= 18:
        bill = 250
        print("Ticket price is 250 rs")

    else:
        print("Ticket price is 500 rs.")

want_photo = input("Do you want to take photo (Y/N) ?")
if want_photo == 'y' or want_photo == 'Y':
    bill = bill + 50
    print(f"your total bill is {bill}")
else:
    print("Can't Ride")
