class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the boundary indexes for the search
        left, right = 0, len(nums) - 1
      
        # Use binary search to find the target
        while left < right:
            # Calculate the middle index
            mid = (left + right) // 2  # Updated to use floor division for clarity

            # Determine if the mid element is in the rotated or sorted part
            if nums[0] <= nums[mid]:
                # If target is between the first element and mid, go left
                if nums[0] <= target <= nums[mid]:
                    right = mid
                # Else, go right
                else:
                    left = mid + 1
            else:
                # If target is between mid and last element, go right
                if nums[mid] < target <= nums[-1]:  # Use -1 for last element index
                    left = mid + 1
                # Else, go left
                else:
                    right = mid
      
        # Check if the left index matches the target, otherwise return -1
        return left if nums[left] == target else -1