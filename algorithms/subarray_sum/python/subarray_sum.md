# Subarray Sum

Given an array of integers `nums` and an integer `k`, count the total number of continuous subarrays whose sum equals `k`.

## Problem Description

We need to find all contiguous subarrays in a given array that sum up to a specific target value `k`. This problem tests our ability to optimize algorithms and use data structures effectively.

## Approaches

### 1. Brute Force (O(n^3))

```python
def subarray_sum_n3(nums: List[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j + 1]) == k:
                count += 1
    return count
```

This approach checks all possible subarrays. It's straightforward but inefficient for large inputs.

### Optimized Brute Force (O(n^2))

```python
def subarray_sum_n2(nums: List[int], k: int) -> int:
    count = 0
    for start in range(len(nums)):
        current_sum = 0
        for end in range(start, len(nums)):
            current_sum += nums[end]
            if current_sum == k:
                count += 1
    return count
```

This improves on the first approach by keeping a running sum, eliminating one loop.

### Optimal Solution (O(n))

```python
def subarray_sum_n(nums: List[int], k: int) -> int:
    count, current_sum = 0, 0
    sum_dict = {0: 1}  # Prefix sum and frequency map
    for num in nums:
        current_sum += num
        count += sum_dict.get(current_sum - k, 0)
        sum_dict[current_sum] = sum_dict.get(current_sum, 0) + 1
    return count
```

This solution uses a hash map to store cumulative sums, allowing for a single-pass solution.

### Explanation

The optimal solution works by maintaining a running sum and a dictionary of sum frequencies. When we find that `current_sum - k` exists in our dictionary, it means we've found a subarray with sum `k`.

### Example

```python
if __name__ == '__main__':
    unsorted_array = [7, 2, -5, 1, 1, -1, 5, -5]
    k = 5
    result_n3 = subarray_sum_n3(unsorted_array, k)
    result_n2 = subarray_sum_n2(unsorted_array, k)
    result_n = subarray_sum_n(unsorted_array, k)
    print(f"n^3: {result_n3}, n^2: {result_n2}, n: {result_n}")  # Expected output: 5 5 5
```
For the input array [7, 2, -5, 1, 1, -1, 5, -5] and k = 5, there are 5 subarrays that sum to 5:
1. [7, 2, -5, 1]
2. [7, 2, -5, 1, 1, -1]
3. [1, -1, 5]
4. [5]
5. [7, 2, -5, 1, 1, -1, 5, -5]