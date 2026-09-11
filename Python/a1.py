##Guess the number game

import random

attempts = 7
number = random.randint(1,100)
attempt = 0


def rules():
    print("Welcome to the Guessing Number Game!")
    print("Guess the random number between 0 and 100 (included).")
    print("You will receive hints if your guess is too high or too low.")
    print("Let's begin!")

def play():
    print("Let's play!")


def lesgo():
    global attempt
    guess = int(input(f"Make your guess: " ))
    if guess > number:
        print("It's lower" )
        return False
    elif guess < number:
        print("It's higher!")
        return False
    elif guess == number:
        print (f'Congrats! The answer is {guess}')
        return True

### 

rules()

while attempt <= attempts:
    if lesgo():
        break
    attempt += 1
else:
    print(f'Game over! The answer was: {number}')







