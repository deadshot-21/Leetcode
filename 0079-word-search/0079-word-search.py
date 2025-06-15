class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c, k):
            if k == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:
                return False
            
            original_char = board[r][c]
            board[r][c] = '#'
            
            found = (dfs(r + 1, c, k + 1) or # Down
                     dfs(r - 1, c, k + 1) or # Up
                     dfs(r, c + 1, k + 1) or # Right
                     dfs(r, c - 1, k + 1))   # Left
            
            board[r][c] = original_char
            
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True 
                        
        return False