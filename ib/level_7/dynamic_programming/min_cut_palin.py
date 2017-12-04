class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        self.cache = {}

        ret = self.recur(A)

        return ret

    def recur(self, s):
        if len(s) == 1:
            return 0

        if self.is_palin(s):
            return 0

        min_cut = 999999999
        for i in range(1, len(s)):
            if self.is_palin(s[:i]):
                if s[i:] not in self.cache:
                    self.cache[s[i:]] = self.recur(s[i:])

                right = self.cache[s[i:]]
                min_cut = min(min_cut, right + 1)

        self.cache[s] = min_cut

        return self.cache[s]

    def is_palin(self, s):
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

if __name__ == '__main__':
    assert(Solution().minCut("ZPPgWPOaDlSJeou8bws8gaEKtYcX1K0KGWBqwoDUEgcZpxIDtK4RVMStD6ZPEv2h2tx03oodBf49L4beFbj6SNBWTXht9eYCDTo") == 92)

    assert(Solution().minCut("aabbaa") == 0)
    assert(Solution().minCut("ab") == 1)
    assert(Solution().minCut("a") == 0)
    assert(Solution().minCut("aab") == 1)
    assert(Solution().minCut("aabbaabb") == 1)
    assert(Solution().minCut("abcde") == 4)

