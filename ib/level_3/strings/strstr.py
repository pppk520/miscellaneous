'''
Another question which belongs to the category of questions which are intentionally stated vaguely. 
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

Implement strStr().

 strstr - locate a substring ( needle ) in a string ( haystack ). 
Try not to use standard library string functions for this question.
'''

class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if haystack == None or len(haystack) == 0:
            return -1

        if needle == None or len(needle) == 0:
            return -1

        if len(needle) > len(haystack):
            return -1


        len_needle = len(needle)

        for i in range(len(haystack) - len_needle + 1):
            found = True
            for j in range(len_needle):
                if haystack[i + j] != needle[j]:
                    found = False
                    break

            if found:
                return i

        return -1

print(Solution().strStr("b", "b"))
print(Solution().strStr("djkdjfaijiaaaaaafejhriuehreu", "aaaa"))
print(Solution().strStr("", ""))
print(Solution().strStr("hehrkehrkejrke", "jr"))

