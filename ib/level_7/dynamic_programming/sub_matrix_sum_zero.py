class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if not A or len(A) == 0:
            return 0

        n = len(A)
        m = len(A[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        dp[0][0] = A[0][0]

        count = 0

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + A[i][0]

        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + A[0][j]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + A[i][j]

        for r1 in range(n):
            for r2 in range(r1, n):
                d = {}

                for j in range(m):
                    if r1 == 0:
                        val = dp[r2][j]
                    else:
                        val = dp[r2][j] - dp[r1 - 1][j]

                    if not val in d:
                        d[val] = 0

                    d[val] += 1

                for val in d:
                    if val == 0:
                        count += d[val]

                    if d[val] > 1:
                        count += (d[val] * (d[val] - 1)) / 2

        return count

print(Solution().solve([[0, 0],
                        [0, 0]]) == 9)

print(Solution().solve([[0, 0, 0],
                        [0, 0, 0]]) == 18)

print(Solution().solve([[-8, 5, 7],
                        [ 3, 7,-8],
                        [ 5,-8, 9]]) == 2)

print(Solution().solve([[0]]) == 1)
print(Solution().solve([[0],[0]]) == 3)

