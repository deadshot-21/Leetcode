class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        N = len(ratings)
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                candies[i] = max(candies[i-1]+1, candies[i])
        
        for i in range(N-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1]+1,candies[i])
        
        return sum(candies)
                
                    
