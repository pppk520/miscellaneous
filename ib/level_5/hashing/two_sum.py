class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        d = {}

        for i in range(len(A)):
            if not A[i] in d:
                d[A[i]] = [i]
            else:
                d[A[i]].append(i)
            
        ret = (999999, 999999)
        for i in range(len(A)):
            target = B - A[i]
            if target in d:
                for t in d[target]:
                    if t <= i:
                        continue

                    if t < ret[1]:
                        ret = (i, t)

        if ret == (999999, 999999):
            return []

        return [ret[0] + 1, ret[1] + 1]

print(Solution().twoSum([1], 2))
print(Solution().twoSum([1, 1, 1], 2))
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8], -3))
