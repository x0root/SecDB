# Import the os and shutil modules to work with files and directories
import os
import shutil

# Define a function to create a database file and write data to it
def create_database(filename, data):
    # Open the file in write mode
    with open(filename, "w") as f:
        # Write the data to the file
        f.write(data)
        # Close the file
        f.close()

# Define a function to copy a database file multiple times
def copy_database(filename, copies):
    # Get the file name without the extension
    name = filename.split(".")[0]
    # Get the file extension
    ext = filename.split(".")[1]
    # Loop through the number of copies
    for i in range(1, copies + 1):
        # Create a new file name with a number suffix
        new_filename = name + str(i) + "." + ext
        # Copy the original file to the new file using shutil
        shutil.copy(filename, new_filename)

# Define a function to update all the copies of a database file
def update_database(filename, data, copies):
    # Get the file name without the extension
    name = filename.split(".")[0]
    # Get the file extension
    ext = filename.split(".")[1]
    # Loop through the number of copies
    for i in range(0, copies + 1):
        # Create a file name with a number suffix if i is not zero
        if i == 0:
            new_filename = filename
        else:
            new_filename = name + str(i) + "." + ext
        # Open the file in write mode
        with open(new_filename, "w") as f:
            # Write the data to the file
            f.write(data)
            # Close the file
            f.close()

# Define a function to delete all the copies of a database file
def delete_database(filename, copies):
    # Get the file name without the extension
    name = filename.split(".")[0]
    # Get the file extension
    ext = filename.split(".")[1]
    # Loop through the number of copies
    for i in range(0, copies + 1):
        # Create a file name with a number suffix if i is not zero
        if i == 0:
            new_filename = filename
        else:
            new_filename = name + str(i) + "." + ext
        # Remove the file using os
        os.remove(new_filename)

# Define the name of the database file
filename = "database.txt"
# Define the number of copies to make
copies = 10
# Define the data to write to the file
data = "name,last_name\n"

# Create the database file and write data to it
create_database(filename, data)
# Copy the database file multiple times
copy_database(filename, copies)

# Ask the user for their name and last name
while True:
    # Get the user input
    user_input = input("Enter your name and last name, separated by a comma, or press enter to quit: ")
    # Check if the input is empty
    if user_input == "":
        # Break the loop
        break
    # Check if the input is delete
    elif user_input.lower() == "delete":
        # Delete all the copies of the database file
        delete_database(filename, copies)
        # Print a confirmation message
        print("All the database files have been deleted.")
    # Check if the input is valid
    elif "," in user_input:
        # Add the input to the data variable, with a newline character
        data += user_input + "\n"
        # Update all the copies of the database file
        update_database(filename, data, copies)
        # Print a confirmation message
        print("Your data has been saved to the database.")
    else:
        # Print an error message
        print("Invalid input. Please enter your name and last name, separated by a comma.") 
