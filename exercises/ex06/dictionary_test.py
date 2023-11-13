"""Testing the dictionaries I wrote!"""
__author__ = "730656379"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance
from exercises.ex06.dictionary import count
import pytest


def test_invert1() -> None:
    """Test if invert will actually change the keys to values and values to keys."""
    assert invert({'w': 'd', 'x': 'a', 'y': 'b', 'z': 'c'}) == {'d': 'w', 'a': 'x', 'b': 'y', 'c': 'z'}


def test_invert2() -> None:
    """Test if function returns an empty dict when given empty dict."""
    assert invert({}) == {}


with pytest.raises(KeyError):
    """Checks if the function raises a key error when there are multiple of the same values."""
    my_dictionary = {'Frank': 'Bell', 'Rachel': 'Bell'}
    invert(my_dictionary)


def test_invert3() -> None:
    """Test if invert will actually change the keys to values and values to keys."""
    assert invert({'w': 'd'}) == {'d': 'w'}


def test_favorite_color1() -> None:
    """Test if most frequent color is returned."""
    assert favorite_color({'Alice': "Blue", "Tim": "White", "Elvis": "Blue"}) == "Blue"


def test_favorite_color2() -> None:
    """Test if most frequent color is returned."""
    assert favorite_color({'Ted': "White", "Tim": "White", "Tech": "White"}) == "White"


def test_favorite_color_if_tie() -> None:
    """Test if all tied colors are returned."""
    assert favorite_color({'Alice': "Blue", "Tim": "White", "Elvis": "Green"}) == "Blue"


def test_count1() -> None:
    """Test if the function returns a dictionary with the count of the times the string appears in the inputed list."""
    assert count(['x', 'y', 'x']) == {'x': 2, "y": 1}


def test_count2() -> None:
    """Test if the function returns a dictionary with the count of the times the string appears in the inputed list."""
    assert count(['x', 'y', 'y', 'w', 'w', 'z', 'z', 'w', 'z']) == {'x': 1, "y": 2, 'w': 3, 'z': 3}


def test_count_tie() -> None:
    """Test if the function returns a dictionary with the count of the times the string appears in the inputed list, when all the counts are the same."""
    assert count(['x', 'y', 'z']) == {'x': 1, "y": 1, "z": 1}


def test_alphabetizer1() -> None:
    """Returns the first letter of the word, then all the words that begin with that letter."""
    assert alphabetizer(['bat', 'cat', 'tat']) == {'b': ['bat'], 'c': ['cat'], 't': ['tat']}


def test_alphabetizer2() -> None:
    """Returns the first letter of the word, then all the words that begin with that letter."""
    assert alphabetizer(['cold', 'snow', 'trey', 'under']) == {'c': ['cold'], 's': ['snow'], 't': ['trey'], 'u': ['under']}


def test_alphabetizer_cases() -> None:
    """Returns the first letter of the word, then all the words that start with that letter regardless of casing."""
    assert alphabetizer(['Tat', 'bat', 'cat', 'tee']) == {'b': ['bat'], 'c': ['cat'], 't': ['Tat', 'tee']}


def test_update_attendance1() -> None:
    """Check if the function updates the attendance when given the student name and when they attended class."""
    assert update_attendance({"Monday": ["Brinda", "Ariel"]}, "Tuesday", "Evelyn") == {'Monday': ['Brinda', 'Ariel'], 'Tuesday': ['Evelyn']}


def test_update_attendance2() -> None:
    """Check if the function updates the attendance when given the student name and when they attended class."""
    assert update_attendance({"Tuesday": ["Brinda"], "Wednesday": ["Ariel"]}, "Thursday", "Evelyn") == {'Tuesday': ['Brinda'], 'Wednesday': ['Ariel'], 'Thursday': ['Evelyn']}


def test_update_attendance() -> None:
    """Check if the function does no update the attendance when given the same name within the day."""
    assert update_attendance({"Monday": ["Brinda", "Ariel"]}, "Monday", "Brinda") == {'Monday': ['Brinda', 'Ariel']}