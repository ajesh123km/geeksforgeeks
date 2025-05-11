def getMinDiff(arr, k):
    if not arr: return 0
    arr.sort()
    res = arr[-1] - arr[0]

    for i in range(1, len(arr)):
        if arr[i] < k: continue
        res = min(res, max(arr[i-1] + k, arr[-1] - k) - min(arr[0] + k, arr[i] - k))
    
    return res

# Example usage
arr, k = [12, 6, 4, 15, 17, 10], 6
print("Minimum Maximum Difference:", getMinDiff(arr, k))
