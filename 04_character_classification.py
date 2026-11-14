
ch = input("Enter a character: ")

if len(ch) != 1:
    print("Enter only one character")
elif ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
