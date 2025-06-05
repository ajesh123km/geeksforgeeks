def kthElement(a, b, k):
    arr = []
    
    for i in a:
        arr.append(i)
    
    for i in b:
        arr.append(i)
    
    arr.sort()
    
    return arr[k - 1]
    

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5
    print(kthElement(a, b, k))
