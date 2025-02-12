class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashmap={}
        for i, n in enumerate(nums):
            s = sum([int(x) for x in str(n)])
            if s in hashmap:
                hashmap[s].append(n)
            else:
                hashmap[s] = [n]
        max_sum = -1
        for x,y in hashmap.items():
            if len(y) >= 2:
                y.sort(reverse=True)
                max_sum = max(max_sum,y[0]+y[1])
        return max_sum