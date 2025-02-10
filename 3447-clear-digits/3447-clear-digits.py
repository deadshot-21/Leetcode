class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        # Make a stack of non digit characters and pop when a digit arrives. 
        # Poppping the last element is equivalent to removing the left 
        # non digit character
        for c in s:
            if c.isdigit():
                ans.pop()
            else:
                ans.append(c)

        return ''.join(ans)