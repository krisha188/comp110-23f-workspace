"""One Shot Wordle. """

__author__ = "730656379"

secret: str = "python"

word_guess: str = input(f"What is your {len(secret)}-letter guess? ")

# prints this if the word length isn't the same as the secret variable's word length
while len(word_guess) != len(secret):
    word_guess = str(input(f"That was not {len(secret)} letters! Try again: " ))

#emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_of_guess: int = 0
emoji_string: str = ""

while index_of_guess < len(secret):
    # if the letter of the guess is in the same position as the letter in secret
    if word_guess[index_of_guess] == secret[index_of_guess]: 
        emoji_string = emoji_string + GREEN_BOX 
    else:
        # when a letter of guess is in secret, but in the wrong place
        guessed_character = False
        alternative_index: int = 0
        while not (guessed_character) and alternative_index < len(secret):
            if secret[alternative_index] == word_guess[index_of_guess]:
                guessed_character = True
            alternative_index = alternative_index + 1
        if guessed_character:
            emoji_string = emoji_string + YELLOW_BOX
        # when letter in guess isn't in secret
        else:
            emoji_string = emoji_string + WHITE_BOX
    index_of_guess = index_of_guess + 1

print(emoji_string)

# the guess is wrong
if word_guess != secret:
    print("Not quite. Play again soon!")
    exit()
# guess is right
else:
    print("Woo! You got it!")

