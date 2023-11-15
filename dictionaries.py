# Write a program to demonstrate working with dictionaries in python.
# Dictionary demonstration program

# Creating a dictionary
student = {
    'name': 'Gangadhar',
    'age': 20,
    'grade': 'A',
    'courses': ['Math', 'English', 'History']
}

# Accessing dictionary values
print("Student Information:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Grade: {student['grade']}")
print(f"Courses: {', '.join(student['courses'])}")

# Modifying dictionary values
student['age'] = 21
student['grade'] = 'B'
student['courses'].append('Science')

# Displaying modified information
print("\nUpdated Student Information:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Grade: {student['grade']}")
print(f"Courses: {', '.join(student['courses'])}")

# Adding a new key-value pair
student['gender'] = 'Male'

# Displaying the final information
print("\nFinal Student Information:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
  
