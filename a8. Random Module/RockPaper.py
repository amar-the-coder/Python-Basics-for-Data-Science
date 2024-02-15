import random
user_input = int(input("Enter your choice:\nPress 0 for Rock\nPress 1 for Paper\nPress 2 for Scissors\n"))
system_choice = random.randint(0,2)
if user_input>=3 or user_input<0:
    print("Oops!! you have press invalid number so try again")

else:
    if system_choice==0:
        print("Computer choice: Rock")
    elif system_choice==1:
        print("Computer choice: Paper")
    else:
        print("Computer choice: Scissors")

    if system_choice==user_input:
        print("It is Draw")

    elif system_choice==0 and user_input==2:
        print("You lose")
    elif system_choice==2 and user_input==0:
        print("You Win Congrats")
    elif system_choice>user_input:
        print("You lose Try Again")
    elif system_choice<user_input:
        print("You Win Congrats")