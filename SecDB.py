# Import the os, shutil, and hashlib modules to work with files, directories, and hashes
import os
import shutil
import hashlib

print("SecDB")
print("")
print("Made by Jose")
print("")
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

# Define a function to encrypt the data with SHA-256
def encrypt_data(data):
    # Encode the data as bytes
    data_bytes = data.encode("utf-8")
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256(data_bytes)
    # Get the hexadecimal representation of the hash
    data_hash = hash_object.hexdigest()
    # Return the hashed data
    return data_hash

# Define a function to list the data in the database file
def list_data(filename):
    # Open the file in read mode
    with open(filename, "r") as f:
        # Read the data from the file
        data = f.read()
        # Close the file
        f.close()
    # Print the data
    print(data)

# Define a function to check the hash of a file
def check_hash(filename, expect):
    # Open the file in read mode
    with open(filename, "rb") as f:
        # Read the data from the file
        data = f.read()
        # Close the file
        f.close()
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256(data)
    # Get the hexadecimal representation of the hash
    data_hash = hash_object.hexdigest()
    # Compare the hash with the expected hash
    if data_hash == expect:
        # Return True if they are the same
        return True
    else:
        # Return False if they are different
        return False

# Define a function to delete the corrupted files
def delete_corrupted(filename, copies, hashes):
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
        # Check the hash of the file with the expected hash
        if not check_hash(new_filename, hashes[new_filename]):
            # Remove the file if it is corrupted
            os.remove(new_filename)
            # Print a message
            print(f"{new_filename} is corrupted and deleted.")

# Define the name of the database file
filename = "database.txt"
# Define the number of copies to make
copies = 10
# Define the data to write to the file
data = "name,last_name\n"

# Encrypt the data with SHA-256
encrypted_data = encrypt_data(data)

# Create the database file and write encrypted data to it
create_database(filename, encrypted_data)
# Copy the database file multiple times
copy_database(filename, copies)

# Store the expected hashes of the files in a dictionary
hashes = {}
# Loop through the number of copies
for i in range(0, copies + 1):
    # Create a file name with a number suffix if i is not zero
    if i == 0:
        new_filename = filename
    else:
        new_filename = filename.rsplit(".", 1)[0] + str(i) + "." + filename.rsplit(".", 1)[1]

    # Store the hash of the file as the value of the file name key
    hashes[new_filename] = encrypt_data(data)

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
    # Check if the input is list
    elif user_input.lower() == "list":
        # List the data in the database file
        list_data(filename)
        # Print a confirmation message
        print("The data in the database file has been listed.")
    # Check if the input is valid
    elif "," in user_input:
        # Add the input to the data variable, with a newline character
        data += user_input + "\n"
        # Encrypt the data with SHA-256
        encrypted_data = encrypt_data(data)
        # Update all the copies of the database file
        update_database(filename, encrypted_data, copies)
        # Update the expected hashes of the files
        for i in range(0, copies + 1):
            # Create a file name with a number suffix if i is not zero
            if i == 0:
                new_filename = filename
            else:
                new_filename = filename.rsplit(".", 1)[0] + str(i) + "." + filename.rsplit(".", 1)[1]

            # Store the hash of the file as the value of the file name key
            hashes[new_filename] = encrypt_data(data)
        # Print a confirmation message
        print("Your data has been encrypted and saved to the database.")
    # Check if the input is check
    elif user_input.lower() == "check":
        # Delete the corrupted files
        delete_corrupted(filename, copies, hashes)
        # Print a confirmation message
        print("The corrupted files have been checked and deleted.")
    else:
        # Print an error message
        print("Invalid input. Please enter your name and last name, separated by a comma.")
