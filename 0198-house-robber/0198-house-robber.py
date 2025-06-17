class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rb1,rb2=0,0

        for n in nums:
            temp = max(n+rb1,rb2)
            rb1 = rb2
            rb2 = temp
        return rb2