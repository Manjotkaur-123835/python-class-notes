
"""
PYTHON PRACTICALS
A collection of 15 Python programming practicals.
"""

import math
import os


# 1. Roots of a Quadratic Equation
def quadratic_equation():
    print("\n--- Quadratic Equation ---")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("This is not a quadratic equation.")
        return

    d = b ** 2 - 4 * a * c

    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        print("Two distinct real roots:", r1, "and", r2)
    elif d == 0:
        r = -b / (2 * a)
        print("Two equal real roots:", r)
    else:
        real = -b / (2 * a)
        imaginary = math.sqrt(-d) / abs(2 * a)
        print("Complex roots:")
        print(f"{real} + {imaginary}i")
        print(f"{real} - {imaginary}i")


# 2. Prime Numbers
def prime_numbers():
    print("\n--- Prime Numbers ---")
    n = int(input("Enter a number: "))

    if n <= 1:
        print(n, "is not a prime number.")
        return

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            print(n, "is not a prime number.")
            return

    print(n, "is a prime number.")


# 3. Star Pyramids
def star_pyramids():
    print("\n--- Star Pyramid ---")
    rows = int(input("Enter number of rows: "))

    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)


# 4. Character Classification
def character_classification():
    print("\n--- Character Classification ---")
    ch = input("Enter a character: ")

    if len(ch) != 1:
        print("Please enter only one character.")
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            print("It is a vowel.")
        else:
            print("It is a consonant.")
    elif ch.isdigit():
        print("It is a digit.")
    else:
        print("It is a special character.")


# 5. String Operations
def string_operations():
    print("\n--- String Operations ---")
    s = input("Enter a string: ")

    print("Original string:", s)
    print("Uppercase:", s.upper())
    print("Lowercase:", s.lower())
    print("Length:", len(s))
    print("Reversed:", s[::-1])
    print("Title case:", s.title())
    print("Number of words:", len(s.split()))


# 6. Swap Prefixes of Two Strings
def swap_prefixes():
    print("\n--- Swap Prefixes of Two Strings ---")
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    n = int(input("Enter prefix length: "))

    if n < 0 or n > min(len(s1), len(s2)):
        print("Invalid prefix length.")
        return

    result1 = s2[:n] + s1[n:]
    result2 = s1[:n] + s2[n:]

    print("First string after swapping:", result1)
    print("Second string after swapping:", result2)


# 7. Substring Indices
def substring_indices():
    print("\n--- Substring Indices ---")
    s = input("Enter a string: ")
    sub = input("Enter substring to search: ")

    if not sub:
        print("Substring cannot be empty.")
        return

    indices = []
    start = 0

    while True:
        index = s.find(sub, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1

    if indices:
        print("Substring found at indices:", indices)
    else:
        print("Substring not found.")


# 8. Cubes of Even Integers
def cubes_of_even_integers():
    print("\n--- Cubes of Even Integers ---")
    n = int(input("Enter the limit: "))

    print("Even numbers and their cubes:")
    for i in range(2, n + 1, 2):
        print(i, ":", i ** 3)


# 9. File Handling
def file_handling():
    print("\n--- File Handling ---")
    filename = input("Enter file name (default: practical.txt): ")

    if not filename.strip():
        filename = "practical.txt"

    content = input("Enter text to write into file: ")

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        print("Data written successfully.")

        with open(filename, "r", encoding="utf-8") as file:
            print("\nFile contents:")
            print(file.read())

    except OSError as e:
        print("File error:", e)


# 10. Dictionary of Cubes
def dictionary_of_cubes():
    print("\n--- Dictionary of Cubes ---")
    n = int(input("Enter the limit: "))

    cubes = {i: i ** 3 for i in range(1, n + 1)}

    print("Dictionary of cubes:")
    print(cubes)


# 11. Tuple Operations
def tuple_operations():
    print("\n--- Tuple Operations ---")
    values = input("Enter numbers separated by spaces: ")

    numbers = tuple(map(int, values.split()))

    print("Original tuple:", numbers)
    print("Length:", len(numbers))
    print("Maximum:", max(numbers) if numbers else "Empty tuple")
    print("Minimum:", min(numbers) if numbers else "Empty tuple")
    print("Sum:", sum(numbers))
    print("Sorted tuple:", tuple(sorted(numbers)))

    element = int(input("Enter an element to count: "))
    print("Occurrences:", numbers.count(element))
    print("Index:", numbers.index(element)
          if element in numbers else "Element not found")


# 12. Employee Class and Object Counting
class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)


def employee_class():
    print("\n--- Employee Class and Object Counting ---")
    employees = []

    n = int(input("Enter number of employees: "))

    for i in range(n):
        print("\nEmployee", i + 1)
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))

        emp = Employee(name, salary)
        employees.append(emp)

    print("\nEmployee Details:")
    for emp in employees:
        emp.display()
        print()

    print("Total number of employee objects:", Employee.count)


# 13. Class Point2D
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"Point: ({self.x}, {self.y})")

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2
        )


def point2d():
    print("\n--- Class Point2D ---")

    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    p1 = Point2D(x1, y1)
    p2 = Point2D(x2, y2)

    print("First point:")
    p1.display()

    print("Second point:")
    p2.display()

    print("Distance between points:", p1.distance(p2))


# 14. Inheritance: Class Point3D
class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print(f"3D Point: ({self.x}, {self.y}, {self.z})")

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        )


def point3d():
    print("\n--- Inheritance: Class Point3D ---")

    print("Enter first 3D point:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    z1 = float(input("z1: "))

    print("Enter second 3D point:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    z2 = float(input("z2: "))

    p1 = Point3D(x1, y1, z1)
    p2 = Point3D(x2, y2, z2)

    print("First point:")
    p1.display()

    print("Second point:")
    p2.display()

    print("Distance between points:", p1.distance(p2))


# 15. Exception Handling for a Name
def exception_handling_name():
    print("\n--- Exception Handling for a Name ---")

    try:
        name = input("Enter your name: ")

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if not name.replace(" ", "").isalpha():
            raise ValueError("Name must contain only alphabets.")

        print("Hello,", name)

    except ValueError as e:
        print("Invalid input:", e)

    finally:
        print("Program execution completed.")


# Main Menu
def main():
    practicals = {
        1: quadratic_equation,
        2: prime_numbers,
        3: star_pyramids,
        4: character_classification,
        5: string_operations,
        6: swap_prefixes,
        7: substring_indices,
        8: cubes_of_even_integers,
        9: file_handling,
        10: dictionary_of_cubes,
        11: tuple_operations,
        12: employee_class,
        13: point2d,
        14: point3d,
        15: exception_handling_name
    }

    while True:
        print("\n" + "=" * 45)
        print("          PYTHON PRACTICALS MENU")
        print("=" * 45)

        for number, function in practicals.items():
            print(f"{number}. {function.__name__.replace('_', ' ').title()}")

        print("0. Exit")
        print("=" * 45)

        try:
            choice = int(input("Enter your choice (0-15): "))

            if choice == 0:
                print("Thank you for using Python Practicals!")
                break

            if choice in practicals:
                practicals[choice]()
            else:
                print("Invalid choice. Please select between 0 and 15.")

        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
