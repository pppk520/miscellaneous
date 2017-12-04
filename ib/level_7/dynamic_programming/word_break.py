class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        dp = [0] * (len(A) + 1)        
        dp[-1] = 1

        len_s = set(map(len, B))

        for start in range(len(A)-1, -1, -1):
            for len_w in len_s:
                end = start + len_w

                if end > len(A):
                    continue

                if dp[end] == 1 and A[start : end] in B:
                    dp[start] = 1

        return dp[0]


print(Solution().wordBreak("myinterviewtrainer", ["trainer", "my", "interview"]) == 1)
print(Solution().wordBreak("myinterviewtrainer", ["trainer", "my", "intrview"]) == 0)

