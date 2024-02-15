height = input("enter the heights Separated by a space: ")
height_list = height.split()
count = 0
for height in height_list:
    count = count + 1
print(count)
total = 0

for i in range(count):
    height_list[i] = int(height_list[i])

for person in height_list:
    total += person

avg = total / count
print(f" the averge is {round(avg)}")
