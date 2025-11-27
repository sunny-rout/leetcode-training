import pytest
from group_anagrams import groupAnagramsASCII, groupAnagramsChar

def sort_and_compare(result, expected):
    """Helper function to sort nested lists for comparison."""
    sorted_result = sorted([sorted(group) for group in result])
    sorted_expected = sorted([sorted(group) for group in expected])
    return sorted_result == sorted_expected

@pytest.mark.parametrize("group_anagrams_func", [groupAnagramsASCII, groupAnagramsChar])
def test_group_anagrams_basic_case(group_anagrams_func):
    """Test a basic case with multiple anagram groups."""
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    result = group_anagrams_func(input_strs)
    assert sort_and_compare(result, expected)



@pytest.mark.parametrize("group_anagrams_func", [groupAnagramsASCII, groupAnagramsChar])
def test_group_anagrams_empty_list(group_anagrams_func):
    """Test with an empty input list."""
    input_strs = []
    expected = []
    result = group_anagrams_func(input_strs)
    assert sort_and_compare(result, expected)


@pytest.mark.parametrize("group_anagrams_func", [groupAnagramsASCII, groupAnagramsChar])
def test_group_anagrams_no_anagrams(group_anagrams_func):
    """Test a case where no strings are anagrams of each other."""
    input_strs = ["abc", "def", "ghi"]
    expected = [["abc"], ["def"], ["ghi"]]
    result = group_anagrams_func(input_strs)
    assert sort_and_compare(result, expected)


@pytest.mark.parametrize("group_anagrams_func", [groupAnagramsASCII, groupAnagramsChar])
def test_group_anagrams_all_anagrams(group_anagrams_func):
    """Test a case where all strings are anagrams of each other."""
    input_strs = ["listen", "silent", "enlist"]
    expected = [["listen", "silent", "enlist"]]
    result = group_anagrams_func(input_strs)
    assert sort_and_compare(result, expected)


@pytest.mark.parametrize("group_anagrams_func", [groupAnagramsASCII, groupAnagramsChar])
def test_group_anagrams_with_empty_strings(group_anagrams_func):
    """Test with empty strings in the input list."""
    input_strs = ["", "b", ""]
    expected = [["", ""], ["b"]]
    result = group_anagrams_func(input_strs)
    assert sort_and_compare(result, expected)

@pytest.mark.parametrize("group_anagrams_func", [groupAnagramsASCII, groupAnagramsChar])
def test_group_anagrams_single_string(group_anagrams_func):
    """Test with a single string in the input list."""
    input_strs = ["hello"]
    expected = [["hello"]]
    result = group_anagrams_func(input_strs)
    assert sort_and_compare(result, expected)
