# Function to check if books can be allocated within 'pageLimit'
def check(arr, k, pageLimit):
    cnt = 1
    pageSum = 0
    for pages in arr:  
        if pageSum + pages > pageLimit:
            cnt += 1
            pageSum = pages
        else:
            pageSum += pages
    return cnt <= k

# Function to find the minimum page limit using binary search
def findPages(arr, k):
    if k > len(arr):
        return -1
    
    minPageLimit = max(arr)
    maxPageLimit = sum(arr)

    # Binary search on the possible page limits
    left, right = minPageLimit, maxPageLimit
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if check(arr, k, mid):
            result = mid  # Store the valid result
            right = mid - 1  # Try for a smaller limit
        else:
            left = mid + 1  # Increase the limit

    return result

# Example usage
if __name__ == "__main__":
    arr = [12, 34, 67, 90]  
    k = 2
    print(findPages(arr, k))  # Output: 113
