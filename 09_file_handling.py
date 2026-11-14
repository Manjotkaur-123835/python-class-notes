
filename = "sample.txt"

# Writing into a file
f = open(filename, "w")
f.write("Welcome to Python Programming!")
f.close()

# Reading from a file
f = open(filename, "r")
data = f.read()
print("File contents:")
print(data)
f.close()

# Appending data
f = open(filename, "a")
f.write("\nThis is file handling practical.")
f.close()

print("Data written and appended successfully.")
