class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        if len(A) == 0:
            return 0

        ll = [-999999] * len(A[0])

        for j in range(len(A[0])):
            for i in range(len(A)):
                ll[j] = max(ll[j], A[i][j])

        if len(ll) == 1:
            return ll[0]

        dp = [-9999999] * len(ll)
        dp[0] = ll[0]
        dp[1] = max(ll[0:2])

        for i in range(2, len(ll)):
            dp[i] = max(dp[i - 2] + ll[i], dp[i - 1])

        return dp[-1]


print(Solution().adjacent([[1,2,3,4], [2,3,4,5]]) == 8)
print(Solution().adjacent([[28]]) == 28)
