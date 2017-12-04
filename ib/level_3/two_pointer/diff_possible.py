class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        i = 0
        j = 1

        while j < len(A):
            if i == j:
                j += 1
                continue

            diff = A[j] - A[i]

            if diff == B:
                return 1
            elif diff > B:
                i += 1
            else:
                j += 1

        return 0


print(Solution().diffPossible([0, 1, 9, 10, 13, 17, 17, 17, 23, 25, 29, 30, 37, 38, 39, 39, 40, 41, 42, 60, 64, 70, 70, 70, 72, 75, 85, 85, 90, 91, 91, 93, 95], 83) == 1)
print(Solution().diffPossible([1, 2, 2, 3, 4], 0) == 1)
print(Solution().diffPossible([1,3,5], 4) == 1)
print(Solution().diffPossible([1,3,4], 4) == 0)
print(Solution().diffPossible([1,2,3], 0) == 0)
