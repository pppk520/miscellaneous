'''
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
'''

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)

        sum_n = n * (n + 1) / 2
        sum_n2 = n * (n + 1) * (2*n + 1) / 6

        s1 = sum(A)
        s2 = sum([v**2 for v in A])

        t1 = s1 - sum_n
        t2 = s2 - sum_n2

        a = (t2 / t1 + t1) / 2
        b = (t2 / t1 - t1) / 2

        return (a, b)

print(Solution().repeatedNumber([3,1,2,5,3]))
