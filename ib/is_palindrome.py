class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        if A < 0:
            return False

        return str(A) == str(A)[::-1]


print(Solution().isPalindrome(12121) == True)
print(Solution().isPalindrome(123) == False)
