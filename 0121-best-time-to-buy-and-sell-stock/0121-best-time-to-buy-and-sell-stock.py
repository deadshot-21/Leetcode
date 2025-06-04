class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        mPrice=0
        while r<len(prices):
            if prices[l] < prices[r]:
                mPrice = max(mPrice,prices[r] - prices[l])
            else:
                l=r
            r+=1
        return mPrice