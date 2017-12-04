class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        if len(arr) == 0:
            return []

        stack = [arr[0]]

        ret = [-1]
        for v in arr[1:]:
            if v > stack[-1]:
                ret.append(stack[-1])
                stack.append(v)
            else:
                while len(stack) > 0 and v <= stack[-1]:
                    stack.pop()

                if len(stack) == 0:
                    ret.append(-1)
                else:
                    ret.append(stack[-1])

                stack.append(v)

        return ret


if __name__ == '__main__':
    print(Solution().prevSmaller([39, 27, 11, 4, 24, 32, 32, 1]))
    print(Solution().prevSmaller([4, 5, 2, 10]))
    print(Solution().prevSmaller([3, 2, 1]))

