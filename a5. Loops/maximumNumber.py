# do not use len and sum
number = input("enter the list of numbers separated by space ")

number_list = number.split()
count = 0
for number in number_list:
    count += 1
print(f"The length of the list is : {count}")

for i in range(0, len(number_list)):
    number_list[i] = int(number_list[i])
print(number_list)

maximum_number = number_list[0]
minimum_number = number_list[0]
for number in number_list:
    if number > maximum_number:
        maximum_number = number

    if number < minimum_number:
        minimum_number = number

print(f"The maximum number is: {maximum_number}")
print(f"The maximum number is: {minimum_number}")
