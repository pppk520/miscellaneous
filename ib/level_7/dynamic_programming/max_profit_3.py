class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        mab_1 = -99999999 # max_after_buy_1
        mab_2 = -99999999 # max_after_buy_2
        mas_1 = 0         # max_after_sell_1
        mas_2 = 0         # max_after_sell_2

        for v in A:
            mas_2 = max(mas_2, mab_2 + v)
            mab_2 = max(mab_2, mas_1 - v)
            mas_1 = max(mas_1, mab_1 + v)
            mab_1 = max(mab_1, -v)

        return mas_2

print(Solution().maxProfit([1,2,1,2]) == 2)
