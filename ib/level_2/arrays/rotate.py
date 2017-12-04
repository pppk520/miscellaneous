class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)

        for i in range(n / 2):
            for j in range(i, n - i - 1):
                A[i][j], A[n - j - 1][i] = A[n - j - 1][i], A[i][j]
                A[n - j - 1][i], A[n - i - 1][n - j - 1] = A[n - i - 1][n - j - 1], A[n - j - 1][i]
                A[n - i - 1][n - j - 1], A[j][n - i - 1] = A[j][n - i - 1], A[n - i - 1][n - j - 1]

        return A


arr = [[1,2,3,4],
       [3,4,5,6],
       [6,7,8,9],
       [1,1,1,1]]

for row in Solution().rotate(arr):
    print(row)


