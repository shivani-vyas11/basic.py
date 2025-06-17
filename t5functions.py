# functions to greet the user 
def greet (name):
    print(f"hello,{name}!")

# function to check if a number is even 
def is_even(number):
    return number % 2 == 0
# usage 
greet("shivani")
num = 8 
print(f"Is {num} even? {'Yes' if is_even(num) else 'No'}")
        