class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        if A <= 1:
            return 1

        dp = [0] * (A + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, A + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[-1] % (10**9 + 7)

print(Solution().chordCnt(1) == 1)
print(Solution().chordCnt(2) == 2)
print(Solution().chordCnt(3) == 5)
print(Solution().chordCnt(5) == 42)
print(Solution().chordCnt(8) == 1430)
print(Solution().chordCnt(19) == 767263183)
