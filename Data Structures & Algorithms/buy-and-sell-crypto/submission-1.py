class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, h = 0, 1
        max_profit = 0

        while h < len(prices):
            if prices[l] < prices[h]:
                profit = prices[h] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l=h
            h+=1
        return max_profit
