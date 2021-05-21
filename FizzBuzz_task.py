'''
Write a program that prints the numbers from 1 to 100. But:
For multiples of three print '"Fizz" instead of a number
For multiples of five prince "Buzz" instead of a number
For numbers which are multiples of both three and five print "FizzBuzz"
'''

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