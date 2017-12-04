class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        mice_pos = sorted(A)
        pos = sorted(B)

        val = 0
        for i in range(len(pos)):
            val = max(val, abs(mice_pos[i] - pos[i]))

        return val


print(Solution().mice([4,-4,2], [4,0,5]) == 4)
