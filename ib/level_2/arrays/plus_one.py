'''
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if len(A) == 0:
            return []

        idx = 0
        # ignore leading 0s
        for i, v in enumerate(A):
            if v != 0:
                break

            idx += 1
        
        arr = A[idx:][::-1][:]

        c = 1
        for i, v in enumerate(arr):            
            new_v = (v + c) % 10
            c = (v + c) / 10
            arr[i] = new_v

        if c == 1:
            arr.append(c)

        return arr[::-1]

print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([0,0,1,2,3]))
print(Solution().plusOne([1,0,0,1,2,3]))




