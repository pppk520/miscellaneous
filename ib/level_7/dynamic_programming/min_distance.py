class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        dp = [[9999 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

        for i in range(len(A) + 1):
            dp[i][0] = i

        for i in range(len(B) + 1):
            dp[0][i] = i

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return dp[-1][-1]


print(Solution().minDistance("", "") == 0)
print(Solution().minDistance("", "A") == 1)
print(Solution().minDistance("Anshuman", "Antihuman") == 2)
print(Solution().minDistance("Ansandnadkeiieiiekdkhuman", "AdkjaikeAdlkekentihuman") == 16)
