from typing import List

# Slowest solution with cubic complexity O(n^3)
def subarray_sum_n3(nums: List[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j + 1]) == k:
                count += 1
    return count

# Improved solution with quadratic complexity O(n^2)
def subarray_sum_n2(nums: List[int], k: int) -> int:
    count = 0
    for start in range(len(nums)):
        current_sum = 0
        for end in range(start, len(nums)):
            current_sum += nums[end]
            if current_sum == k:
                count += 1
    return count

# Optimal solution with linear complexity O(n)
def subarray_sum_n(nums: List[int], k: int) -> int:
    count, current_sum = 0, 0
    sum_dict = {0: 1}  # Prefix sum and frequency map

    for num in nums:
        current_sum += num
        count += sum_dict.get(current_sum - k, 0)
        sum_dict[current_sum] = sum_dict.get(current_sum, 0) + 1
    
    return count

if __name__ == '__main__':
    unsorted_array = [7, 2, -5, 1, 1, -1, 5, -5]
    k = 5

    result_n3 = subarray_sum_n3(unsorted_array, k)
    result_n2 = subarray_sum_n2(unsorted_array, k)
    result_n = subarray_sum_n(unsorted_array, k)

    print(f"n^3: {result_n3}, n^2: {result_n2}, n: {result_n}")  # Expected output: 5, 5, 5
