"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730656379"

word_guess: str = input("Enter a 5-character word: ")

if len(word_guess) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else: 
    len(word_guess) == 5

letter_guess: str = input("Enter a single character: ")

if len(letter_guess) != 1:
    print("Error: Character must be a single character.")
    exit()
else: 
    len(letter_guess) == 1

print("Searching for " + letter_guess + " in " + word_guess)

number_matching_letters: int = 0

if letter_guess == word_guess[0]:
    number_matching_letters = number_matching_letters + 1
    print(letter_guess + " found at index 0")
else: 
    letter_guess != word_guess[0]

if letter_guess == word_guess[1]:
    number_matching_letters = number_matching_letters + 1
    print(letter_guess + " found at index 1")
else: 
    letter_guess != word_guess[1]

if letter_guess == word_guess[2]:
    number_matching_letters = number_matching_letters + 1
    print(letter_guess + " found at index 2")
else: 
    letter_guess != word_guess[2]

if letter_guess == word_guess[3]:
    number_matching_letters = number_matching_letters + 1
    print(letter_guess + " found at index 3")
else: 
    letter_guess != word_guess[3]

if letter_guess == word_guess[4]:
    number_matching_letters = number_matching_letters + 1
    print(letter_guess + " found at index 4")
else: 
    letter_guess != word_guess[4]

if number_matching_letters > 1:
    print(str(number_matching_letters) + " instances of " + letter_guess + " found in " + word_guess)
else:
    number_matching_letters != 0
    if number_matching_letters == 1:
        print(str(number_matching_letters) + " instance of " + letter_guess + " found in " + word_guess)
    else:
        print("No instances of " + letter_guess + " found in " + word_guess)
