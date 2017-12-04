class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(1, len(A) + 1):
                if A[i - 1] == A[j - 1] and i != j:
                    dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        if dp[-1][-1] >= 2:
            return 1

        return 0


print(Solution().anytwo("abab") == 1)
print(Solution().anytwo("abba") == 0)
print(Solution().anytwo("abbxxxa") == 1)
