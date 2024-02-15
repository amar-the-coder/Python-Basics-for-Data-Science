# function with return
def sum_(a1, b1):
    c = a1 + b1
    return c


num_1 = 4
num_2 = 5
print(sum_(num_1, num_2))


# we can also return multiple values through a function
def calculate(a, b):
    add = a + b
    product = a * b
    differnce = a - b
    division = a / b
    return add, product, differnce, division


n1 = 12
n2 = 3
p, q, r, s = calculate(n1, n2)
print(f"the sum is : {p}")
print(f"the product is : {q}")
print(f"the difference is : {r}")
print(f"the division is : {s}")

import statistics

def mean_median_mode(list_1):
    return statistics.mean(list_1),statistics.median(list_1),statistics.mode(list_1) # it will give a tuple
    # return [statistics.mean(list_1),statistics.median(list_1),statistics.mode(list_1)] # now it will give a list

print(mean_median_mode([1,2,3,4,5,6,7,8,9]))