'''
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()

        for i in range(0, len(A), 2):
            if i == len(A) - 1:
                break

            # swap
            A[i], A[i + 1] = A[i + 1], A[i]

        return A

print(Solution().wave([1,2,3,4]))
print(Solution().wave([5,1,3,2,4]))
