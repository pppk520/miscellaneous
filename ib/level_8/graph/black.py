class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        if not A:
            return 0

        self.n = len(A)
        self.m = len(A[0])

        self.seen = set()
        count = 0
        for i in range(self.n):
            for j in range(self.m):            
                if A[i][j] == 'X' and not (i, j) in self.seen:
                    self.bfs(A, i, j)
                    count += 1

        return count

    def bfs(self, arr, i, j):
        queue = [(i, j)]

        while len(queue) > 0:
            i, j = queue.pop(0)
            
            for ni, nj in self.adj(i, j):
                if arr[ni][nj] != 'X':
                    continue

                if (ni, nj) not in self.seen:
                    queue.append((ni, nj))

            self.seen.add((i, j))
    
    def adj(self, i, j):
        ret = []

        for di in [-1, 1]:
            adj_i = i + di
            if adj_i >= 0 and adj_i < self.n:
                ret.append((adj_i, j))

        for dj in [-1, 1]:
            adj_j = j + dj
            if adj_j >= 0 and adj_j < self.m:
                ret.append((i, adj_j))

        return ret


if __name__ == '__main__':
    assert(Solution().black([]) == 0)
    assert(Solution().black(['OOOXOOO',
                             'OOXXOXO',
                             'OXOOOXO']) == 3)
    
    assert(Solution().black(['OOXXXOXOOO',
                             'OXOOOXXOXO',
                             'OXOOXOXOXO',
                             'OXOOXXXOXO',
                             'OXOOOOXOXO']) == 4)

    assert(Solution().black(["XXXXXOXOXO", 
                             "OOOOOXOOXX", 
                             "XOOOXXOOXX", 
                             "XXOOXXXOXX", 
                             "XOOOOOXXOO", 
                             "XOXOOOXXXO", 
                             "XOOOXXXXXO", 
                             "XXXXXXXXXX", 
                             "OXOXOOOOXX", 
                             "XOOXOXOOXO"]) == 7)

