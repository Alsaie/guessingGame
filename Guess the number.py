#Guess the number
from random import randrange

number = randrange(20)

while True:
    guess = int(input("What is your guess? "))
    if number == guess:
        print("Correct!")
        break
    print('Smaller, try again!' if (number < guess) else 'Bigger, try again!')
