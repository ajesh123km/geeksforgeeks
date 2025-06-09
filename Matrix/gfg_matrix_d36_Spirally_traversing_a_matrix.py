def spirallyTraverse(mat):
    m = len(mat)
    n = len(mat[0])

    res = []
    vis = [[False] * n for _ in range(m)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c = 0, 0
    idx = 0

    for _ in range(m * n):
        res.append(mat[r][c])
        vis[r][c] = True

        newR, newC = r + dr[idx], c + dc[idx]

        if 0 <= newR < m and 0 <= newC < n and not vis[newR][newC]:
            r, c = newR, newC
        else:
            idx = (idx + 1) % 4
            r += dr[idx]
            c += dc[idx]

    return res


if __name__ == "__main__":
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

    res = spirallyTraverse(mat)
    print(" ".join(map(str, res)))
