class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        max_profit = 0
        for i in range(len(prices)):
            curr = prices[i]
            for j in range(i+1, len(prices)):
                if curr < prices[j]:
                    # profit possible
                    max_profit = max(max_profit, prices[j] - curr)
        return max_profit
