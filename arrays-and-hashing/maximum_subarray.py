from typing import List

def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        if current_sum < 0:
            current_sum = 0

        current_sum += num
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    nums_input = input("Enter a list of numbers separated by spaces: ")
    nums_list = [int(x) for x in nums_input.split()]

    result = maxSubArray(nums_list)
    print(f"The maximum subarray sum is: {result}")