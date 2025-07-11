def countPairs(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    cnt = 0
    while left < right:
        sum = arr[left] + arr[right]
        if sum < target:
            cnt += right - left
            left += 1
        else:
            right -= 1
    return cnt

if __name__ == "__main__":
    arr = [2, 1, 8, 3, 4, 7, 6, 5]
    target = 7
    print(countPairs(arr, target))
