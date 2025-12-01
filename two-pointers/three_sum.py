
def ThreeSum(nums):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        l, r = i+1, n-1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                
    return result

if __name__ == "__main__":
    nums_input = input("Enter a list of numbers separated by spaces: ")
    nums_list = [int(x) for x in nums_input.split()]

    result = ThreeSum(nums_list)
    print(f"The triplets that sum to zero are: {result}")