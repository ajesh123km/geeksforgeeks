def findMajority(arr):
    n, freq = len(arr), {}
    for ele in arr:
        freq[ele] = freq.get(ele, 0) + 1

    res = sorted([ele for ele, cnt in freq.items() if cnt > n // 3])
    return res


arr = [2, 2, 3, 1, 3, 2, 1, 1]
print(*findMajority(arr))
