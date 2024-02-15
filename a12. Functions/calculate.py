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
