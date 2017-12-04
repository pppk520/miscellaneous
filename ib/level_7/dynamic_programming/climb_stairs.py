class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A <= 1:
            return A

        dp = [0] * A

        dp[0] = 1
        dp[1] = 2

        for i in range(2, A):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


print(Solution().climbStairs(3) == 3)
print(Solution().climbStairs(30) == 1346269)
