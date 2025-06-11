def matSearch(mat, x):
    n = len(mat)
    m = len(mat[0])
  
    for i in range(n):
        for j in range(m):
            if mat[i][j] == x:
                return True
  
    return False

if __name__ == "__main__":
    mat = [[3, 30, 38],
           [20, 52, 54],
           [35, 60, 69]]
    x = 35
    print("true" if matSearch(mat, x) else "false")
