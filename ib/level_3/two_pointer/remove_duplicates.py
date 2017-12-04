'''
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example: 
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]. 
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0
        j = 0

        if len(A) == 0:
            return 0

        while j < len(A):                
            if j > 0 and A[j] == A[j - 1]:
                j += 1
                continue

            A[i] = A[j]
            i += 1
            j += 1

        return i

arr = [1,1,2,2,3,4,5,6,6,6,6,6,6,7,8]
count = Solution().removeDuplicates(arr)

print(arr[:count])

