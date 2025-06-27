def countSubarrays(arr, k):
    prefixSums = {}
    res = 0
    currSum = 0

    for val in arr:
        currSum += val
        if currSum == k:
            res += 1
        if currSum - k in prefixSums:
            res += prefixSums[currSum - k]
        prefixSums[currSum] = prefixSums.get(currSum, 0) + 1

    return res

if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    k = -10
    print(countSubarrays(arr, k))
