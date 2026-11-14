
try:
    name = input("Enter your name: ")

    if not name.strip():
        raise ValueError("Name cannot be empty")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Name should contain only alphabets")

    print("Hello,", name)

except ValueError as e:
    print("Error:", e)

finally:
    print("Program execution completed")
