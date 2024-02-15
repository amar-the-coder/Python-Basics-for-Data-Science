number = int(input("enter the number for which you want the table "))
count = int(input("enter the count upto which you want the result "))
product=1
for i in range(1,count+1):
    product=number*i
    print(f"The result of {number} * {i} = {product}")


