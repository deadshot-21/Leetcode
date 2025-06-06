class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for c in s:
            if s_stack and c == "#":
                s_stack.pop()
            elif c != "#":
                s_stack.append(c)
        for c in t:
            if t_stack and c == "#":
                t_stack.pop()
            elif c != "#":
                t_stack.append(c)
        return s_stack == t_stack