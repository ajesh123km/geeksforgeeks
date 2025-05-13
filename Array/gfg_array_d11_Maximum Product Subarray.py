class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        max_prod = arr[0]
        min_temp = arr[0]
        max_temp = arr[0]
        
        for i in range(1, n):
            if arr[i] < 0:
                min_temp, max_temp = max_temp, min_temp  # Swap when encountering negative numbers
            
            max_temp = max(arr[i], max_temp * arr[i])
            min_temp = min(arr[i], min_temp * arr[i])
            
            max_prod = max(max_prod, max_temp)
        
        return max_prod

arr = [-2, 6, -3, -10, 0, 2]
ob = Solution()
print(ob.maxProduct(arr))
