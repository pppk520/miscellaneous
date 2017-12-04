class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

        dp[0][0] = 1

        for i in range(1, len(A)+1):
            if A[i - 1] == C[i - 1]:
                dp[i][0] = 1
            else:
                break

        for j in range(1, len(B)+1):
            if B[j - 1] == C[j - 1]:
                dp[0][j] = 1
            else:
                break

        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                try:            
                    if C[i + j - 1] == B[j - 1] and dp[i][j-1] == 1:
                        dp[i][j] = 1
                    elif C[i + j - 1] == A[i - 1] and dp[i-1][j] == 1:
                        dp[i][j] = 1
                except:
                    return 0

        return dp[-1][-1]


print(Solution().isInterleave("sblIWKBF9yT3sAw4", "OxRZnGzMeMJ7ZCwidxBSTDyaNj1D", "OsxblRZnGIWKzBF9yTMyaNj1D") == 0)
print(Solution().isInterleave("", "", "") == 1)
print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == 1)
print(Solution().isInterleave("aabccaa", "dbbcabb", "aadbbcbcacaabb") == 1)
print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") == 0)
