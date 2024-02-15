sum_total = 0
for i in range(1, 101):
    sum_total += i
print(f"the sum of first 100 numbers is: {sum_total}")

# now with user input
sum_ = 0
num = int(input("enter the number upto which you want to find the sum"))
for i in range(1, num + 1):
    sum_ += i
print(f"the sum of first {num} numbers is: {sum_}")


