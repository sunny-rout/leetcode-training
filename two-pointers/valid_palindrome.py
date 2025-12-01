def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters ignoring case
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    result = isPalindrome(input_str)
    print(f"Is the string a palindrome? {result}")