def hIndex(citations):
    citations.sort(reverse=True)
    return sum(c > i for i, c in enumerate(citations))
citations = [6, 0, 3, 5, 3]
print(hIndex(citations))   
