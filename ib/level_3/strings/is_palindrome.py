class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        chars = []
        for v in A:
            if v.isalpha() or v.isdigit():
                chars.append(v)

        A = ''.join(chars).lower()

        n = len(A)

        if n % 2 == 0:
            l = n / 2 - 1
            r = n / 2
        else:
            l = r = n / 2

        while l >= 0:
            if A[l] != A[r]:
                return 0

            l -= 1
            r += 1

        return 1

print(Solution().isPalindrome('1a2') == 0)
print(Solution().isPalindrome('A man, a plan, a canal: Panama') == 1)
print(Solution().isPalindrome('A man, a plan, a canaa') == 0)
