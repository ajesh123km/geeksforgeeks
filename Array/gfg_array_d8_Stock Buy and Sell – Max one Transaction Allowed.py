class Solution:
    def maximumProfit(self, prices):
        if not prices:  # Handling empty list case
            return 0
        
        min_so_far = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            min_so_far = min(min_so_far, prices[i])
            max_profit = max(max_profit, prices[i] - min_so_far)   
        
        return max_profit

# Example Usage:
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print("Maximum Profit:", solution.maximumProfit(prices))
