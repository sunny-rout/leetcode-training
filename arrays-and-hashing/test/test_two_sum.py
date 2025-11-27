import pytest
import sys
import os

from two_sum import twoSum


def test_twoSum_basic_case():
    """Test a basic case where the solution is found."""
    assert sorted(twoSum([2, 7, 11, 15], 9)) == [0, 1]


def test_twoSum_at_end():
    """Test when the pair is at the end of the list."""
    assert sorted(twoSum([3, 2, 4], 6)) == [1, 2]


def test_twoSum_with_negative_numbers():
    """Test with negative numbers in the input list."""
    assert sorted(twoSum([-1, -3, 5, 90], 4)) == [0, 2]


def test_twoSum_with_zero():
    """Test when the target can be formed with a zero."""
    assert sorted(twoSum([5, 2, 0, 4], 4)) == [2, 3]


def test_twoSum_with_duplicate_numbers():
    """Test when the input list contains duplicate numbers."""
    assert sorted(twoSum([3, 3], 6)) == [0, 1]


def test_twoSum_no_solution():
    """Test a case where no two numbers add up to the target."""
    assert twoSum([1, 2, 3, 4], 8) is None


def test_twoSum_empty_list():
    """Test with an empty input list."""
    assert twoSum([], 10) is None
