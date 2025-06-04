class Solution:
  def maxFrequency(self, nums: list[int], k: int) -> int:

    def kadane(nums, target, k):
        maxSum = 0
        sum = 0
        for num in nums:
            if num == target:
                sum += 1
            elif num == k:
                sum -= 1
            if sum < 0: 
                sum = 0
            maxSum = max(maxSum, sum)
        return maxSum

    return nums.count(k) + max(kadane(nums, target, k)
                               for target in range(1, 51)
                               if target != k)