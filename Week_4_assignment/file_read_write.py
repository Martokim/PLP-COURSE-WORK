with open("input.txt", "w") as file:
    file.write("Hello there I'm martin , currently learning python \n")
    file.write("Python helps in automation and scripting.\n")
    file.write("You can read and write files easily.\n")
    file.write("Learning Python can open many doors.\n")
    file.write("Keep practicing and improving your skills.\n")

with open("input.txt", "r") as file:
    content = file.read

# Proccess the content by converting the text to uppercase and count the number of words.
word_count = len(content.split())  # Count the number of words
upper_content = content.upper()  # Convert the content to uppercase

# Step 4: Write the processed content to a new output file
with open("output.txt", "w") as file:
    file.write("PROCESSED TEXT:\n")
    file.write(upper_content)  # Write the uppercase content
    file.write("\n")  # Add a new line
    file.write(f"WORD COUNT: {word_count}\n")  # Write the word count

# Step 5: Print a success message
print("✅ Success! The file 'output.txt' has been created with the processed content.")