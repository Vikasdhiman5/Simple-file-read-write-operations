# Write data into a file
file = open("example.txt", "w")

text = input(" Enter text to store in the file: ")
file.write(text)

file.close()

print("Data written to file successfully!\n")

# Read data from the file
file = open("example.txt", "r")

content = file.read()

file.close()

print("Reading data from file:")
print(content)
