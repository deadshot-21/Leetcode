class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])

        fresh = 0
        queue = deque()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                if grid[i][j] == 1:
                    fresh+=1
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        minutes=0
        while queue:
            i,j, minutes = queue.popleft()
            for ni, nj in directions:
                if 0<=i+ni<r and 0<=j+nj<c and grid[i+ni][j+nj] == 1:
                    grid[i+ni][j+nj] = 2
                    fresh -= 1
                    queue.append((i+ni,j+nj,minutes+1))
        
        return minutes if not fresh else -1
            