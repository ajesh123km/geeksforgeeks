def findMin(arr):
    res = arr[0]

    for i in range(1, len(arr)):
        res = min(res, arr[i])
    return res

if __name__ == "__main__":
    arr = [5, 6, 1, 2, 3, 4]
    print(findMin(arr))
