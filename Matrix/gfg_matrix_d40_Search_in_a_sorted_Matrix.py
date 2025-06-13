def searchMatrix(mat, x):
    n = len(mat)
    m = len(mat[0])

    lo, hi = 0, n * m - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        row = mid // m
        col = mid % m

        if mat[row][col] == x:
            return True

        if mat[row][col] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return False

if __name__ == "__main__":
    mat = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
    x = 14

    print("true" if searchMatrix(mat, x) else "false")
