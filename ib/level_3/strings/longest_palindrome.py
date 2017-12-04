'''
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
'''

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        longest_length = 0
        longest_palin = ''

        palin = None
        for i in range(len(A)):
            palin = self.get_longest_palin(A, i, False)
            if len(palin) > longest_length:
                longest_length = len(palin)
                longest_palin = palin

            palin = self.get_longest_palin(A, i, True)
            if len(palin) > longest_length:
                longest_length = len(palin)
                longest_palin = palin

        return longest_palin

    def get_longest_palin(self, s, idx, is_middle):
        r = idx + 1
        l = idx - 1

        if is_middle:
            r = idx + 1
            l = idx     
        
        while True:
            if r == len(s) or l < 0:
                return s[l + 1 : r]

            if s[r] == s[l]:
                r += 1
                l -= 1
            else:
                return s[l + 1 : r]

        return ''        

if __name__ == '__main__':
    assert(Solution().longestPalindrome('abb') == 'bb')
    assert(Solution().longestPalindrome('a') == 'a')
    assert(Solution().longestPalindrome('ab') == 'a')
    assert(Solution().longestPalindrome('aba') == 'aba')
    assert(Solution().longestPalindrome('abba') == 'abba')
    assert(Solution().longestPalindrome('adfdabcdefggfedcba933eijdkaj') == 'abcdefggfedcba')
