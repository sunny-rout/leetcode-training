### Intuition

The problem requires checking if a string reads the same backward as it does forward, after ignoring case and filtering out all non-alphanumeric characters.

A simple approach would be to first process the string by creating a new, filtered version that only contains lowercase alphanumeric characters. Then, we could easily check if this new string is equal to its reverse. However, this method requires allocating extra memory for the new string.

A more optimal and memory-efficient approach is to use two pointers. By placing one pointer at the beginning of the string and another at the end, we can move them toward the center, comparing characters as we go. We'll just need to add logic to skip over any non-alphanumeric characters we encounter.

### Approach

The two-pointer method avoids using extra memory and checks the string in a single pass.

1. Initialize two pointers: `left` at the start of the string (index 0) and `right` at the end (index `len(s) - 1`).
2. Loop as long as `left` is less than `right`.
3. Inside the loop, advance the `left` pointer until it points to an alphanumeric character.
4. Similarly, move the `right` pointer backward until it points to an alphanumeric character.
5. Compare the characters at the `left` and `right` pointers, ignoring case (e.g., by converting both to lowercase). If they are not the same, the string is not a palindrome, and we can return `False`.
6. If the characters match, move the `left` pointer forward and the `right` pointer backward to continue checking the rest of the string.
7. If the loop completes without finding any mismatches, it means the string is a palindrome, and we return `True`.

### Complexity

* **Time complexity:** O(n)
  In the worst case, each pointer will traverse the entire string once.

* **Space complexity:** O(1)
  This approach uses only a constant amount of extra space for the two pointers, making it highly memory-efficient compared to the method of creating a new filtered string (which would be O(n)).