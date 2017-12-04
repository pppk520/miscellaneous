class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):
        centers = zip(E, F)


    def get_covered_indexes(self, i, j, R):
        


    def get_neighbors(self, i, j, bx, by)
        xs = [-1, 0, 1]
        ys = [-1, 0, 1]

        ll = [(x, y) for x in xs for y in ys]
        ll.remove((0, 0))

        ret = []
        for dx, dy in ll:
            x = i + dx
            y = i + dy

            if x >= 0 and x < bx and y >= 0 and y < by:
                ret.append((x, y))
                
        return ret



print(Solution().solve(2, 3, 1, 1, [2], [3]) == 'NO')
