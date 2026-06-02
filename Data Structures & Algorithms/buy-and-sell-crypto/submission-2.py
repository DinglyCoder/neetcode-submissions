class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]

        for i in prices:
            maxProfit = max(maxProfit, i - buyPrice)

            buyPrice = min(buyPrice, i)
        
        return maxProfit