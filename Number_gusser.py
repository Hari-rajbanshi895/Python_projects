import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

elif top_of_range <= 0:
    print("Please enter the number above 0")

else:
    print('Enter number next time')
    quit()

random_number = random.randint(0,top_of_range)

guesses = 0
while True:
    guesses += 1
    user_input = input("Make your guess: ")
    if user_input.isdigit():
        user_input = int(user_input)

    else:
        print('Enter number next time')
        continue

    if user_input  == random_number :
            print('You won!')
            break
    else:
        if user_input > random_number:
             print('You were above')
        else:
             print('you were below')


print("you got", guesses, "incorrect")



