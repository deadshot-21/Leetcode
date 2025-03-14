class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Initialize left to 0 (minimum possible result) and 
        # right to the maximum number of candies in any pile
        left, right = 0, max(candies)

        # Binary search for the highest number of candies per child
        while left < right:
            # Mid is the number of candies to distribute per child; add 1 and 
            # shift right by 1 to get the upper middle for even numbers
            mid = (left + right + 1) // 2
          
            # Count how many children can receive 'mid' number of candies
            count = sum(candy // mid for candy in candies)
          
            # If the number of children that can receive 'mid' candies is at least k,
            # mid can be a potential answer, so we move left pointer up to mid
            if count >= k:
                left = mid
            # Otherwise, we decrease the right pointer, as we need less candies per child
            else:
                right = mid - 1
      
        # left is now the maximum number of candies per child that we can distribute
        return left