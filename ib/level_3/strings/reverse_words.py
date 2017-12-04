'''
Given an input string, reverse the string word by word.

Example:

Given s = "the sky is blue",

return "blue is sky the".

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
'''

class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        words = A.strip().split()

        return ' '.join(words[::-1])


if __name__ == '__main__':
    print(Solution().reverseWords("the sky  is blue"))
    assert(Solution().reverseWords("the sky is blue") == "blue is sky the")


