# User function Template for Python3
class Solution:
    def search(self, pat, txt):
        m, n = len(pat), len(txt)
        lps = [0] * m
        res = []

        # Preprocess the pattern (calculate lps[] array) 
        length = 0  # length of the previous longest prefix suffix
        for i in range(1, m):
            while length > 0 and pat[i] != pat[length]:
                length = lps[length - 1]
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length

        # Search the pattern in the text  
        i = j = 0
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
            if j == m:
                res.append(i - j)
                j = lps[j - 1]
            elif i < n and txt[i] != pat[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return res

# Example usage
if __name__ == "__main__":
    txt = "aabaacaadaabaaba"
    pat = "aaba"
    solution = Solution()
    result = solution.search(pat, txt)
    print(result)  # Output: [0, 9, 12]
