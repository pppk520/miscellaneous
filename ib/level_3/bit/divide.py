'''
Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Example:

5 / 2 = 2
Also, consider if there can be overflow cases. For overflow case, return INT_MAX.
'''

class Solution:
    # @param dividend : integer
    # @param divisor : integer
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 2147483647

        if divisor == 1:
            return dividend

        sign = 1
        if (dividend > 0 and divisor < 0) or \
           (dividend < 0 and divisor > 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        val = 0
        while True:
            count = 0
            while dividend - (divisor << count) > 0:
                count += 1

            if count == 0:
                break

            val |= 1 << (count - 1)
            dividend -= divisor << (count - 1)

        if sign < 0:
            return -val

        return val



print(Solution().divide(-5700836, -7169730) == 0)
print(Solution().divide(5, -2) == -2)
print(Solution().divide(5, 1) == 5)
print(Solution().divide(2147483647, 1) == 2147483647)
print(Solution().divide(5, 2) == 2)
print(Solution().divide(0, 2) == 0)
print(Solution().divide(5, 0) == 2147483647)
print(Solution().divide(1, 10) == 0)
print(Solution().divide(99992782329831, 278390) == (99992782329831/278390))
