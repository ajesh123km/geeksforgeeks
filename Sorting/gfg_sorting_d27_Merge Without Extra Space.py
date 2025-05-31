def mergeArrays(a, b):
    i = len(a) - 1
    j = 0

    while i >= 0 and j < len(b):
        if a[i] < b[j]:
            i -= 1
        else:
            a[i], b[j] = b[j], a[i]
            i -= 1
            j += 1

    a.sort()
    b.sort()

if __name__ == "__main__":
    a = [1, 5, 9, 10, 15, 20]
    b = [2, 3, 8, 13]
    mergeArrays(a, b)

    for ele in a:
        print(ele, end=' ')
    print()
    for ele in b:
        print(ele, end=' ')
