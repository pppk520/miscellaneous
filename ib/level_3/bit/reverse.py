class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        ret = 0

        for _ in range(32):
            ret = (ret << 1) | (A & 1)
            A >>= 1

        return ret


print(Solution().reverse(0) == 0)
print(Solution().reverse(3) == 3221225472)
print(Solution().reverse(4294967295) == 4294967295)
