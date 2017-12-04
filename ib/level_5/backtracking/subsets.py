class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        arr = sorted(A)
        self.ret = []
        
        self.recur(arr, 0, [])

        return sorted(self.ret)

    def recur(self, arr, idx, curr):
        if len(arr) == 0 or idx == len(arr):
            self.ret.append(curr)
            return

        self.recur(arr, idx + 1, curr + [arr[idx]])
        self.recur(arr, idx + 1, curr)



print(Solution().subsets([1,2,3]))
print(Solution().subsets([15, 20, 12, 19, 4]))
