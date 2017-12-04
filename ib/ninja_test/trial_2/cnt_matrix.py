class Solution:
    # @param A : list of integers
    # @return an integer
    def cntMatrix(self, A):
        total = 1

        for k in range(2, len(A) + 1):
            if len(A) % k != 0:
                continue

            all_sorted = True
            for i in range(0, len(A), k):
                if not self.is_sorted(A[i:i + k]): 
                    all_sorted = False

#            print('k = %s, all_sorted = %s' %(k, all_sorted))
            if not all_sorted: 
                continue

            total += self.get_count(k, len(A))

        return total % (10 ** 9 + 7)

    def get_count(self, k, N):
        import math

        return math.factorial(k) ** (N // k)

    def is_sorted(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False

        return True



print(Solution().cntMatrix([2, 1]) == 1)
print(Solution().cntMatrix([1, 3, 2, 4]) == 5)
print(Solution().cntMatrix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 971570913)
