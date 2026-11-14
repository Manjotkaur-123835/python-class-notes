
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

n = int(input("Enter prefix length: "))

if n < 0 or n > min(len(s1), len(s2)):
    print("Invalid prefix length")
else:
    new_s1 = s2[:n] + s1[n:]
    new_s2 = s1[:n] + s2[n:]

    print("First string:", new_s1)
    print("Second string:", new_s2)
