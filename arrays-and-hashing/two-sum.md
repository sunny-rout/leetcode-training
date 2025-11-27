### Intuition

A brute-force approach of checking every pair of numbers results in a time complexity of O(n²), which is inefficient for large input arrays. To optimize, we need a way to quickly check if the complement of a number (i.e., `target - current_number`) has already been seen. A hash map is the ideal data structure for this, providing average O(1) time complexity for lookups. By storing numbers we've already encountered and their indices, we can instantly determine if we've found a valid pair.

### Approach

We can solve this problem in a single pass using a hash map.

1. Initialize an empty hash map to store numbers from the array as keys and their corresponding indices as values.
2. Iterate through the array from left to right.
3. For each number `num` at index `i`, calculate its complement: `complement = target - num`.
4. Check if the `complement` exists in the hash map.
   - If it does, we have found the two numbers that add up to the target. We can return the index of the complement stored in the hash map and the current index `i`.
   - If it does not, add the current number `num` and its index `i` to the hash map.

This one-pass approach ensures that by the time we encounter the second number of the pair, the first number is already in the hash map, allowing us to find the solution efficiently.

### Complexity

* **Time complexity:** O(n)
    We iterate through the array of `n` elements only once. Each lookup and insertion in the hash map takes, on average, O(1) time.

- **Space complexity:** O(n)
    In the worst-case scenario, we might have to store all `n` elements of the array in the hash map before finding the pair.
