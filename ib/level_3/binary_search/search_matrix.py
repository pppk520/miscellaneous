class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if len(A) == 0:
            return 0

        lo = 0
        hi = len(A) * len(A[0]) - 1
        
        row_size = len(A[0])

        while lo <= hi:
            mid = (lo + hi) >> 1

            row = mid / row_size
            col = mid % row_size

            if A[row][col] == B:
                return 1
            elif A[row][col] > B:
                hi = mid - 1
            else:
                lo = mid + 1

        return 0


arr = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print(Solution().searchMatrix(arr, 3) == 1)
print(Solution().searchMatrix(arr, 100) == 0)
