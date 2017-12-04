class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def rodCut(self, A, B):
        if not B:
            return []

        cuts = [0] + B + [A]
        self.dp = [[None for _ in range(len(cuts))] for _ in range(len(cuts))]
        min_cost, min_k = self.recur(cuts, 0, len(cuts) - 1)

        ks = self.backtrace(0, len(cuts) - 1, min_k)

        return [cuts[i] for i in ks]

    def backtrace(self, i, j, k):
        if not k:
            return []

        ks = [k]

        if self.dp[i][k]:
            ks.extend(self.backtrace(i, k, self.dp[i][k][1]))

        if self.dp[k][j]:
            ks.extend(self.backtrace(k, j, self.dp[k][j][1]))

        return ks

    def recur(self, cuts, i, j):
        if j - i <= 1:
            return (0, -1)

        if self.dp[i][j]:
            return self.dp[i][j]

        min_cost = 9999999
        min_k = None

        for k in range(i + 1, j):
            cost1, _ = self.recur(cuts, i, k)
            cost2, _ = self.recur(cuts, k, j)

            cost = cost1 + cost2 + (cuts[j] - cuts[i])

            if cost < min_cost:
                min_cost = cost
                min_k = k

        self.dp[i][j] = (min_cost, min_k)

        return self.dp[i][j]

if __name__ == '__main__':
    print(Solution().rodCut(1, [])) # 
    print(Solution().rodCut(6, [1, 2, 5])) # [2, 1, 5]
    print(Solution().rodCut(10, [1, 3, 4, 6, 7])) # [4, 1, 3, 7, 6]
    print(Solution().rodCut(3, [1, 3, 4, 6, 7])) # [1, 3, 4, 6, 7]
    print(Solution().rodCut(100, [1, 4, 6, 7, 19, 21, 25, 33, 43, 45, 56, 76, 88, 92])) # [56 33 19 7 4 1 6 25 21 45 43 76 88 92]

