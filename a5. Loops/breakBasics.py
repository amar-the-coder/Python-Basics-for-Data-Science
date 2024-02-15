# break
count =1
while count<=10:
    print(count)
    count+=1
    if count ==7:
        break
    print("Hi")
print("Out from Loop")

# break

list1 = ["hi" , "hello", "welcome"]
names = ["krish", "ram", "madhav"]

for item in list1:
    for name in names:
        print(item,name)

    if item=='hello' and name =='ram':
        break
    print("out of inner loop")
print("out from outer loop")

