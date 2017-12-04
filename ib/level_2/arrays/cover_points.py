class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        if len(X) == 0:
            return 0

        start = X[0], Y[0]
        steps = 0
        for i in range(1, len(X)):
            diff_x = X[i] - start[0]
            diff_y = Y[i] - start[1]

            steps += min(abs(diff_x), abs(diff_y))
            steps += abs(abs(diff_x) - abs(diff_y))

            start = X[i], Y[i]

        return steps


print(Solution().coverPoints([0, 1, 1], [0, 1, 2]))
