def mergeOverlap(arr):
    # Sort intervals by the start value
    arr.sort(key=lambda x: x[0])
    
    res = []
    
    for start, end in arr:
        if res and res[-1][1] >= start:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])
    
    return res


arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
res = mergeOverlap(arr)
for interval in res:
    print(interval[0], interval[1])
