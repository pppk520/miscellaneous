class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        dp = [99999999999] * len(A)
        dp[0] = 0
        
        for row in A:
            tmp = 99999999999999
            for i in range(len(row)):
                t = min(tmp, dp[i]) + row[i]
                tmp = dp[i]
                dp[i] = t

        return min(dp)


arr = [
     [2],
     [3,4],
     [6,5,7],
     [4,1,8,3]
]

print(Solution().minimumTotal(arr) == 11)

