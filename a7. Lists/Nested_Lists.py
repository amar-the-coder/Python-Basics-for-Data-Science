basic_list_1 = [1,2,3,4,5,6,7,8,9,[10,11,12,13,14,15,16]]
print(len(basic_list_1))

print(basic_list_1[9][1]) # to access the element in nested list

# question to hide the money

row_1 = ['X','X','X']
row_2 = ['X','X','X']
row_3 = ['X','X','X']

matrix_list = [row_1,row_2,row_3]

print(f"{row_1}\n{row_2}\n{row_3}")
row_position = int(input(" enter the row where you want to hide the money"))
column_position = int(input(" enter the column where you want to hide the money"))
row_selected = matrix_list[row_position-1]
row_selected[column_position-1]= '0'
print(f"{row_1}\n{row_2}\n{row_3}")


