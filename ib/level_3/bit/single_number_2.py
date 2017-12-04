'''
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Example :

Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output : 4
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        value = 0
        for i in range(32):
            zero_count = 0

            mask = 1 << i
            for v in A:
                if v & mask == 0:
                    zero_count += 1

            if zero_count % 3 == 0:
                value |= mask

        return value

print(Solution().singleNumber([1, 2, 4, 3, 3, 2, 2, 3, 1, 1]) == 4)


