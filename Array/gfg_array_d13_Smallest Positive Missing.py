class Solution:
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        arr.sort()

        res = 1  # Start with the smallest positive number
        for num in arr:
            if num == res:
                res += 1
            elif num > res:
                break  # If num > res, res cannot be in the array

        return res
sol = Solution()
arr = [2, -3, 4, 1, 1, 7]
print(sol.missingNumber(arr))  # Output: 3

