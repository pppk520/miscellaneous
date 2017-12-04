class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []

        val = 0
        for v in A:
            if not v in ['+', '-', '*', '/']:
                stack.append(int(v))
                continue

            v2 = stack.pop()
            v1 = stack.pop()

            if v == '+':
                stack.append(v1 + v2)
            elif v == '-':
                stack.append(v1 - v2)
            elif v == '*':
                stack.append(v1 * v2)
            else:
                stack.append(v1 / v2)

        if len(stack) == 0:
            return 0

        return stack.pop()




print(Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9)
print(Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6)
