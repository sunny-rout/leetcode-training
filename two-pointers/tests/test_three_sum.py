import pytest
from three_sum import ThreeSum

def sort_results(result):
    """Sorts a list of lists to ensure a stable comparison."""
    return sorted([sorted(triplet) for triplet in result])

def test_three_sum_basic_case():
    """Test a standard case with multiple solutions."""
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    result = ThreeSum(nums)
    assert sort_results(result) == sort_results(expected)

def test_three_sum_no_solution():
    """Test a case where no triplets sum to zero."""
    nums = [1, 2, 3, 4]
    expected = []
    result = ThreeSum(nums)
    assert result == expected

def test_three_sum_with_zeros():
    """Test a case with multiple zeros, which should result in one triplet."""
    nums = [0, 0, 0, 0]
    expected = [[0, 0, 0]]
    result = ThreeSum(nums)
    assert sort_results(result) == sort_results(expected)

def test_three_sum_with_duplicates():
    """Test a case with duplicates to ensure the output contains unique triplets."""
    nums = [-2, 0, 0, 2, 2]
    expected = [[-2, 0, 2]]
    result = ThreeSum(nums)
    assert sort_results(result) == sort_results(expected)

def test_three_sum_empty_and_short_lists():
    """Test edge cases with empty and short lists."""
    assert ThreeSum([]) == []
    assert ThreeSum([1, -1]) == []