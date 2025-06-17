class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in closeToOpen.values():
                stack.append(c) 
            else:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
