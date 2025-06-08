class Solution:
    def isPalindrome(self, x: int) -> bool:
        l,r = 0,len(str(x))-1
        while l<=r:
            if str(x)[l] != str(x)[r]:
                return False
            l+=1
            r-=1
        return True