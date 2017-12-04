'''
You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

Example:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2
'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)

        if n == 0:
            return 0

        while n > 0:
            if self.is_palin(A[:n]):
                return len(A) - n

            n -= 1

        return len(A) - 1

    def is_palin(self, s):
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True


print(Solution().solve('') == 0)
print(Solution().solve('A') == 0)
print(Solution().solve('ABC') == 2)
print(Solution().solve('ABA') == 0)
print(Solution().solve('AACECAAAA') == 2)
print(Solution().solve('AACECABAABAABABABAABABABAAAAA') == 27)
