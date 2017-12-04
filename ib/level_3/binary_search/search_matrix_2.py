class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if len(A) == 0:
            return False

        row = 0
        col = len(A[0]) - 1

        while row < len(A) and col >= 0:
            if A[row][col] > B:
                col -= 1
            elif A[row][col] < B:
                row += 1
            else:
                return True

        return False

arr = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(Solution().searchMatrix(arr, 5) == True)
print(Solution().searchMatrix(arr, 20) == False)
