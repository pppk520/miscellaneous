'''
Given an array with n objects colored red, white or blue, 
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
'''

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        if len(A) == 0:
            return A

        i = 0
        j = 1

        while i < len(A) and A[i] == 0:
            i += 1

        j = i + 1
        while i < len(A) and j < len(A):
            if A[j] == 0:
                A[i], A[j] = A[j], A[i]
                i += 1

            j += 1

        while i < len(A) and A[i] == 1:
            i += 1

        j = i + 1
        while i < len(A) and j < len(A):
            if A[j] == 1:
                A[i], A[j] = A[j], A[i]
                i += 1

            j += 1

        return A

print(Solution().sortColors([]))
print(Solution().sortColors([1]))
print(Solution().sortColors([0,1,2,2,1,2]))
print(Solution().sortColors([0,1,2,0,1,2]))
