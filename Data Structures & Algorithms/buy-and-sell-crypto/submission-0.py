class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 0
        max_profit = 0

        while i < len(prices):
            while j != len(prices):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
                j+=1
            i+=1
            j=i
        return max_profit 