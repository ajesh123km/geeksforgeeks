from bisect import bisect_left, bisect_right

def countFreq(arr, target):
    l = bisect_left(arr, target)
    r = bisect_right(arr, target)
    return r - l
    

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    target = 2
    print(countFreq(arr, target))
