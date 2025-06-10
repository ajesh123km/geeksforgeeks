def rotateMatrix(mat):
    n = len(mat)
    
    for row in mat:
        row.reverse()

    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

if __name__ == "__main__":
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

    rotateMatrix(mat)

    for row in mat:
        print(" ".join(map(str, row)))
