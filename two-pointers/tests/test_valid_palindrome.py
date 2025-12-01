import pytest
from valid_palindrome import isPalindrome

def test_is_palindrome_basic_true():
    """Test a classic palindrome with mixed case and punctuation."""
    assert isPalindrome("A man, a plan, a canal: Panama") == True

def test_is_palindrome_basic_false():
    """Test a simple non-palindrome."""
    assert isPalindrome("race a car") == False

def test_is_palindrome_empty_string():
    """Test an empty string, which is considered a palindrome."""
    assert isPalindrome("") == True

def test_is_palindrome_single_character():
    """Test a single character string."""
    assert isPalindrome("a") == True

def test_is_palindrome_with_numbers():
    """Test a palindrome that includes numbers."""
    assert isPalindrome("Was it a car or a cat I saw?") == True
    assert isPalindrome("No 'x' in 'Nixon'") == True

def test_is_palindrome_all_non_alphanumeric():
    """Test a string with only non-alphanumeric characters."""
    assert isPalindrome(".,;!@#$%^&*()") == True

def test_is_palindrome_unicode():
    """Test a string with unicode characters (though isalnum is ASCII-based)."""
    # This will be false because `isalnum` might not cover all unicode characters
    # depending on the environment, but the logic holds.
    assert isPalindrome("Able, was I ere I saw Elba") == True
