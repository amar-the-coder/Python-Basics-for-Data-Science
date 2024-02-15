# HW: Create a guessing game. Initialize the correct guess. Keep on asking the user of a guess. If the guess is
# higher than the correct guess, then prompt the user that you are high and you should guess low. and similarly for
# low guesses.

correct_guess = 90

while True:
    num = int(input("Please Guess a number between 1 to 100 "))

    if correct_guess==num:
        print("You guess right!! Congrats")
        break

    if num>correct_guess:
        print("you guess more. Please guess less")
    else:
        print("You have  Guess less. Please Guess more ")

print("now with logic 2")
# logic 2
correct_guess_1 = 23
while num!=correct_guess_1:
    if num > correct_guess_1:
        print("you guess more. Please guess less")
        num = int(input("guess less"))
    else:
        print("you guess less. Please guess more")
        num = int(input("guess more"))
print("correct guess")