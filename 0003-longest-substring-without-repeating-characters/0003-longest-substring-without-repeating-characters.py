class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r, c in enumerate(s):
            while c in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(c)
            res = max(res,r-l+1)
        return res
        
