def mimic (my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

#This doesn't show up in terminal since its only print would show output in terminal
mimic('Hi')

print(mimic('Hello!'))

def mimic1 (my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    # have to put greater than or equal to since the index is 1 less than the number
    if len(my_words) <= letter_idx:
        return ("Index too high")
    return my_words[letter_idx]

print(mimic1('present', 4))

