class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        maj = None
        count = 0

        for i in range(len(A)):
            if count == 0:
                maj = A[i]
                count += 1
                continue

            if A[i] == maj:
                count += 1
            else:
                count -= 1

        return maj


print(Solution().majorityElement([2, 1, 2]) == 2)
