class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        arr = sorted(A)

        return max(arr[-1] * arr[-2] * arr[-3],
                   arr[0] * arr[1] * arr[-1])


#print(Solution().maxp3([0, -1, 3, 100, 70, 50]) == 350000)
print(Solution().maxp3([1, 3, 5, 2, 8, 0, -1, -3]) == 120)
