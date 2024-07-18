class Solution:
    def maxProfit(self, prices) -> int:

        min = 10001
        max = 0

        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > max:
                max = prices[i] - min

        return max
