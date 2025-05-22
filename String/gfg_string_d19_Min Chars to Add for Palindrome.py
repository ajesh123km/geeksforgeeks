def minChar(s):
    new_s = s + "#" + s[::-1]
    n = len(new_s)
    lps = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and new_s[i] != new_s[j]:
            j = lps[j - 1]
        if new_s[i] == new_s[j]:
            j += 1
            lps[i] = j

    return len(s) - lps[-1]

print(minChar("AACECAAAA"))
