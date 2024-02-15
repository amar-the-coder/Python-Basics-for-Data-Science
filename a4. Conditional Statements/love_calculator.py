name1 = input("what is the name? ")
name2 = input("what is his/her name? ")
combine_string = name1 + name2
lower_case_string = combine_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 20:
    print(f"your score is {love_score}% and you both should stay away from each other ")

elif love_score >= 40 and love <= 50:
    print(f"your score is {love_score}% and you both together a nice couple (coke and mentos) like a blast")

elif love_score >= 90:
    print(f"your score is {love_score}% and you both are made for each other")

else:
    print(f"your love score is {love_score}%")
