class Solution:
    def findTriplets(self, arr):
        map = {}
        ans = []
        for j in range(len(arr)):
            for k in range(j + 1, len(arr)):
                val = -1 * (arr[j] + arr[k])
                if val in map:
                    for i in map[val]:
                        ans.append([i, j, k])
            if arr[j] not in map:
                map[arr[j]] = []
            map[arr[j]].append(j)
        return ans

arr = [0, -1, 2, -3, 1]
sol = Solution()
res = sol.findTriplets(arr)
for triplet in res:
    print(triplet[0], triplet[1], triplet[2])
