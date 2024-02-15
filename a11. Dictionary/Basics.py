# dict_name = {key:value}

phone_no = {'ram': 1234, 'shyamm': 3456, 'mohan': 1111}

# dictionaries are ordered
# Duplicate values are not allowed, although it will just print the last occurrences of that element

# Access the element

print(phone_no['shyamm'])  # using a key value

# another way of creating dictionaries

phone_no_ = dict([('ram', 1234), ('shyam', 3456), ('mohan', 8978)])
print(phone_no_)

# update the value
phone_no['mohan'] = 9999
# or
phone_no['madhav'] = {1111, 2222, 3333}
print(phone_no)

# we can also add a dictionary like
phone_no['shyam'] = {'shyam_home': 5555, 'shyam_work': 4444}
print(phone_no['shyam'])

print(phone_no)

# to access in nested dictionary
print(phone_no['shyam']['shyam_work'])

# to delete key
# del phone_no_['ram]

# pop - it will delete key as
print(phone_no.pop('shyam'))

# pop.item - it will delete the last key
print(phone_no.popitem())

# clear - it will delete all the keys
# phone_no.clear()

# we can print in the three ways
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())

# Storing financial information of a stock in a dictionary

stock_info = {
    "symbol": "AAPL",
    "company_name": "Apple Inc.",
    "current_price": 150.25,
    "net_income": 2.5,
    "revenue": 30.5,
    "dividend_yield": 1.5
}

# Storing dates
dates = [{"year": 2023, "month": 9, "day": 23},
         {"year": 2023, "month": 9, "day": 24},
         {"year": 2023, "month": 9, "day": 25}]

# Storing multiple products in a single dictionary

products3 = {
    1001: {
        "name": "Laptop",
        "price": 999.99,
        "brand": "Dell",
        "in_stock": True
    },
    1002: {
        "name": "Smartphone",
        "price": 699.99,
        "brand": "Apple",
        "in_stock": False
    },
    1003: {
        "name": "Tablet",
        "price": 399.99,
        "brand": "Samsung",
        "in_stock": True
    }
}

country_codes = {
    "US": "United States",
    "CA": "Canada",
    "GB": "United Kingdom",
    "AU": "Australia",
    "DE": "Germany",
    "FR": None,
    "JP": "Japan",
    "IN": "India",
    "CN": "China",
    "BR": None
}
# how to access in nested list...
print(products3[1002]['price'])

print(dates[0]['month'])

# how updating works in dictionary

dict_one = {'Name': 'John', 'PAN': 10001, 'Salary': 200000, 'Address': 'Delhi'}
dict_one['Name'] = 1
dict_one['years_of_exp'] = 20
print(dict_one)

# If the key already exists, it gets overwritten. If it doesn't exist, then a new key value pair is created

# methods of dictionaries

# .items() .keys() .values()

print(stock_info.items())  # combination of key and value in form of list and tuples
print(stock_info.keys())
print(stock_info.values())

# now how to iterate in the dictionary

# 3 ways of iterating over dictionaries
# iterate over the values
# iterate over the keys
# iterate over both at the same time

for var in stock_info:  # by default, iterates over the keys
    print(var)

for key in stock_info:  # by default, iterates over the keys
    print(stock_info[key])

for var in stock_info.keys():
    print(var)

# Iterate over the values directly

for value in stock_info.values():
    print(value)

# Iterate over both at the same time
for key, value in stock_info.items():
    print(key, value)

# Storing multiple products in a single dictionary
products3 = {
    1001: {
        "name": "Laptop",
        "price": 999.99,
        "brand": "Dell",
        "in_stock": True
    },
    1002: {
        "name": "Smartphone",
        "price": 699.99,
        "brand": "Apple",
        "in_stock": False
    },
    1003: {
        "name": "Tablet",
        "price": 399.99,
        "brand": "Samsung",
        "in_stock": True
    }
}

product4 = {'Product1': True, 'Product2': False, 'Product3': True, 'Product4': False}

# print the names of all products which are out of stock

for i in product4:      # iterate over the keys
    if product4[i] == False:
        print(i)

# Iterate over the keys
for key in product4:
     if product4[key] == False:
       print(key)

# Q: Given some text, return a dictionary of word counts where each key is a unique word of the text and the
# corresponding value is the count of that word.

text = """This is good day. I am doing good"""

# clean the text, upper / lower, remove extra spaces and special symbols
text = text.lower().replace('.', '').replace(',', '')
# split
words = text.split()
# run a for loop and count each word.

word_counts = {}
for word in words:
    word_counts[word] = words.count(word)

