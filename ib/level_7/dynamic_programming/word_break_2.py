class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):
        self.dp = {}
        ret = self.recur(A, B)

        return sorted(ret)

    def recur(self, s, d):
        if len(s) == 0:
            return

        if s in self.dp:
            return self.dp[s]

        ret = []

        if s in d:
            ret.append(s)

        for i in range(1, len(s)):
            if s[:i] in d:
                subs = self.recur(s[i:], d)
                for sub in subs:
                    ret.append(s[:i] + ' ' + sub)

        self.dp[s] = ret

        return ret




# [ "cat sand dog", "cats and dog" ]
print(Solution().wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]))

print(Solution().wordBreak('aabbbabaaabbbabaabaab', ["bababbbb", "bbbabaa", "abbb", "a", "aabbaab", "b", "babaabbbb", "aa", "bb"]))
