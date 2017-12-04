import heapq

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d = {}
        self.mpath = 0

        for i, v in enumerate(A):
            if v not in d:
                d[v] = []

            d[v].append(i)

        self.max_depth(d, 0)

        return self.mpath
    
    def max_depth(self, d, root_i):
        # it's not a parent node
        if root_i not in d:
            return 0

        depth_list = []

        # iterate children
        for node_i in d[root_i]:
            depth_list.append(self.max_depth(d, node_i))

        maxes = heapq.nlargest(2, depth_list)

        if len(d[root_i]) == 1:
            self.mpath = max(self.mpath, max(maxes) + 1)
        else:
            self.mpath = max(self.mpath, maxes[0] + maxes[1] + 2)
    
        return max(maxes) + 1
print(Solution().solve([-1, 0, 0, 0, 3]) == 3)
print(Solution().solve([-1, 0]) == 1)
print(Solution().solve([-1, 0, 1, 1, 2, 0, 5, 0, 3, 0, 0, 2, 3, 1, 12, 14, 0, 5, 9, 6, 16, 0, 13, 4, 17, 2, 1, 22, 14, 20, 10, 17, 0, 32, 15, 34, 10, 19, 3, 22, 29, 2, 36, 16, 15, 37, 38, 27, 31, 12, 24, 29, 17, 29, 32, 45, 40, 15, 35, 13, 25, 57, 20, 4, 44, 41, 52, 9, 53, 57, 18, 5, 44, 29, 30, 9, 29, 30, 8, 57, 8, 59, 59, 64, 37, 6, 54, 32, 40, 26, 15, 87, 49, 90, 6, 81, 73, 10, 8, ]) == 14)
print(Solution().solve([-1, 0, 0, 2, 1, 2, 4, 4, 2, 5, 5, 1, 1, 2, 4, 13, 7, 0, 2, 9, 2, 16, 18, 0, 13, 13, 22, 10, 8, 3, 26, 14, 24, 0, 26, 0, 8, 15, 6, 22, 20, 30, 1, 2, 10, 0, 39, 3, 8, 40, 9, 12, 42, 37, 39, 47, 52, 24, 29, 48, 15, 18, 50, 46, 43, 55, 26, 1, 6, 28, 59, 51, 56, 4, 53, 30, 5, 54, 18, 29, 3, 65, 30, 16, 9, 22, 14, 30, 32, 62, 0, 6, 44, 18, 37, 14, 80, 93, 2, 95]) == 11)
