class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        if len(A) == 0:
            return 0

        n = len(A)
        m = len(A[0])

        histo_dp = [[0 for _ in range(m)] for _ in range(n)]

        for j in range(m):
            histo_dp[0][j] = A[0][j]

        for i in range(1, n):
            for j in range(m):
                if A[i][j] == 1:
                    histo_dp[i][j] = histo_dp[i-1][j] + 1

        max_area = 0
        for i in range(n):
            max_histo = self.get_max_histo(histo_dp[i])
            max_area = max(max_area, max_histo)

        return max_area

    def get_max_histo(self, row):
        stack = [0]

        max_area = 0
        n = len(row)
        i = 1

        while i < n:
            if len(stack) == 0 or row[i] > row[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()

                if len(stack) > 0:
                    area = row[tp] * (i - stack[-1] - 1)
                else:
                    area = row[tp] * i

                max_area = max(max_area, area)

        while len(stack) > 0:
            tp = stack.pop()

            if len(stack) > 0:
                area = row[tp] * (n - stack[-1] - 1)
            else:
                area = row[tp] * n

            max_area = max(max_area, area)

        return max_area

print(Solution().maximalRectangle([[1,1,1],
                                   [0,1,1],
                                   [1,0,0]]) == 4)

print(Solution().maximalRectangle([[1,1,1,1],
                                   [0,1,1,1],
                                   [1,0,1,0]]) == 6)
