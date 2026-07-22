class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            # This would check if there are any cheaper buy prices from indicies 0
            if buy_price > prices[i]:
                buy_price = prices[i]
            # Check current profit if higher than max profit
            max_profit = max(max_profit, prices[i] - buy_price)

        return max_profit            

        