class Solution:
    def getHappyString(self, length: int, index: int) -> str:
        # Helper function for depth-first search to find all happy strings
        def dfs(current_str):
            # Base condition: if current string reaches the desired length, add to results
            if len(current_str) == length:
                happy_strings.append(current_str)
                return
            # Iterate through all possible characters
            for char in 'abc':
                # Avoid repeating characters
                if current_str and current_str[-1] == char:
                    continue
                # Recursively build the string
                dfs(current_str + char)

        # List to store all possible happy strings
        happy_strings = []
        # Start the DFS with an empty string
        dfs('')
        # If there are fewer than k happy strings, return an empty string
        # Otherwise, return the k-th happy string (1-indexed)
        return '' if len(happy_strings) < index else happy_strings[index - 1]