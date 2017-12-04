'''
Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

    A -> 1
    
    B -> 2
    
    C -> 3
    
    ...
    
    Z -> 26
    
    AA -> 27
    
    AB -> 28 
'''

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        base = 1
        val = 0

        for c in A[::-1]:
            val += (ord(c) - ord('A') + 1) * base
            base *= 26

        return val

print(Solution().titleToNumber('') == 0) 
print(Solution().titleToNumber('C') == 3) 
print(Solution().titleToNumber('AB') == 28) 
print(Solution().titleToNumber('ABZZA') == 510381) 
