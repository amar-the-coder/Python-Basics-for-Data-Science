# Q: Create a logic that checks if a number is positive and further checks if the number is even or odd.

# Even positive
# Even negative
# Odd positive
# Odd negative
# zero

var = 10
if var > 0 and var % 2 == 0:
    print('Even positive')
elif var > 0 and var % 2 != 0:
    print('Odd positive')
elif var < 0 and var % 2 == 0:
    print('Even negative')
elif var < 0 and var % 2 != 0:
    print('Odd negative')
else:
    print('zero')

# logic 2
var = 10
if var > 0:
    if var % 2 == 0:
        print('Positive Even')
    else:
        print('Odd positive')
elif var < 0:
    if var % 2 == 0:
        print('Negative Even')
    else:
        print('Odd Negative')
else:
    print('zero')

