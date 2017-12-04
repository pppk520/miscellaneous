class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        if not A:
            return A

        stack = [0]

        ret = [-1] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[stack[-1]]:
                idx = stack.pop()
                ret[idx] = A[i]

                while len(stack) > 0 and A[stack[-1]] < A[i]:
                    idx = stack.pop()
                    ret[idx] = A[i]

            stack.append(i)

        return ret


print(Solution().nextGreater([4, 5, 2, 10])) # [5, 10, 10, -1]
print(Solution().nextGreater([1, 2, 4, 5, 2, 3, 4, 10])) # [2, 4, 5, 10, 3, 4, 10, -1]
