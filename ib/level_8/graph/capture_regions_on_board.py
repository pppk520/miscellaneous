class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        self.n = len(A)
        self.m = len(A[0])
        self.board = A

        if self.n == 0 or self.m == 0:
            return A

        for i in range(self.n):
            if A[i][0] == 'O':
                self.explore_and_mark(i, 0)

            if A[i][self.m - 1] == 'O':
                self.explore_and_mark(i, self.m - 1)

        for j in range(self.m):
            if A[0][j] == 'O':
                self.explore_and_mark(0, j)

            if A[self.n - 1][j] == 'O':
                self.explore_and_mark(self.n - 1, j)

        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == 'R':
                    self.board[i][j] = 'O'
                elif self.board[i][j] == 'O':
                    self.board[i][j] = 'X'

        return self.board

    def explore_and_mark(self, i, j):
        to_visit = [(i, j)]

        while len(to_visit) > 0:
            i, j = to_visit.pop(0)
            
            for ni, nj in self.adj(i, j):
                if self.board[ni][nj] != 'O':
                    continue

                to_visit.append((ni, nj))

            self.board[i][j] = 'R'

    def adj(self, i, j):
        ll = []

        if i >= 1:
            ll.append((i - 1, j))
        if i < self.n - 1:
            ll.append((i + 1, j))
        if j >= 1:
            ll.append((i, j - 1))
        if j < self.m - 1:
            ll.append((i, j + 1))

        return ll

print(Solution().solve([['X', 'X', 'X', 'X'],
                        ['X', 'O', 'O', 'X'],
                        ['X', 'X', 'O', 'X'],
                        ['X', 'O', 'X', 'X']]))


print(Solution().solve([[]]))

print(Solution().solve([['X', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
                        ['X', 'X', 'O', 'O', 'X', 'O', 'O', 'X'],
                        ['O', 'X', 'X', 'O', 'X', 'O', 'X', 'X']]))

