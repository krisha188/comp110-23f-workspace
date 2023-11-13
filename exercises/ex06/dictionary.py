"""Exercise with dictionaries."""
__author__ = "730656379"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary with the keys and values inverted."""
    inverted: dict[str, str] = {}
    keys: list[str] = []

    for value in x:
        keys.append(x[value])

    for key in x:
        inverted[x[key]] = key

    i = 0
    while i < len(keys):
        j = 0
        while j < len(keys):
            if i != j and keys[i] == keys[j]:
                raise KeyError("Dictionary cannot have two of the same keys!")
            j += 1
        i += 1

    return inverted


def favorite_color(x: dict[str, str]) -> str:
    """Returns the most popular color."""
    empty_dict: dict[str, int] = {}

    for key in x:
        if x[key] in empty_dict:
            empty_dict[x[key]] += 1
        else:
            empty_dict[x[key]] = 1

    counter = 0
    tie = []

    for i in empty_dict:
        if empty_dict[i] > counter:
            counter = empty_dict[i]
    
    for i in empty_dict:
        if empty_dict[i] == counter:
            tie.append(i)
   
    return tie[0]


def count(x: list[str]) -> dict[str, int]:
    """Returns a dictionary with the count of the times the string appears in the inputed list."""
    empty_dict: dict[str, int] = {}

    for key in x:
        if key in empty_dict:
            empty_dict[key] += 1
        else:
            empty_dict[key] = 1
    return empty_dict


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary with the first letters of each of the words in the list and the multiple words associated with that letter."""
    alphabetized_dict: dict[str, list[str]] = {}

    for key in x:
        y = key[0].lower()
        if y in alphabetized_dict:
            alphabetized_dict[y].append(key)
        else:
            alphabetized_dict[y] = [key]
    return alphabetized_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the attendence of the person on a certain day."""
    if day in attendance:
        if student in attendance[day]:
            return attendance
    else:
        if day in attendance:
            attendance[day] += [student]
        else:
            attendance[day] = [student]
    return attendance