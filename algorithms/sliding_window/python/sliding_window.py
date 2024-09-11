from typing import List, Tuple

# Kadane's algorithm
def get_max_sum_range(nums: List[int]) -> Tuple[int, int, int]: # O(n)
    if not nums:
        return (0, -1, -1)
    
    max_sum = current_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return (max_sum, start, end)

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, start_idx, end_idx = get_max_sum_range(nums)
    print(f"Maximum sum: {max_sum}, Range: [{start_idx}, {end_idx}]")

