class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res = 0
        for num in nums:
            freq[num] += 1
        for key in freq:
            if key + 1 in freq:
                res = max(res, freq[key] + freq[key + 1])
        return res