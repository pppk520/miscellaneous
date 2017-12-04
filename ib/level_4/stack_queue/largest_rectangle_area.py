class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = [0]

        max_area = 0
        i = 0
        for i in range(1, len(A)):
            if len(stack) > 0 and A[i] < A[stack[-1]]:
                pi = None
                while len(stack) > 0:
                    pi = stack.pop()

                    if len(stack) == 0:
                        l = -1
                    else:
                        l = stack[-1]

                    max_area = max(max_area, A[pi] * (i - 1 - l))

                    if len(stack) == 0 or A[stack[-1]] <= A[i]:
                        break

            stack.append(i)

        i += 1
        while len(stack) != 0:
            pi = stack.pop()

            if len(stack) == 0:
                l = -1
            else:
                l = stack[-1]

            max_area = max(max_area, A[pi] * (i - l - 1))


        return max_area

if __name__ == '__main__':
    assert(Solution().largestRectangleArea([47, 69, 67, 97, 86, 34, 98, 16, 65, 95, 66, 69, 18, 1, 99, 56, 35, 9, 48, 72, 49, 47, 1, 72, 87, 52, 13, 23, 95, 55, 21, 92, 36, 88, 48, 39, 84, 16, 15, 65, 7, 58, 2, 21, 54, 2, 71, 92, 96, 100, 28, 31, 24, 10, 94, 5, 81, 80, 43, 35, 67, 33, 39, 81, 69, 12, 66, 87, 86, 11, 49, 94, 38, 44, 72, 44, 18, 97, 23, 11, 30, 72, 51, 61, 56, 41, 30, 71, 12, 44, 81, 43, 43, 27]) == 418)
    assert(Solution().largestRectangleArea([6, 2, 5, 4, 5, 1, 6]) == 12)
    assert(Solution().largestRectangleArea([1]) == 1)
    assert(Solution().largestRectangleArea([2,1,5,6,2,3]) == 10)
