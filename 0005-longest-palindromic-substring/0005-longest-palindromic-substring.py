class Solution:
    def longestPalindrome(self, s: str) -> str:
        lmax, rmax = 0, 0
        for i, c in enumerate(s):
            l = r = i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > rmax-lmax+1:
                    lmax, rmax = l, r
                l-=1
                r+=1
            
            l , r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > rmax-lmax+1:
                    lmax, rmax = l, r
                l-=1
                r+=1
        return s[lmax:rmax+1]