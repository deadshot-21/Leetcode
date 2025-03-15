from typing import List
from bisect import bisect_left

class Solution:
    # This function aims to find the minimum capability required to form k pairs
    def minCapability(self, nums: List[int], k: int) -> int:
      
        # The inner function 'is_feasible' checks if a given capability 'capability'
        # is sufficient to form at least k pairs.
        def is_feasible(capability):
            count, last_used_index = 0, -2  # Initialize counters
            for current_index, value in enumerate(nums):
                # Skip if the value is greater than the capability or if the element
                # is right after the previously used element (to ensure non-adjacency).
                if value > capability or current_index == last_used_index + 1:
                    continue
                # If neither condition is met, increment the count
                # and update 'last_used_index'.
                count += 1
                last_used_index = current_index
            # Check if the capability is sufficient to form k pairs.
            return count >= k

        # Perform a binary search over the range [0, max(nums) + 1),
        # using the 'is_feasible' function as the key.
        # The 'bisect_left' will find the leftmost value in the range
        # where 'is_feasible' returns True (i.e., the minimum capability).
        return bisect_left(range(max(nums) + 1), True, key=is_feasible)