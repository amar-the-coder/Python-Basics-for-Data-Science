l1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

l2 = []

for i in range(len(l1)):
    if l1[i] >= 20 and l1[i] <= 50:
        l2.append(l1[i])
print(l2)


