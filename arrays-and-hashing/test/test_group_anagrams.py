import pytest
from group_anagrams import groupAnagrams

def sort_and_compare(result, expected):
    """Helper function to sort nested lists for comparison."""
    sorted_result = sorted([sorted(group) for group in result])
    sorted_expected = sorted([sorted(group) for group in expected])
    return sorted_result == sorted_expected

def test_group_anagrams_basic_case():
    """Test a basic case with multiple anagram groups."""
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    result = groupAnagrams(input_strs)
    assert sort_and_compare(result, expected)

def test_group_anagrams_empty_list():
    """Test with an empty input list."""
    input_strs = []
    expected = []
    result = groupAnagrams(input_strs)
    assert sort_and_compare(result, expected)

def test_group_anagrams_no_anagrams():
    """Test a case where no strings are anagrams of each other."""
    input_strs = ["abc", "def", "ghi"]
    expected = [["abc"], ["def"], ["ghi"]]
    result = groupAnagrams(input_strs)
    assert sort_and_compare(result, expected)

def test_group_anagrams_all_anagrams():
    """Test a case where all strings are anagrams of each other."""
    input_strs = ["listen", "silent", "enlist"]
    expected = [["listen", "silent", "enlist"]]
    result = groupAnagrams(input_strs)
    assert sort_and_compare(result, expected)

def test_group_anagrams_with_empty_strings():
    """Test with empty strings in the input list."""
    input_strs = ["", "b", ""]
    expected = [["", ""], ["b"]]
    result = groupAnagrams(input_strs)
    assert sort_and_compare(result, expected)

def test_group_anagrams_single_string():
    """Test with a single string in the input list."""
    input_strs = ["hello"]
    expected = [["hello"]]
    result = groupAnagrams(input_strs)
    assert sort_and_compare(result, expected)
