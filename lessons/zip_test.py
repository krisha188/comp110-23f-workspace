"""Test my zip function."""
__author__ = "730656379"

from lessons.zip import zip


def test_unequal_lists() -> None:
    """Test if zip shows {} when given lists of unequal lengths."""
    assert zip(['happy', 'life'], [1, 2, 3, 4]) == {}


def test1_zip() -> None:
    """Test if zip makes a dictionary when given two lists."""
    assert zip(['a', 'b', 'c'], [1, 2, 3]) == {'a': 1, 'b': 2, 'c': 3}


def test2_zip() -> None:
    """Tests if zip makes a dictionary when given two lists."""
    assert zip(['March', 'April', 'May', 'June'], [3, 4, 5, 6]) == {'March': 3, 'April': 4, 'May': 5, 'June': 6}
