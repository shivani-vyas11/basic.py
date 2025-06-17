# 1.Basic syntax and variables 
# Declear Variables 
name = "shivani"
age = 21
height  = 5.5
 
# print using formatted strings (f-strings)
print(f"MY name is {name}.")
print(f"I am {age}years old.")
print(f"My height is {height}feet .")

# 2. Data types and type conversion
#  print the data types of each variable
print(f"Data type of name :{type(name)}")
print(f"Data type of age :{type(age)}")
print(f"Data type of height :{type(height)}")

# convert age to string
age_str = str(age)
print(f"Age as string: {age_str}")

# Convert height to integer
height_int = int(height)
print(f"Height as an integer: {height_int}")