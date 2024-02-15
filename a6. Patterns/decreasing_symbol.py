rows = int(input(" enter the number of rows? "))
symbols = input(" enter the symbol ")

for i in range(1,rows+1):
    for j in range(i,rows+1):
        print(symbols,end="")
    print()