# Import typing List to specify the type of the input nums.
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Initialize variables to store the maximum triplet value, the maximum number encountered so far,
        # and the maximum difference between the maximum number and the current number.
        max_triplet_value = 0
        max_number = 0
        max_difference = 0
      
        # Iterate through each number in the input list.
        for number in nums:
            # Calculate the maximum triplet value by taking the maximum between the current max_triplet_value
            # and the product of max_difference and the current number.
            max_triplet_value = max(max_triplet_value, max_difference * number)
          
            # Update max_number if the current number is greater than the max_number seen so far.
            max_number = max(max_number, number)
          
            # Update max_difference which is the maximum difference found between max_number and any number.
            max_difference = max(max_difference, max_number - number)
      
        # Return the maximum possible triplet value found.
        return max_triplet_value