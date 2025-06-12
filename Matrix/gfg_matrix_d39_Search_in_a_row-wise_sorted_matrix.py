class Solution:
    def search(self, arr, x):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if x == arr[mid]:
                return True
            if x < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False

    def searchRowMatrix(self, mat, x):
        n, m = len(mat), len(mat[0])
        for i in range(n):
            if self.search(mat[i], x):  # Use self.search instead of search
                return True
        return False

if __name__ == "__main__":
    ob = Solution()
    mat = [[3, 4, 9],
           [2, 5, 6],
           [9, 25, 27]]
    x = 9
    if ob.searchRowMatrix(mat, x):
        print("true")
    else:
        print("false")
