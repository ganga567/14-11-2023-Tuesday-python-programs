# Write a script named copyfile.py. This script should prompt the user for the names of two text files. The contents of the first file should be input and written to the second file. 

def copy_file_contents(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, 'r') as source:
            # Read the contents of the source file
            content = source.read()

        # Open the destination file for writing
        with open(destination_file, 'w') as destination:
            # Write the contents to the destination file
            destination.write(content)

        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    
    except FileNotFoundError:
        print("File not found. Please check the file names and try again.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Get file names from the user
source_file = input("Enter the name of the source text file: ")
destination_file = input("Enter the name of the destination text file: ")

# Copy contents from the source file to the destination file
copy_file_contents(source_file, destination_file)
