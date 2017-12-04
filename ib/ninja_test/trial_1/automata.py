class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : integer
    # @param E : integer
    # @return an integer
    def automata(self, A, B, C, D, E):
        n = E
        dp = [[0 for _ in range(len(A))] for _ in range(n + 1)]

        accepts = set(C)
        for j in range(len(A)):
            if j in accepts:
                dp[0][j] = 1

        for i in range(1, n + 1):
            for j in range(len(A)):
                dp[i][j] = dp[i - 1][A[j]] + dp[i - 1][B[j]]

        return dp[-1][D]


A = [0, 2, 1]
B = [1, 0, 2]
C = [0]
D = 0

print(Solution().automata(A, B, C, D, 3) == 3)
print(Solution().automata(A, B, C, D, 2) == 2)
print(Solution().automata(A, B, C, D, 1) == 1)
