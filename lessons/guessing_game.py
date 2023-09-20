"""Program that loops until correct number is guessed"""

from random import randint

secret: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))

number_of_tries: int = 0
max_tries: int = 3
#repeats 4 times since we started at 0, could start at 1 to have 3 tries, or in the while loop make the upper bound max_tries - 1

# now the while operation has two requirments)
while (guess != secret) and (number_of_tries < max_tries):
    print("Wrong!")
    #if guess is out of bounds, let them know
    if(guess < 1) or (guess < 10):
        print("That is not between 1 and 10!")
    if guess < secret:
        print("Too low!")
    else: #could also use elif here (elif guess > secret), don't need to though as the condition for the while loop is that guess doesn't equal secret
        print("Too high!")
    #Ask for another number
    guess = int(input("Guess again: "))
    number_of_tries += 1

# If you reach this point then guess == secret
# you keep repeating the while loop until its false

if guess == secret:
    print("You guessed correctly!")
else:
    print("You lose")

#exit an infinate loop (press control c)