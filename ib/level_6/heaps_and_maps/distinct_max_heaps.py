class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A <= 2:
            return 1

        k = 1
        v = 1
        while v < A:
            k += 1
            v *= 2
        
        m = A - v/2 + 1
        tmp = v / 4
        l_count = tmp - 1 + min(tmp, m)
        r_count = tmp - 1 + max(0, m - tmp)
        
        return self.ncr(A - 1, l_count) * self.solve(l_count) * self.solve(r_count)

    def ncr(self, n, r):
        import operator as op

        r = min(r, n-r)
        if r == 0: return 1
        numer = reduce(op.mul, xrange(n, n-r, -1))
        denom = reduce(op.mul, xrange(1, r+1))
        return numer//denom


print(Solution().solve(4) == 3)
print(Solution().solve(5) == 8)
print(Solution().solve(9) == 896)
