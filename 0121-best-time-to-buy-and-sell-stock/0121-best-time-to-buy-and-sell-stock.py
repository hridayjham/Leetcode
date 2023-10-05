class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxprofit = 0
        
        while (right < len(prices)):
            if prices[right] < prices[left]:
                left = right
            elif prices[right] - prices[left] > maxprofit:
                maxprofit = prices[right] - prices[left]
            right += 1
                
        return maxprofit
        