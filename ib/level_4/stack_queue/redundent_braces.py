class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []

        for c in A:
            if c == ')':
                p = stack.pop()
                op_count = 0
                while p != '(':
                    if p in ['+', '-', '*', '/']:
                        op_count += 1

                    p = stack.pop()

                if op_count == 0:
                    return 1                    
            else:
                stack.append(c) 

        return 0



print(Solution().braces('((a + b))') == 1)
print(Solution().braces('(a + (a + b))') == 0)
print(Solution().braces('(a * b)') == 0)
print(Solution().braces('(a)') == 1)
