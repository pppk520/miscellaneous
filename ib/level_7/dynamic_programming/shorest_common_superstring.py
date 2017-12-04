class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n = len(A)
        strs = A

        dp = [[-1 for _ in range(2 ** n)] for _ in range(n)]
        str_map = {}
        for i in range(2 ** n):
            str_map[i] = None

        for i in range(n):
            dp[i][1<<i] = len(strs[i])
            str_map[1<<i] = strs[i]


    def fill_dp(self, dp, strs, i, mask):
        for x in range(len(strs)):
            for m in dp[x]:
                if (m & 1 << i):
                    if dp[x][m] < 0:
                        self.fill_dp(dp, strs, x, m)

                    dp[i][mask] = min(dp[i][mask], dp[x][m])

    def get_max_overlap(self, s1, s2):
        overlap_len = 0
        max_s = None

        if s2 in s1:
            return len(s2), s1
        elif s1 in s2:
            return len(s1), s2

#        print('s1 = %s, s2 = %s' %(s1, s2))
        # s1 suffix matches s2 prefix
        for i in range(1, min(len(s1), len(s2))):
            if s1[-i:] == s2[:i]:
                if i > overlap_len:
                    overlap_len = i
                    max_s = s1[:-i] + s2

        # s2 suffix matches s1 prefix
        for i in range(1, min(len(s1), len(s2))):
            if s2[-i:] == s1[:i]:
                if i > overlap_len:
                    overlap_len = i
                    max_s = s2[:-i] + s1

        if not max_s:
            return overlap_len, s1 + s2
            
        return overlap_len, max_s



print(Solution().solve(["abcd"]) == 4)
print(Solution().solve(["abcd", "cdef", "fgh", "de"]) == 8)
print(Solution().solve(["abcd", "def", "deded", "de"]) == 10) # abcdededef
