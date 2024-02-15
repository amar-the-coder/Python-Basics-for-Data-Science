print("press 1 for withdraw cash")
print("press 1 for deposit cash")

user_input = int(input("enter the choice"))
current_amount = 20000
if user_input == 1:
    withdraw_amt = int(input("enter the amount to withdraw"))

    if current_amount>=withdraw_amt:
        current_amount = current_amount - withdraw_amt

    else:
        print("Not Enough balance")

elif user_input ==2:
    deposit_amt = int(input("Please enter the deposit amount"))
    current_amount += deposit_amt

else:
    print("Invalid Choice")

print("The current balance os" ,current_amount)


