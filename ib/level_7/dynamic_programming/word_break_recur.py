class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        self.cache = {}

        return self.is_possible(A, 0, B)

    def is_possible(self, s, start, d):
        possible = False

        if s[start:] in d:
            return True

        if s[start:] in self.cache:
            return self.cache[s[start:]]

        for i in range(start + 1, len(s)):
            if s[start:i] in d:
                possible = possible or self.is_possible(s, i, d)

        self.cache[s[start:]] = possible

        return possible


print(Solution().wordBreak("myinterviewtrainer", ["trainer", "my", "interview"]) == 1)
print(Solution().wordBreak("myinterviewtrainer", ["trainer", "my", "intrview"]) == 0)

