# syntax is - for var_name in sequence
#                   statements
print("the basics of for loop")
numbers = [2, 3, 5, -2, 10]
squares = []
for i in numbers:
    square = i ** 2
    squares.append(square)
print(f"The list of squares is: {squares}")

# for else
print("the basics of for loop without break")
numbers_1 = [2, 3, 4, 5, -1, 0, 5, 3]
for i in numbers_1:
    print(i)
else:
    print("Successfully Completed")

# for else with break - in this case it will not go in else block
print("the basics of for loop else with break")
numbers_2 = [2, 3, 4, 5, -1, 0, 5, 3]
for i in numbers_2:
    print(i)
    if i == 0:
        break
else:
    print("Successfully Completed")

# for else with break - in this case it will not go in else block

tuple_example = (2, 3, 46, 5, 34, -1)
for i in tuple_example:
    print(i)
    if i % 6 == 0:
        print(i)
        break

# print("no number divisble by 6") -- this line executes everytime so that instead of using it here we can put in the
# else block

else:
    print("This is no number divisble by 6")
    print("Execute Successfully")
