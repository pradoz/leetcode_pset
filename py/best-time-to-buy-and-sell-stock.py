# O(n^2) runtime, O(1) space. brute force check every possibility
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        N = len(prices)
        for i in range(N):
            for j in range(i+1, N):
                profit = prices[j] - prices[i]
                total_profit = max(total_profit, profit)
        return total_profit


# O(n) solution, O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = max_price = 0
        for price in reversed(prices):
            max_price = max(max_price, price)
            total_profit = max(total_profit, max_price - price)
        return total_profit

