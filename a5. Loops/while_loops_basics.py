# while condition|expression
#         statements

count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("in else block")
print("out from loop")

# now with break keyword
count_num = 1
while count_num <= 5:
    print(count_num)
    count_num += 1

    if count_num == 3:
        break
else:
    print("in else block")
print("out from loop")

# now in one line

count = 5
while count > 0: print(count); count -= 1
print("out of loop")


# question enter the -1 to get out of loop

number = int(input("enter a number (-1 to Quit)"))
while number!=-1:
    print(number)
    number = int(input("enter a number (-1 to quit)"))
else:
    print("in else block")
print("out from loop")

