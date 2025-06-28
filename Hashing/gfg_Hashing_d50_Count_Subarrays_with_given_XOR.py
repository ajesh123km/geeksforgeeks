def subarrayXor(arr, k):
    res = 0
    for i in range(len(arr)):
        prefXOR = 0
        for j in range(i, len(arr)):
            prefXOR ^= arr[j]
            if prefXOR == k:
                res += 1
    return res

if __name__ == "__main__":
    arr = [4, 2, 2, 6, 4]
    k = 6
    print(subarrayXor(arr, k))
