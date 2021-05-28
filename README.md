# Tasks 

## Function Task

- Build a basic Object Orientated Calculator
- Phase 1: build a simple calculator class containing add, subtract, multiply, divide.
- Phase 2: expand by creating:
- Divisible by method that returns true or false dependent on the outcome
- Work out and return the area of a triangle
- Inch to cm converter
- NOTE -> Must be in class and method format

```python
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
```
## Fizzbuzz Challenge

- Write a program that prints the numbers from 1 to 100.
- For multiples of five prince "Buzz" instead of a number
- For numbers which are multiples of both three and five print "FizzBuzz"
- For multiples of three print '"Fizz" instead of a number

```python
# Writing a python program that prints number from 1 to 100

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
```

## Writing a python program that prints number from 1 to 100

*Control flow age and permission task*

*Control Flow Age and Permission*

Timings 30 Minutes

#### Summary
Simple program to use control flow!

#### Tasks
rules of what the program is supose to do are followed,see bellow
Starter code
`
age = 19
driver_lisence = True

- You can vote and drivre
- You can vote
- You can driver
- you can't legally drink but your mates/uncles might have your back (bigger 16)
- Your too young, go back to school!
as a user I should be able to keep being prompted for input until I say 'exit'
`

#### Acceptance Criteria
- is a program that run continuously
- handles strings and integers
- has exist condition
- all business logic works

```python
user_prompt = True
while user_prompt:
    age = input("Welcome, please enter your age otherwise type 'exit' to close the program: ")
    if age == "exit":
        user_prompt = False
        break
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide your answer in digits. ")
    if age.isdigit() and int(age) >= 17:
        drivers_license = input("Do you have a driver's license? Y/N ")
        if drivers_license == "Y" and int(age) >= 18:
            print("You can vote and drive")
        if drivers_license == "Y" and int(age) == 17:
            print("You can drive. You can't legally drink but your mates or uncles might have your back!")
        if drivers_license == "N" and int(age) >= 18:
            print("You can vote")
        if drivers_license == "N" and int(age) == 17:
            print("You can't legally drink but your mates or uncles might have your back!")
        user_prompt = True
        continue
    if age.isdigit() and int(age) < 17:
       print("You're too young, go back to school!")
       user_prompt = True
       continue

print("Thank you for using our service.")
```