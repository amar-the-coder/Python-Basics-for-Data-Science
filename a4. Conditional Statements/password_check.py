current_pwd = 'Password@123'

password = input("enter the password")

while current_pwd != password:
    current_pwd = input('Please enter the password again')

print('Access Granted')

# with while true:
print("now with while true")
correct_pwd = 'Password@123'
# pwd = input("Please enter the password")
# infinite loop
while True:
    pwd = input('Please enter the password again')
    if pwd == correct_pwd:
        print("Access Granted")
        break
