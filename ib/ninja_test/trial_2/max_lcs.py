class Solution:
    # @param A : string
    # @return a list of integers
    def maxLCS(self, A):
        N = len(A)

        dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, N + 1):
#                print('%s, %s, %s, %s' %(i - 1, N - j, A[i - 1], A[N - j]))
                if A[i - 1] == A[N - j] and N - j > i - 1:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        max_val = dp[-1][-1]

        if max_val == 0:
            return [1, 0]

        for i in range(len(dp)):
            for j in range(i + 1, len(dp)):
                if dp[i][j] == max_val:
                    return [i, max_val]

        return [1, 0]

print(Solution().maxLCS('abc')) # [1, 0]
print(Solution().maxLCS('abba')) # [2, 2]
