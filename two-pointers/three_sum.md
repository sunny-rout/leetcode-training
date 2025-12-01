### Intuition

This problem is a natural extension of the "Two Sum" problem. A brute-force approach would involve three nested loops to check every possible triplet of numbers, but this is highly inefficient with a time complexity of O(n³) and makes handling duplicate triplets complicated.

To optimize, the key first step is to sort the input array. Sorting helps in two major ways: it allows us to use a more efficient two-pointer technique to find pairs, and it makes skipping duplicate values straightforward. By fixing one number in the array, the problem is reduced to finding two other numbers that sum up to the negative of the fixed number—essentially, a "Two Sum" problem on the remainder of the array.

### Approach

The solution combines a primary loop with the two-pointer technique on a sorted array.

1.  **Sort the array:** First, sort the input array `nums`. This is crucial for the two-pointer logic and for handling duplicates.
2.  **Iterate with the first pointer:** Loop through the array with an index `i` from the start up to `len(nums) - 2`. This element, `nums[i]`, will be the first number of our potential triplet.
3.  **Skip duplicates:** To avoid duplicate triplets, if the current element `nums[i]` is the same as the previous element `nums[i-1]`, skip it and continue to the next iteration. This check is only performed if `i > 0`.
4.  **Use two pointers for the remaining part:** For each `nums[i]`, initialize a `left` pointer at `i + 1` and a `right` pointer at the end of the array (`len(nums) - 1`).
5.  **Find the pair:** In a `while` loop (while `left < right`), calculate the sum of the three numbers: `current_sum = nums[i] + nums[left] + nums[right]`.
    *   If `current_sum < 0`, the sum is too small, so we need a larger number. Increment the `left` pointer.
    *   If `current_sum > 0`, the sum is too large, so we need a smaller number. Decrement the `right` pointer.
    *   If `current_sum == 0`, we have found a valid triplet. Add `[nums[i], nums[left], nums[right]]` to our result list.
6.  **Skip duplicates for the second and third numbers:** After finding a valid triplet, we must move the pointers and skip any subsequent duplicate elements to avoid adding the same triplet multiple times. Increment `left` and then continue incrementing it as long as it's less than `right` and points to the same value as the previous `left` element.

### Complexity

*   **Time complexity:** O(n²)
    The initial sort takes O(n log n). The main part of the algorithm is the nested loop structure: the outer loop runs `n` times, and the inner two-pointer loop runs, at most, `n` times for each outer iteration. This results in a dominant time complexity of O(n²).

*   **Space complexity:** O(1) or O(n)
    The space complexity depends on the implementation of the sorting algorithm. If the sorting is done in-place, the space complexity is O(1) (excluding the storage for the output). If a sorting algorithm that uses extra space is used, it could be up to O(n).