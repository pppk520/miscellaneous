class Solution:
    # @param A : list of integers
    # @return an integer
    def cntInc(self, A):
        N = len(A)

        count = 0
        i = 0
        j = 1
        while j < N:
            if A[j] <= A[j - 1]:
                count += ((j - i) * (j - i - 1)) // 2
                i = j

            j += 1

        count += ((j - i) * (j - i - 1)) // 2
        count += N
    
        return count % (10**9 + 7)

print(Solution().cntInc([4, 5, 1, 2]) == 6)
print(Solution().cntInc([1,1,1,1,1]) == 5)
print(Solution().cntInc([1,2,3,4]) == 10)
