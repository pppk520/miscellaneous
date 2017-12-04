class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        profit = 0

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                profit += A[i] - A[i - 1]

        return profit


print(Solution().maxProfit([1,2,3]) == 2)
