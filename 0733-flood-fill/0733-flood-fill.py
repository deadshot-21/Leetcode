class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r,c = len(image), len(image[0])
        curr_color = image[sr][sc]
        def dfs(i,j):
            if i >= r or i < 0 or j>=c or j<0 or image[i][j] != curr_color:
                return
            print(i,j)
            image[i][j] = color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        if curr_color != color:
            dfs(sr,sc)
        return image
