'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
For example:
Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

class Solution:
    # @param A : tuple of integers
    # @return a tuple
    def singleNumber(self, A):
        tmp = 0

        for v in A:
            tmp ^= v

        # get the first diff bit
        idx = 0
        while tmp > 0:
            if tmp >> idx & 1 != 0:
                break

            idx += 1

        v1 = 0
        v2 = 0
        val = 1 << idx

        for v in A:
            if v & val != 0:
                v1 ^= v
            else:
                v2 ^= v

        return v1, v2

print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))


