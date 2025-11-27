

from typing import List, Optional

def twoSum(nums: List[int], target: int) -> Optional[List[int]]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


if __name__ == "__main__":
    try:
        nums_input = input("Enter a list of numbers separated by spaces: ")
        nums_list = [int(x) for x in nums_input.split()]

        target_input = input("Enter the target number: ")
        target_num = int(target_input)

        result = twoSum(nums_list, target_num)

        if result:
            print(f"The indices of the two numbers that add up to {target_num} are: {result}")
        else:
            print(f"No two numbers in the list add up to {target_num}.")
    except ValueError:
        print("Invalid input. Please enter integers for the numbers and the target.")
