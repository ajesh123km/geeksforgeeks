def kthMissing(arr, k):
    s = set(arr)
    count = 0
    curr = 0

    while count < k:
        curr += 1
        if curr not in s:
            count += 1
    
    return curr


if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(kthMissing(arr, k))
