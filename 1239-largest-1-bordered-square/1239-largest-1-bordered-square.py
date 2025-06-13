class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # dp_left[r][c] stores the number of consecutive 1s to the left of grid[r][c]
        dp_left = [[0] * cols for _ in range(rows)]
        # dp_top[r][c] stores the number of consecutive 1s to the top of grid[r][c]
        dp_top = [[0] * cols for _ in range(rows)]

        # Populate dp_left and dp_top tables
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dp_left[r][c] = dp_left[r][c-1] + 1 if c > 0 else 1
                    dp_top[r][c] = dp_top[r-1][c] + 1 if r > 0 else 1
        
        max_side = 0

        # Iterate from bottom-right to top-left to find the largest square
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                # 's' is the maximum possible side length of a square ending at (r, c)
                # ensuring the right and bottom borders are solid 1s.
                s = min(dp_left[r][c], dp_top[r][c])

                # Check for smaller squares from 's' down to 1
                while s > max_side: # Optimization: no need to check squares smaller than max_side found so far
                    # Check if the top border is solid 1s
                    # The top-left corner would be (r - s + 1, c - s + 1)
                    # The cell (r - s + 1, c) needs to have at least 's' 1s to its left (including itself)
                    if dp_left[r - s + 1][c] >= s and \
                       dp_top[r][c - s + 1] >= s:
                        max_side = s
                        break  # Found the largest square for this (r, c), move to next cell
                    s -= 1
        
        return max_side * max_side