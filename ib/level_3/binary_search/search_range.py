# -*- coding: utf-8 -*-
'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]

and target value 8,

return [3, 4].
'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        lo = 0
        hi = len(A) - 1

        r_idx = self.bs(A, lo, hi, B, 'r')
        l_idx = self.bs(A, lo, hi, B, 'l')

        if r_idx == None or l_idx == None:
            return [-1, -1]

        return [l_idx, r_idx]

    def bs(self, arr, lo, hi, target, direction):
        idx = None

        while lo <= hi:
            mid = (lo + hi) / 2

            if arr[mid] == target:
                idx = mid
                if direction == "r":
                    lo = mid + 1
                elif direction == 'l':
                    hi = mid - 1
                else:
                    return idx
            elif arr[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return idx


print(Solution().searchRange([1], 1)) # [0,0]
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8)) # [3,4]
