'''
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3 
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        while B != 0:
            A, B = B, A % B

        return A


if __name__ == '__main__':
    from fractions import gcd

    assert(Solution().gcd(525, 25) == gcd(525, 25))
    assert(Solution().gcd(13, -39) == gcd(13, -39))
   

