import pytest
from maximum_subarray import maxSubArray

def test_max_subarray_basic_case():
    """Test a basic case with a mix of positive and negative numbers."""
    # The subarray [4, -1, 2, 1] has the largest sum of 6.
    assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_all_positive():
    """Test with an array of all positive numbers."""
    # The largest sum should be the sum of the entire array.
    assert maxSubArray([1, 2, 3, 4]) == 10

def test_max_subarray_all_negative():
    """Test with an array of all negative numbers."""
    # The largest sum is the largest number (closest to zero).
    assert maxSubArray([-1, -2, -3, -4]) == -1

def test_max_subarray_single_element():
    """Test with a single element in the array."""
    assert maxSubArray([5]) == 5
    assert maxSubArray([-5]) == -5

def test_max_subarray_ends_with_large_negative():
    """Test a case where the max subarray is in the middle."""
    assert maxSubArray([1, 2, -1, 4, -10]) == 6

def test_max_subarray_starts_with_large_positive():
    """Test a case where the max subarray is at the beginning."""
    assert maxSubArray([8, -19, 5, 6]) == 11

def test_max_subarray_includes_zero():
    """Test a case that includes zero."""
    assert maxSubArray([-2, 1, -3, 4, 0, 2, 1, -5, 4]) == 7

def test_max_subarray_empty_list():
    """Test with an empty input list, should raise an IndexError."""
    with pytest.raises(IndexError):
        maxSubArray([])