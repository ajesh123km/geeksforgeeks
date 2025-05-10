
from typing import List

def maximumProfit(prices: List[int]) -> int:
    res = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:  # Add profit when price increases
            res += prices[i] - prices[i - 1]
    return res

# Define prices before calling the function
prices1 = [100, 180, 260, 310, 40, 535, 695]
print("Maximum Profit for prices1:", maximumProfit(prices1))  # Expected Output: 865
prices2 = [4, 2, 2, 2, 4]
print("Maximum Profit for prices2:", maximumProfit(prices2)) 
