'''
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)

'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) == 0:
            return -1

        l_min = [A[0]]
        for i in range(1, len(A)):
            l_min.append(min(l_min[-1], A[i]))

        r_max = [A[-1]]
        for i in range(len(A) - 2, -1, -1):
            r_max.append(max(r_max[-1], A[i]))
        r_max = r_max[::-1]

        i = 0
        j = 0
        max_dist = -1
        while i < len(A) and j < len(A):
            if l_min[i] <= r_max[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1

        return max_dist

print(Solution().maximumGap([]) == -1)
print(Solution().maximumGap([3,5,4,2]) == 2)
print(Solution().maximumGap([3,5,4,2,1,2,3,5,7,1,2,4,4,67,3,1,1]) == 14)
