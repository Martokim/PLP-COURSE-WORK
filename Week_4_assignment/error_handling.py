# Ask the user to enter a filename
filename = input("Please enter the filename you want to read: ")

try:
    # Try opening the file
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)  # Display the content of the file

except FileNotFoundError:
    # Handle the error if the file doesn't exist
    print(f"Error: The file '{filename}' was not found.")
except IOError:
    # Handle other I/O errors (e.g., file is not readable)
    print(f"Error: Could not read the file '{filename}'.")
except Exception as e:
    # Handle any other exceptions
    print(f"An unexpected error occurred: {e}")