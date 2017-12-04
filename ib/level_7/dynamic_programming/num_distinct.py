class Solution:
    # @param S : string
    # @param T : string
    # @return an integer
    def numDistinct(self, S, T):
        dp = [[0 for _ in range(len(T))] for _ in range(len(S))]

        if len(S) < len(T):
            return 0

        if S[0] == T[0]:
            dp[0][0] = 1

        for i in range(1, len(S)):
            if S[i] == T[0]:
                dp[i][0] = dp[i-1][0] + 1
            else:
                dp[i][0] = dp[i-1][0]

        for i in range(1, len(S)):
            for j in range(1, min(i + 1, len(T))):
                if S[i] == T[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]

print(Solution().numDistinct("rabbbit", "rabbit") == 3)
print(Solution().numDistinct("rabbbaaaiitititiiiaaait", "rabbit") == 51)
print(Solution().numDistinct("aaaababbababbaabbaaababaaabbbaaabbb", "bbababa") == 22113)
