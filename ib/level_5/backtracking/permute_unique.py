class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        self.ret = set()
        self.permute_internal(A, [])

        return self.ret

    def permute_internal(self, nums, curr):
        if len(nums) <= 1:
            self.ret.add(tuple(curr + nums))
            return

        for i in range(len(nums)):            
            remain = nums[:]
            remain.remove(nums[i])
            self.permute_internal(remain, curr[:] + [nums[i]])



print(Solution().permute([1,1,2]))
print(Solution().permute([1,2,3]))
