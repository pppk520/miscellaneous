'''
Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9
'''
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        ret = []
        sign = 1
        start_idx = 0

        A = A.strip()
        if A[0] == '-':
            sign = -1
            start_idx = 1
        elif A[0] == '+':
            start_idx = 1

        for i in range(start_idx, len(A)):
            c = A[i]

            if c.isdigit():
                ret.append(c)
            else:
                break

        if len(ret) == 0:
            return 0

        ret = int(''.join(ret)) * sign

        if ret > 2147483647:
            return 2147483647
        elif ret < -2147483648:
            return -2147483648

        return ret


if __name__ == '__main__':
    assert(Solution().atoi('+ 3611156') == 0)
    assert(Solution().atoi('-54332872018247709407 4 54') == -2147483648)
    assert(Solution().atoi(' +7') == 7)
    assert(Solution().atoi('9 2704   01885D 9M   65291S844404U7463') == 9)
    assert(Solution().atoi(' V515V 5793K 627 23815945269 1 1249794L 631 8755 7') == 0)
    assert(Solution().atoi('5121478262 8070067M75 X199R 547 8C0A11 93I630 4P4071 029W433619 M3  5 14703818 776366059B9O43393') == 2147483647)
    assert(Solution().atoi('- 5 88C340185Q  71  8079 834617385 2898422X5297Z6900') == 0)    
    assert(Solution().atoi(' 7 U 0 T7165  0128862 089 39 5') == 7)
    assert(Solution().atoi('788') == 788)
    assert(Solution().atoi('   788') == 788)
    assert(Solution().atoi('   788*&&(*&') == 788)
    assert(Solution().atoi('   -788') == -788)
    assert(Solution().atoi('99999999999999999999999999999999999999999999999999999999') == 2147483647)
    

