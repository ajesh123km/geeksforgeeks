class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        pivot = -1

        # Step 1: Identify pivot—the first element from the right that is smaller than its next element.
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break

        # If no valid pivot is found, it means the array is in descending order.
        if pivot == -1:
            arr.reverse()
            return

        # Step 2: Find the smallest element greater than arr[pivot] to the right of the pivot.
        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        # Step 3: Reverse the sub-array (suffix) to the right of the pivot.
        left, right = pivot + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Correctly instantiate the class and call the method.
sol = Solution()              # Create an instance of the class.
arr = [2, 4, 1, 7, 5, 0]      # Input array.
sol.nextPermutation(arr)      # Use the instance to call the method.
print(" ".join(map(str, arr)))  # Expected output: "2 4 5 0 1 7"
