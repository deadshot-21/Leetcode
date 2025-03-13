from typing import List
from bisect import bisect_left

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # This function checks if it's possible to make the array zero
        # by applying the first 'k' queries
        def check(k: int) -> bool:
            # Initialize a difference array with an extra element for boundary management
            difference_array = [0] * (len(nums) + 1)
          
            # Apply each query's effect to the difference array
            for left, right, value in queries[:k]:
                difference_array[left] += value
                difference_array[right + 1] -= value
          
            # Accumulate the changes from the difference array
            accumulated_sum = 0
            for original_value, change in zip(nums, difference_array):
                accumulated_sum += change
                # Check if the accumulated value can zero out the original array value
                if original_value > accumulated_sum:
                    return False
            return True

        # Determine the number of queries
        num_queries = len(queries)
      
        # Use binary search to find the minimum number of queries needed
        l = bisect_left(range(num_queries + 1), True, key=check)
      
        # Return -1 if not possible, otherwise return the minimum queries needed
        return -1 if l > num_queries else l