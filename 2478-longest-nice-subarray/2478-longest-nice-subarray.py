from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # Initialize the maximum length of the subarray, the current start of the subarray, 
        # and the mask used to track unique bits
        max_length = start_index = bit_mask = 0
      
        # Enumerate over the list of numbers
        for end_index, number in enumerate(nums):
            # While there is a common bit set in bit_mask and the current number
            while bit_mask & number:
                # Remove the bits of nums[start_index] from bit_mask
                bit_mask ^= nums[start_index]
                # Move the start_index forward as those bits are no longer part of the subarray
                start_index += 1
            # Update max_length if we've found a longer subarray that's nice
            max_length = max(max_length, end_index - start_index + 1)
            # Include the bits of the current number in the bit_mask
            bit_mask |= number
          
        # Return the length of the longest nice subarray
        return max_length