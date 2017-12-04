'''
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.
'''

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A == 1:
            return '1'

        s = '11'
        n = A

        while n > 2:
            tmp = []
            count = 1
            for i in range(1, len(s)):
                if s[i] != s[i - 1]:
                    tmp.append('%s%s' %(count, s[i - 1]))
                    count = 1
                else:
                    count += 1

            if count > 0:
                tmp.append('%s%s' %(count, s[-1]))
            
            s = ''.join(tmp)
            n -= 1

        return s

print(Solution().countAndSay(2) == '11')
print(Solution().countAndSay(3) == '21')
print(Solution().countAndSay(4) == '1211')
print(Solution().countAndSay(5) == '111221')
print(Solution().countAndSay(10) == '13211311123113112211')
