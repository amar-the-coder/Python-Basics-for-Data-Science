# Q: Keep on asking the user for a number. If the user enters '0', quit.
# Finally, return the count of even numbers and odd numbers entered by the user.

even_counter = 0
odd_counter = 0
even_sum = 0
odd_sum = 0

while True:
    num = int(input("enter the number"))
    if num == 0:
        print("quit")
        break

    if num % 2 == 0:
        even_counter += 1
        even_sum += num

    else:
        odd_counter += 1
        odd_sum += num

print(f"the count of even numbers is {even_counter} and there sum is {even_sum}")
print(f"the count of odd numbers is {odd_counter} and there sum is {odd_sum}")
