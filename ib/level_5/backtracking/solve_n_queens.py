class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        self.ret = []

        board = [['.' for _ in range(A)] for _ in range(A)]
        self.solve(board, 0, A)

        return self.ret

    def solve(self, board, i, n):
        if i == n:
            ans = [''.join(row) for row in board]
            self.ret.append(ans)
            return

        for j in range(n):
            if self.is_valid(board, n, i, j):
                b = self.copy_board(board)
                b[i][j] = 'Q'
                self.solve(b, i + 1, n)

    def copy_board(self, board):
        b = []

        for row in board:
            b.append(row[:])

        return b

    def is_valid(self, board, n, x, y):
        for i in range(n):
            if board[i][y] == 'Q':
                return False

        for j in range(n):
            if board[x][j] == 'Q':
                return False

        diff = [(-1, -1), (-1, 1), (1, 1), (1, -1)]


        for dx, dy in diff:
            i = x
            j = y
            while i >= 0 and j >= 0 and i < n and j < n:
                if board[i][j] == 'Q':
                    return False

                i += dx
                j += dy

        return True
        



print(len(Solution().solveNQueens(4)) == 2)
print(len(Solution().solveNQueens(8)) == 92)
