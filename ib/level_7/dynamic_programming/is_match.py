class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        dp = [[0 for _ in range(len(p)+1)] for _ in range(len(s)+1)]

        dp[0][0] = 1

        for i in range(len(s)+1):
            for j  in range(1, len(p)+1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j-1] | dp[i][j-2] 

                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]

                elif p[j - 1] == '.' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[-1][-1]


print(Solution().isMatch('ababbaabbbaaaaabbaaabbababababbababbababbbaabbabbabbaaaabaabbbbaaabaaaaaabbbbbbbab', 'a*.a*b*b..b*b*...bbb*b*..bb*a*..b*b*a*..aa..b*aa*.ba*.a*a*.b.abab*a*bab*b*.b*.a*a*.a.a*.ba*.b*b..ba.a*.baa*.b*b*a*.ab*..bbb*a*bba*a*..aa*.') == 0)
print(Solution().isMatch('baaaaaabaaaabaaaaababababbaab', '..a*aa*a.aba*a*bab*') == 0)
print(Solution().isMatch('aa', 'a') == 0)
print(Solution().isMatch('aa', 'aa') == 1)
print(Solution().isMatch('aaa', 'aa') == 0)
print(Solution().isMatch('aa', 'a*') == 1)
print(Solution().isMatch('aa', '.*') == 1)
print(Solution().isMatch('aab', 'c*a*b') == 1)
