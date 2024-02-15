# Ternary If
# shorthand for if else.
# just like Excel If: IF(condition/s, value_if_true, value_if_False) Ternary if syntax:
# value_if_true if condition else value_if_false
# Advantage: Shorthand. In a single line, we can implement if logic.
# Disadvantage: You can only implement single line logic for both if and else conditions.

# Q: Print positive if a number is positive otherwise print negative
var = -10
print('positive' if var > 0 else 'negative')

# Q: add 2 to the number if it is positive. Otherwise, subtract 2 from the number
var1 = -12
print(var1+2 if  var>0 else var1-2)

# Q: Nested Ternary If
# Q: Print positive if a number is positive print negative if negative. Otherwise print zero.

var_2= 10
print('positive' if var_2 > 0 else 'negative' if var_2 < 0 else 'zero')

