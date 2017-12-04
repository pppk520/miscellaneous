'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
'''
class Solution:
    def is_happy(self, num):
        slow = fast = num

        while True:
            fast = self.next_num(fast)
            if fast == 1: return True

            fast = self.next_num(fast)
            if fast == 1: return True

            slow = self.next_num(slow)

            # loop occurred
            if slow == fast:
                break
        
        return False

    def next_num(self, n):
        ret = 0

        while (n != 0):
            ret += (n % 10) ** 2
            n /= 10

        return ret

print(Solution().is_happy(19) == True)



