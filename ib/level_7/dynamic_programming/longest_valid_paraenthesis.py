class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        dp = [0] * len(A)

        stack = []

        for i, c in enumerate(A):
            if c == '(':
                stack.append(('(', i))
            else: # )
                if len(stack) == 0:
                    continue

                val, idx = stack.pop()
                if val == '(':
                    dp[i] = 1
                    dp[idx] = 1
                else:
                    # invalid, clean up
                    stack = []

        max_len = 0        
        i = 0
        j = 0

        while i < len(dp) and j < len(dp):
            if dp[j] == 1:
                j += 1
            else:
                max_len = max(max_len, j - i)
                j += 1
                i = j

        max_len = max(max_len, len(dp) - i)

        return max_len


print(Solution().longestValidParentheses('') == 0)
print(Solution().longestValidParentheses('(()') == 2)
print(Solution().longestValidParentheses(')()())') == 4)
print(Solution().longestValidParentheses('((()))') == 6)
print(Solution().longestValidParentheses('((()(()()()((((()') == 6)
print(Solution().longestValidParentheses('((()(()()()((((()()()()(()))))))()()()()()()))))))))()()()()()(((((((((((((()))))))))))))))))))()()()()()())') == 46)
