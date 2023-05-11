import pytest
from functions.merge_sorted_lists import merge_sorted_lists

def test_merges_lists():
    # Arrange
    l1 = [1]
    l2 = [2]

    # Act
    answer = merge_sorted_lists(l1, l2)

    # Assert
    assert answer == [1, 2]


def test_merges_reordered_lists():
    # Arrange
    l1 = [2]
    l2 = [1]

    # Act
    answer = merge_sorted_lists(l1, l2)

    # Assert
    assert answer == [1, 2]


def test_for_longer_lists():
    # Arrange
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]

    # Act
    answer = merge_sorted_lists(l1, l2)

    # Assert
    assert answer == [1, 2, 3, 4, 5, 6]