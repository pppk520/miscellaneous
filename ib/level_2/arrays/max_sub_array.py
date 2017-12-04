class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0:
            return 0

        max_sum = -999999999
        curr = 0
        
        for v in A:
            curr += v
            max_sum = max(max_sum, curr)

            if curr < 0:
                curr = 0

        return max_sum



print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6) # [4,-1,2,1]
