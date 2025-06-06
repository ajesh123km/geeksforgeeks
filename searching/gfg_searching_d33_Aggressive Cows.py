class Solution:
    def check(self, stalls, k, dist):
        cnt = 1
        prev = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - prev >= dist:
                prev = stalls[i]
                cnt += 1
        return cnt >= k

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        lo, hi = 1, stalls[-1] - stalls[0]
        res = 0

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.check(stalls, k, mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return res

# Example Usage
stalls = [1, 2, 4, 8, 9]
k = 3
solution = Solution()
print(solution.aggressiveCows(stalls, k))  # Output: 3
