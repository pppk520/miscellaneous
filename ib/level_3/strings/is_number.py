class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        start = 0
        while start < len(A):
            if A[start].isdigit() or A[start] in ['-', '.']:
                break

            start += 1

        if start == len(A):
            return False

        sign = 1
        dot = False
        exp = False
        meet_d = False

        if A[start] == '-':
            sign = -1
            start += 1
        elif A[start] == '.':
            dot = True
            start += 1

        if not A[start].isdigit():
            return False

        for i in range(start, len(A)):
            if A[i] == '.':
                if dot or exp or not meet_d:
                    return False

                dot = True
                meet_d = False
            elif A[i] == 'e':
                if exp or not meet_d:
                    return False

                exp = True
                meet_d = False
            elif not A[i].isdigit() and not A[i] in [' ', '-']:
                return False
            else:
                meet_d = True

        if not A.rstrip(' ')[-1].isdigit():
            return False

        return True

if __name__ == '__main__':
    assert(Solution().isNumber("1.e1") == False)
    assert(Solution().isNumber("32467826570812365702673647926314796457921365792637946579269236594265794625762375621765476592146926410592659021465904652.687236478235187653874637824647856428756387264578245676579032657906097542609  ") == True)
    assert(Solution().isNumber(".3") == True)
    assert(Solution().isNumber("+     ") == False)
    assert(Solution().isNumber("+0.1") == True)
    assert(Solution().isNumber("0") == True)
    assert(Solution().isNumber(" 0.1") == True)
    assert(Solution().isNumber("abc") == False)
    assert(Solution().isNumber("1 a") == False)
    assert(Solution().isNumber("2e10") == True)
    assert(Solution().isNumber("1u") == False)
    assert(Solution().isNumber("0.1e10") == True)
    assert(Solution().isNumber("-01.1e-10") == True)
    assert(Solution().isNumber("0xFF") == False)
    assert(Solution().isNumber("3.") == False)
    assert(Solution().isNumber("3e0.1") == False)
    assert(Solution().isNumber("1f") == False)
    assert(Solution().isNumber("1000L") == False)
    assert(Solution().isNumber("1000LL") == False)
    assert(Solution().isNumber("008") == True)
    

