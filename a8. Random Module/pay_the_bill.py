import random

names = input("enter everybody name seperated with comma:-")
# way_1:
names_list = names.split()
selected_person = random.choice(names_list)
print(f"Today {selected_person} will pay the bill")

# way_2
length = len(names_list)
choice = random.randint(0,len(names_list)-1)
print(f"Today {names_list[choice]} will pay the bill")