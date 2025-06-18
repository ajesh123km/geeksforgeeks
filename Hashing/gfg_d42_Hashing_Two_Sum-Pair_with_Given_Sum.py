def twoSum(arr, target):
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2

    print("true" if twoSum(arr, target) else "false")
