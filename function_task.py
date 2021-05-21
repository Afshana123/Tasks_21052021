# Build a simple calculator class containing add, subtract, multiple and divide

def add(value1, value2):
    return value1 + value2

print(add(2, 3))

def subtract(value1, value2):
    return value1 - value2

print(subtract(9, 5))

def multiply(value1, value2):
    return value1 * value2

print(multiply(2, 3))

def divide(value1, value2):
    return value1 / value2

print(divide(10, 5))


# Create a function that works out whether a number is divisible by another and returns the value True or False
def is_number_divisible(value1, value2):
    if value1 % value2 == 0:
        return True
    else:
        return False

print(is_number_divisible(20, 5))
print(is_number_divisible(7, 2))

# Create a function that works out and returns the area of a triangle

def area_of_triangle(height, base):
    return 1/2 * base * height * 2.54

print(area_of_triangle(5, 2))