class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        min_buy = prices[0]
        for sell in prices:
            maxP = max(maxP, sell - min_buy)
            min_buy = min(min_buy, sell)
        return maxP