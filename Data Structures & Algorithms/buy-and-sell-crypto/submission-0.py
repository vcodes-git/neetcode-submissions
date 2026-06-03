class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = [0] * len(prices)
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > best[i]:
                    best[i] = prices[j] - prices[i]
        return max(best)


            

        