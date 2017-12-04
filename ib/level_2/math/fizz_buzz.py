class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        ret = []

        for i in range(1, A + 1):
            if i % 15 == 0:
                ret.append('FizzBuzz')
            elif i % 5 == 0:
                ret.append('Buzz')
            elif i % 3 == 0:
                ret.append('Fizz')
            else:
                ret.append(str(i))

        return ret

print(Solution().fizzBuzz(5))
