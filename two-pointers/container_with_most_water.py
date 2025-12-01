
def MaxArea(height) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        current_area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

if __name__ == "__main__":
    height_input = input("Enter a list of heights separated by spaces: ")
    height_list = [int(x) for x in height_input.split()]

    result = MaxArea(height_list)
    print(f"The maximum area is: {result}")
