# Nested List:
Student_data = {'ram': {'roll_no': 10, 'age': 20, 'course': 'python'},
                'mohan': {'roll_no': 20, 'age': 22, "course": 'java'}}

# want to print mohan - roll
print(Student_data['mohan']['roll_no'])

# if u want to add phone_no to mohan
Student_data['mohan']['phone'] = 98756
print(Student_data['mohan'])

# if u want to delete
#  it will happen like this -- del Student_data['mohan']['phone']

# want to return what is deleted:
print(Student_data['mohan'].pop('phone'))

# if I want to nest a list in a dictionary ---
travel_data = {'gujrat': ['dwarf', 'somnath', 'statue_of_unity'], 'rajasthan': ['jaipur', 'udaipur']}
print(travel_data)

# if you nest dictionary in a list
customer_data = [{'name': 'ram', 'roll_no': 10, 'age': 20, 'course': 'python'}, {'name': 'mohan', 'roll_no':20, 'age':22,'course': 'java'}]
print(customer_data)
print(customer_data[1]['name']) # it will give mohan

