class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        N = A * 2 - 1
        arr = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(A, 0, -1):
            self.fill(arr, i)

        return arr

    def fill(self, arr, v):
        N = len(arr)
        diff = (N / 2 + 1) - v

        for j in range(diff, N - diff):
            arr[diff][j] = v
            arr[N - diff - 1][j] = v        

        for i in range(diff, N - diff):
            arr[i][diff] = v
            arr[i][N - diff - 1] = v


ret = Solution().prettyPrint(10)
for row in ret:
    print(row)
