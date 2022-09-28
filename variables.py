# Variables in python
my_variable = 'my String variable'
first_name = 'Pancho'
last_name = 'Pampa'
city = 'Valencia'
age = 6
is_married = True

change_value = str(age)

# Printing the values stored in the variables

print(my_variable, 'hi i am ', my_variable, age, len(city), type(change_value), is_married)

# Multiple variables can also be declared in one line:

one_variable, two_variable, three_variable, four_variable, five_variable = 'One variable', 'Two variable', 'Three variable', 250, True

print(one_variable, two_variable, three_variable, four_variable, five_variable)


# Printing out types
print(type('String!'))  # str
print(type(first_name))  # str
print(type(10))  # int
print(type(3.14))  # float
print(type(1 + 1j))  # complex
print(type(True))  # bool
print(type([1, 2, 3, 4]))  # list
print(type({'name': 'Pancho', 'age': 25, 'is_married': 25}))  # dictionary
print(type((1, 2)))  # tuple
print(type(zip([1, 2], [3, 4])))

# Casting: Converting one data type to another data type.

# int to float
num_int = 100
print('num_int', num_int)
num_float = float(num_int)
print('num_float', num_float)


# float to int
gravity = 9.81
print(int(gravity))

# int to string
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

# str to int or float
num_to_str = '10.25'
print('num_int', int(float(num_to_str)))
print('num_float', float(num_to_str))

