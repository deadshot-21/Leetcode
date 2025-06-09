class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        count = 0
        def dfs(i,j):
            if i>=r or i<0 or j<0 or j>=c or grid[i][j] != "1":
                return
            
            grid[i][j] = "2"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count+=1
        return count