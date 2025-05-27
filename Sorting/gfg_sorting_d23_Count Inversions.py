class Solution:
    def countandmerge(self, arr, l, m, r):
        n1, n2, left, right = m-l+1, r-m, arr[l:m+1], arr[m+1:r+1]
        i, j, k, res = 0, 0, l, 0
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                res += (n1 - i)
                j += 1
            k += 1
            
        # Merging remaining elements (these loops must be outside the main while loop)
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
        return res  # Return after merging is fully done
        
    def countinv(self, arr, l, r):
        if l >= r:
            return 0
        m = (r + l) // 2
        return self.countinv(arr, l, m) + self.countinv(arr, m+1, r) + self.countandmerge(arr, l, m, r)

    def inversionCount(self, arr):
        return self.countinv(arr, 0, len(arr)-1)

# Example Usage:
arr = [2, 4, 1, 3, 5]
obj = Solution()
print(obj.inversionCount(arr))  # Expected Output: 3
