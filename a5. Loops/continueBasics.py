count =1
while count <=10:
    print(count)
    count+=1
    if count==7:
        continue
    print("hi")
print("out from loop")

# another example
for i in range(1,11):
    if i==7:
        continue
    else:
        print(i)