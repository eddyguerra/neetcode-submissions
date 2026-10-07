class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0 
        l,r=0,1
        profit=0
        maxProfit=0

        while r< len(prices):
            profit = prices[r]-prices[l]
            maxProfit= max(profit,maxProfit)

            if prices[l]>prices[r]:
                l=r
            r+=1
        return maxProfit