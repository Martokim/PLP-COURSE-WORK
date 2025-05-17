with open("input.txt", "w") as file:
    file.write("Hello there I'm martin , currently learning python \n")
    file.write("Python helps in automation and scripting.\n")
    file.write("You can read and write files easily.\n")
    file.write("Learning Python can open many doors.\n")
    file.write("Keep practicing and improving your skills.\n")

with open("input.txt", "r") as file:
    content = file.read

print (content)
