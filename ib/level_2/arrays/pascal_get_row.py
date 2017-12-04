# -*- coding: utf-8 -*-
'''
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
'''

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A == 0:
            return [1]

        if A == 1:
            return [1, 1]

        ret = [1, 1]
        for i in range(A - 1):
            l = [1]

            for j in range(1, len(ret)):
                l.append(ret[j] + ret[j - 1])

            l.append(1)

            ret = l

        return ret


print(Solution().getRow(0))
print(Solution().getRow(1))
print(Solution().getRow(2))
print(Solution().getRow(3))
print(Solution().getRow(5))
