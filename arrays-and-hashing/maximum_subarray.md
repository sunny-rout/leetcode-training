### Intuition

The problem is to find the contiguous sub-array within an array of numbers that has the largest sum. A brute-force method would be to check every possible sub-array, but this is inefficient, with a time complexity of O(n²) or even O(n³).

A more optimal solution, known as Kadane's Algorithm, can solve this in a single pass (O(n)). The core idea is that a sub-array with a negative sum will never contribute positively to a larger sub-array's sum. Therefore, if the running sum of our current sub-array becomes negative, it's better to discard it and start a new sub-array from the next element. This effectively creates a "sliding window" that expands and resets as we iterate through the array.

### Approach

We can implement this with two variables: one to keep track of the maximum sum found so far (`max_sum`) and another for the sum of the current sub-array (`current_sum`).

1. Initialize `max_sum` to the first element of the array and `current_sum` to 0.
2. Iterate through each number in the array.
3. If `current_sum` becomes negative at any point, reset it to 0. This is because a negative prefix will not help in finding the maximum sum.
4. Add the current number to `current_sum`.
5. After adding the current number, compare `current_sum` with `max_sum`. If `current_sum` is greater, update `max_sum`.
6. After iterating through all the numbers, `max_sum` will hold the largest sub-array sum.

### Complexity

* **Time complexity:** O(n)
  We iterate through the input array of `n` elements only once.

* **Space complexity:** O(1)
  The algorithm uses only a few variables to store the current and maximum sums, so it does not require any extra space proportional to the input size.