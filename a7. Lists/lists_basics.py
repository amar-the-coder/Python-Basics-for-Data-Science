roll_no = [1, 2, 3, 4]
names = ['jenny', 'ram', 'shyam']
mix_list = [1, 'jenny', 'mam']

# lists are already mutable

numbers = [10, 0, -1, 7, 8, 10, -67]
# to access the elements

# 1. INDEXING
print(numbers[0])

# 2. SLICING
print(numbers[1:4])
print(numbers[:5])
print(numbers[0:5:2])
print(numbers[0:5:3])
print(numbers[0::3])
print(numbers[::-1])

# 3. we can also sort
# numbers.sort()
# print(numbers)

# to sort in descending
# numbers.sort(reverse=True)
# print(numbers)

# to get the maximum and minimum number
print(max(numbers))
print(min(numbers))

# for add the elements in lists:

# method 1:-
numbers.append(45)
print(numbers)

# method 2:- for add in any index
numbers.insert(2, 45)
print(numbers)

# method 3:- add multiple values
numbers.extend([45, 46, 47, 48])
print(numbers)

# you want to change the data at a same index- updating
numbers[1] = 45

# updating multiple values in a time
numbers[1:4] = [45, 46, 47]
print(numbers)

# remove - it will remove the first occurence of the element
numbers.remove(45)
print(numbers)

# pop - it will remove the element and also returned the removed element
print(numbers.pop())  # if no index is passed then it will last element
print(numbers)
print(numbers.pop(2))

# iterable in list

list_1 = list(range(5, 101, 5))
print(list_1)

# method 1:
for i in list_1:
    print(i)

# method 2:
for i in range(len(list_1)):
    print(list_1[i])

# method 3:
i = 0
while i < len(list_1):
    print(list_1[i])
    i += 1
