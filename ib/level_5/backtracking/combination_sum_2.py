'''
Given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        self.ret = set()
        self.comb_int(A, [], B)

        return sorted(self.ret)

    def comb_int(self, arr, curr, target):
        if target < 0:
            return

        if target == 0:
            self.ret.add(tuple(sorted(curr)))
            return

        if len(arr) == 0:
            return

        self.comb_int(arr[1:], curr + [arr[0]], target - arr[0])
        self.comb_int(arr[1:], curr, target)


if __name__ == '__main__':
    print(Solution().combinationSum([10,1,2,7,6,1,5], 8))
    print(Solution().combinationSum([15, 8, 15, 10, 19, 18, 10, 3, 11, 7, 17], 33))

