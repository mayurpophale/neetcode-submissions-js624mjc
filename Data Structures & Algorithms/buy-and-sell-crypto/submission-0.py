class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPro = 0
        for i in prices:
            if minPrice > i:
                minPrice = i
            current_profit = i - minPrice
            maxPro = max(maxPro,current_profit)

        return maxPro
