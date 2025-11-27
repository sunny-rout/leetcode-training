### Intuition

The core idea is to find a unique signature for each group of anagrams. Anagrams are words that contain the same characters with the same frequencies. A straightforward way to identify them is to realize that if we sort the letters of two anagrams, the resulting strings will be identical.

However, sorting every string can be computationally expensive. A more optimal approach is to use character counts. Since the problem often specifies lowercase English letters, we can use a fixed-size array (of size 26) to count the occurrences of each character. This count array serves as a unique identifier for all strings in an anagram group.

### Approach

We can use a hash map to group the anagrams, with the character count acting as the key.

1. Initialize a hash map where keys will represent character counts and values will be lists of strings. In Python, a `defaultdict(list)` is ideal for this, as it simplifies appending to lists for new keys.
2. Iterate through each string in the input list.
3. For each string, create a character count array of 26 zeros.
4. Iterate through the characters of the current string and increment the corresponding index in the count array (e.g., `ord(char) - ord('a')`).
5. Since lists are mutable and cannot be used as dictionary keys in Python, convert the count array to an immutable tuple.
6. Use this tuple as a key in the hash map and append the original string to the list associated with that key.
7. After iterating through all the strings, the values of the hash map will be the lists of grouped anagrams.

### Complexity

* **Time complexity:** O(m * n)
    Where `m` is the number of strings in the input list and `n` is the average length of a string. This is because we iterate through each of the `m` strings and then iterate through their `n` characters to build the count array.

* **Space complexity:** O(m * n)
    In the worst case, we need to store all the characters of all the strings in our hash map.
