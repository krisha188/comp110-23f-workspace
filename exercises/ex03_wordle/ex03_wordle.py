"""Wordle!"""

__author__ = "730656379"


def contains_char(word: str, letter: str) -> bool: 
    """This function checks if letter is in word."""
    assert len(letter) == 1
    idx: int = 0
    while idx < len(word):
        if word[idx] == letter:
            return True
        idx = 1 + idx
    else: 
        return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """This function that returns an emoji string telling if the letters are in the right place."""
    assert len(guess) == len(secret)
    idx1: int = 0
    emoji_string: str = ''
    while idx1 < len(guess):
        if guess[idx1] == secret[idx1]:
            emoji_string = emoji_string + GREEN_BOX
        elif contains_char(secret, guess[idx1]) is True:
            emoji_string = emoji_string + YELLOW_BOX
        else: 
            emoji_string = emoji_string + WHITE_BOX
        idx1 = 1 + idx1
    return emoji_string


def input_guess(expected_length: int) -> str:
    """This function gives a input for which you guess a word of a certain length."""
    enter_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(enter_guess) != expected_length:
        wrong_guess: str = input(f"That wasn't {expected_length} chars! Try again: ")
        enter_guess = wrong_guess
    return enter_guess


secret: str = "codes"


def main() -> None:
    """This function ties the other functions together to crete wordle."""
    number_of_guesses = 1
    right_or_wrong = False
    while number_of_guesses < 7:
        print(f"=== Turn {number_of_guesses}/6 ===")
        x = input_guess(len(secret))
        print(emojified(x, secret))
        if x == secret:
            print(f"You won in {number_of_guesses}/6 turns") 
            right_or_wrong is True
            return
        number_of_guesses = number_of_guesses + 1
    if right_or_wrong is False:
        print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()