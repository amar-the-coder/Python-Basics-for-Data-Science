rows = int(input("enter the numbers of rows "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# logic 2
for i in range(rows):
    for j in range(i + 1):  # if i use (rows+1) then it will print square
        print("*", end=" ")
    print()

# logic 3
for i in range(rows + 1):
    print("*" * i)


