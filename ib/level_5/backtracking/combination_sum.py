'''
Example, 
Given candidate set 2,3,6,7 and target 7,
A solution set is:

[2, 2, 3]
[7]
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        self.result = []

        self.recur(sorted(set(A)), [], B)
        return self.result

    def recur(self, arr, curr, target):
        if target == 0:
            self.result.append(curr)
            return

        if target < 0:
            return

        for i, v in enumerate(arr):
            self.recur(arr[i:], curr + [v], target - v)    


print(Solution().combinationSum([], 7)) # []
print(Solution().combinationSum([3,6], 7)) # []
print(Solution().combinationSum([2,3,6,7], 7)) # [2,2,3], [7]
