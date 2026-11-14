
n = int(input("Enter the limit: "))

cube_dict = {}

for i in range(1, n + 1):
    cube_dict[i] = i ** 3

print("Dictionary of cubes:")
print(cube_dict)
