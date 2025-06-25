MAX_CHAR = 26

def getHash(s):
    freq = [0] * MAX_CHAR
    for ch in s:
        freq[ord(ch) - ord('a')] += 1
    return '$'.join(map(str, freq))

def anagrams(arr):
    res = []
    mp = {}
    for i in range(len(arr)):
        key = getHash(arr[i])
        if key not in mp:
            mp[key] = len(res)
            res.append([])
        res[mp[key]].append(arr[i])
    return res

if __name__ == "__main__":
    arr = ["act", "god", "cat", "dog", "tac"]
    res = anagrams(arr)
    for group in res:
        for word in group:
            print(word, end=" ")
        print()
