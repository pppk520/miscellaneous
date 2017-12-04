'''
Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative. 
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.
'''

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        v = 1
        pow_v = x

        while n > 0:
            if n & 1 == 1:
                v = v * pow_v % d

            pow_v = (pow_v ** 2) % d
            n >>= 1

        return v % d

if __name__ == '__main__':
    assert(Solution().pow(45, 13, 257) == 56)
    assert(Solution().pow(0, 0, 1) == 0)
   


