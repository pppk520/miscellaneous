'''
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
'''

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        self.ret = []
        self.permute_internal(A, [])

        return self.ret

    def permute_internal(self, nums, curr):
        if len(nums) <= 1:
            self.ret.append(curr + nums)
            return

        for i in range(len(nums)):            
            remain = nums[:]
            remain.remove(nums[i])
            self.permute_internal(remain, curr[:] + [nums[i]])



print(Solution().permute([1,1,2]))
print(Solution().permute([1,2,3]))
