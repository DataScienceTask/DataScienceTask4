import pytest

from unique_element import find_unique


def test_single_element():
    assert find_unique([42]) == 42


def test_unique_at_beginning():
    assert find_unique([5, 1, 1, 2, 2]) == 5


def test_unique_in_middle():
    assert find_unique([1, 2, 3, 4, 3, 1, 2]) == 4


def test_unique_at_end():
    assert find_unique([1, 3, 1, 3, 2]) == 2


def test_unique_zero():
    assert find_unique([4, 0, 4, 2, 2]) == 0


def test_negative_numbers():
    assert find_unique([-1, -3, 2, -1, -7, -3, 2]) == -7


def test_large_numbers():
    assert find_unique([787042, -14159265, 787042, -123456789, -14159265]) == -123456789


def test_large_input():
    unique = 99999
    arr = [i for i in range(1000)] * 2
    arr.append(unique)
    assert find_unique(arr) == unique
