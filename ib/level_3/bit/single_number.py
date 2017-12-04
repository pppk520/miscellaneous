class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ret = 0

        for v in A:
            ret ^= v

        return ret

print(Solution().singleNumber([1,2,2,3,1]) == 3)
