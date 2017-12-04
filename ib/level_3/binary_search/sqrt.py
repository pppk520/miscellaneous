'''
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3
'''

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0:
            return 0

        elif A == 1:
            return 1

        lo = 0
        hi = A

        while lo <= hi:
            mid = (lo + hi) >> 1
            val = mid ** 2

            if val > A:
                hi = mid - 1
            elif val < A:
                lo = mid + 1
            else:
                return mid

        return min(lo, hi)


print(Solution().sqrt(4) == 2)
print(Solution().sqrt(930675566) == 30506)
print(Solution().sqrt(11) == 3)
print(Solution().sqrt(0) == 0)
print(Solution().sqrt(1) == 1)
print(Solution().sqrt(100) == 10)
