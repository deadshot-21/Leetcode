class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        op=0
        x = heapq.heappop(nums)
        while x < k:
            y = heapq.heappop(nums)
            heapq.heappush(nums, x*2 + y)
            op+=1
            x = heapq.heappop(nums)
        return op