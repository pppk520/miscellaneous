'''
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        d = A - 1
        r = B - 1

        return self.ncr(d + r, d)

    def ncr(self, n, r):
        import math
        return (math.factorial(n) / math.factorial(n - r)) / math.factorial(r)

print(Solution().uniquePaths(2, 2) == 2)
print(Solution().uniquePaths(8, 3) == 36)

