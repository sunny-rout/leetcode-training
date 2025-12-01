import pytest
from container_with_most_water import MaxArea

def test_max_area_basic_case():
    """Test the example from the problem description."""
    # The max area is formed by the lines at index 1 (height 8) and index 8 (height 7).
    # The width is 7, and the height is min(8, 7) = 7. Area = 7 * 7 = 49.
    assert MaxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

def test_max_area_simple_case():
    """Test a simple case with two elements."""
    assert MaxArea([1, 1]) == 1

def test_max_area_all_same_height():
    """Test a case where all heights are the same."""
    # The widest container will have the max area. Width = 3, height = 4. Area = 12.
    assert MaxArea([4, 4, 4, 4]) == 12

def test_max_area_descending_heights():
    """Test a case with descending heights."""
    # The widest container (9, 5) gives area 4 * 5 = 20.
    assert MaxArea([9, 8, 7, 6, 5]) == 20

def test_max_area_ascending_heights():
    """Test a case with ascending heights."""
    # The widest container (5, 9) gives area 4 * 5 = 20.
    assert MaxArea([5, 6, 7, 8, 9]) == 20

def test_max_area_empty_and_single_element_list():
    """Test edge cases with empty and single-element lists."""
    assert MaxArea([]) == 0
    assert MaxArea([10]) == 0
