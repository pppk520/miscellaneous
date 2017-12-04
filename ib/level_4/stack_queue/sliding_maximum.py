'''
A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum for each window. The following example will give you more clarity.

Example :

The array is [1 3 -1 -3 5 3 6 7], and w is 3.

Window position Max
     
[1 3 -1] -3 5 3 6 7 3
1 [3 -1 -3] 5 3 6 7 3
1 3 [-1 -3 5] 3 6 7 5
1 3 -1 [-3 5 3] 6 7 5
1 3 -1 -3 [5 3 6] 7 6
1 3 -1 -3 5 [3 6 7] 7
Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]
'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        if len(A) < B:
            return []

        stack = []

        for i in range(B):
            self.push_stack(stack, A[i])

        result = [stack[0]]

        for i in range(B, len(A)):
            if stack[0] == A[i - B]:
                stack.pop(0)

            self.push_stack(stack, A[i])
            result.append(stack[0])

        return result

    def push_stack(self, stack, val):
        while len(stack) > 0 and stack[-1] < val:
            stack.pop()

        stack.append(val)

print(Solution().slidingMaximum([1,3], 3)) # 
print(Solution().slidingMaximum([1,3,3], 3)) # 3
print(Solution().slidingMaximum([1,3,-1,-3,5,3,6,7], 3)) # 3,3,5,5,6,7

