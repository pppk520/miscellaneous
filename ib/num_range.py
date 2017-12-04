class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        count = 0

        sum_arr = [0] * len(A)
        sum_arr[0] = A[0]
        for i in range(1, len(A)):
            sum_arr[i] = sum_arr[i - 1] + A[i]

        x = 0
        y = 0
        for i in range(len(A)):
            while x != len(A) and (sum_arr[x] - sum_arr[i] + A[i]) < B:
                x += 1

            while y != len(A) and (sum_arr[y] - sum_arr[i] + A[i]) <= C:
                y += 1
        
            count += (y - x)
       
        return count


print(Solution().numRange([80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90], 99, 269) == 58)
'''
print(Solution().numRange([10, 5, 1, 0, 2], 6, 8) == 3)
print(Solution().numRange([10, 5, 1, 0, 2, 8], 6, 8) == 4)
'''
