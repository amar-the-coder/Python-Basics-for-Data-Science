num = int(input("enter the number for which you want to find the reverse? "))
reversed_num = 0
while (num != 0):
    last_digit = num % 10
    # another logic print(last_digit, end="")
    reversed_num = reversed_num * 10 + last_digit
    num = int(num/10) # or num = num//10

print(f"The reverse of the number is {reversed_num}")
