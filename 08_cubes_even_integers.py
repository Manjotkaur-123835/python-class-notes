
n = int(input("Enter the limit: "))

print("Cubes of even integers:")

for i in range(2, n + 1, 2):
    print("Number:", i, "Cube:", i ** 3)
