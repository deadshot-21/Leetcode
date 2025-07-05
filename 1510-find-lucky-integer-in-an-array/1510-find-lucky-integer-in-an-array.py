class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        cnt = -1
        for n in arr:
            hashmap[n] = 1 + hashmap.get(n,0)
        for k,v in hashmap.items():
            if k == v:
                cnt = max(cnt,k)
        return cnt