
s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub == "":
    print("Substring cannot be empty")
else:
    indices = []

    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            indices.append(i)

    if indices:
        print("Substring indices:", indices)
    else:
        print("Substring not found")
