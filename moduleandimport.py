#Write a python program to define a module and import a specific function in that module to another program  

def greet(name):
    return f"Hello, {name}!"


# main_program.py

# Import the specific function from the module
from my_module import greet

# Use the imported function
name = input("Enter your name: ")
message = greet(name)

# Display the result
print(message)
