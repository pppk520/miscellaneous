# -*- coding: utf-8 -*-
'''
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        ll = [[1], [1,1]]

        if A == 0:
            return []

        if A == 1:
            return [[1]]

        if A == 2:
            return ll

        for i in range(A - 2):
            l = [1]

            for j in range(1, len(ll[-1])):
                l.append(ll[-1][j] + ll[-1][j - 1])

            l.append(1)

            ll.append(l)

        return ll

print(Solution().generate(1))
print(Solution().generate(2))
