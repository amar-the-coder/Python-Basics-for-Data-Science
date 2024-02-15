# logic 1

rows = int(input(" enter the number of rows? "))
columns = int(input(" enter the number of columns? "))
symbols = input(" enter the symbol ")

for i in range(rows):
    for j in range(columns):
        print(symbols, end="")
    print()