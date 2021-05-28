'''
Checklist

- [x] You can vote and drive
- [x] You can vote
- [x] You can drive
- [x] you can't legally drink but your mates/uncles might have your back (bigger 16)
- [x] You're too young, go back to school!
- [x] as a user I should be able to keep being prompted for input until I say 'exit'
- [x] is a program that will run continuously until you enter 'exit'

'''

# Age for voting is 18+ years
# Age 17+ for driving a car
# voting and driving > 18

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
