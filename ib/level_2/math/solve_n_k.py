class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        import math

        if len(A) < B:
            return 0

        c_arr = list(str(C))
        digit_num = len(A)

        if B > len(c_arr):
            return 0

        count = 0
        for v in c_arr:
            idx = self.get_lt_idx(A, v)
            count += idx * math.factorial((len(A) - idx))

        print(count)
        return count

    def get_lt_idx(self, arr, digit):
        for i in range(len(arr)):
            if arr[i] >= digit:
                return i - 1
        
        return len(arr) - 1



print(Solution().solve([2, 3, 5, 6, 7, 9], 5, 42950) == 2592)
'''
print(Solution().solve([2,9], 5, 17015) == 0)
print(Solution().solve([], 5, 111) == 0)
print(Solution().solve([0,1,2,5], 1, 123) == 4)
print(Solution().solve([0,1,2,5], 2, 21) == 5)
print(Solution().solve([0,1,2,5], 1, 4) == 3)
'''
