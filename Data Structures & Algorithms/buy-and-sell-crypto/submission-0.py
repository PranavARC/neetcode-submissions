class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n), since the pointers iterate down the list and we never go over the same element twice
        # Space: O(1), since nothing is stored besides the max_profit
        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit <= 0:
                left = right
            else:
                max_profit = max(max_profit, profit)    
            right += 1
        
        return max_profit
