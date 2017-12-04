class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        arr = sorted(A)

        d = {}
        ret = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                val = arr[i] + arr[j]
                target = B - val

                if target in d:
                    for x, y in d[target]:
                        if i not in (x, y) and j not in (x, y):
                            ret.append(tuple([arr[k] for k in sorted((x, y, i, j))]))

                if not val in d:
                    d[val] = [(i, j)]
                else:
                    d[val].append((i, j))


        return sorted(set(ret))


#print(Solution().fourSum([1,0,-1,0,-2,2], 0))
print(Solution().fourSum([9, -8, -10, -7, 7, -8, 2, -7, 4, 7, 0, -3, -4, -5, -1, -4, 5, 8, 1, 9, -2, 5, 10, -5, -7, -1, -6, 4, 1, -5, 3, 8, -4, -10, -9, -3, 10, 0, 7, 9, -8, 10, -9, 7, 8, 0, 6, -6, -7, 6, -4, 2, 0, 10, 1, -2, 5, -2], 0))

