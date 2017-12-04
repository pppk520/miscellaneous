class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)[::-1]
        n = len(A)    

        for i in range(n):
            if i > 0 and A[i] == A[i - 1]:
                continue

            if A[i] == i:
                return 1

        return -1

print(Solution().solve([0]) == 1)
print(Solution().solve([1]) == -1)
print(Solution().solve([0,0,0]) == 1)
print(Solution().solve([0,1,5,3,2,5]) == -1)

