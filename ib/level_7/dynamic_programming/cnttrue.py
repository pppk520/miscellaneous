class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        self.true = {}
        self.false = {}    

        ret = self.tr(A, 0, len(A) - 1)

        return self.true[(0, len(A) - 1)]

    def tr(self, exp, i, j):
        if i == j:
            return exp[i] == 'T'

        if (i, j) in self.true:
            return self.true[(i, j)]

        ans = 0
        for k in range(i, j):
            if exp[k] == '&':
                ans += (self.tr(exp, i, k - 1) * self.tr(exp, k + 1, j))
            elif exp[k] == '|':
                ans += (self.tr(exp, i, k - 1) * self.tr(exp, k + 1, j)) + \
                       (self.tr(exp, i, k - 1) * self.fa(exp, k + 1, j)) + \
                       (self.fa(exp, i, k - 1) * self.tr(exp, k + 1, j))
            elif exp[k] == '^': 
                ans += (self.tr(exp, i, k - 1) * self.fa(exp, k + 1, j)) + \
                       (self.fa(exp, i, k - 1) * self.tr(exp, k + 1, j))

            ans %= 1003

        self.true[(i, j)] = ans

        return ans

    def fa(self, exp, i, j):
        if i == j:
            return exp[i] == 'F'

        if (i, j) in self.false:
            return self.false[(i, j)]

        ans = 0
        for k in range(i, j):
            if exp[k] == '&':
                ans += (self.tr(exp, i, k - 1) * self.fa(exp, k + 1, j)) + \
                       (self.fa(exp, i, k - 1) * self.tr(exp, k + 1, j)) + \
                       (self.fa(exp, i, k - 1) * self.fa(exp, k + 1, j))
            elif exp[k] == '|':
                ans += (self.fa(exp, i, k - 1) * self.fa(exp, k + 1, j))
            elif exp[k] == '^':
                ans += (self.tr(exp, i, k - 1) * self.tr(exp, k + 1, j)) + \
                       (self.fa(exp, i, k - 1) * self.fa(exp, k + 1, j))

            ans %= 1003

        self.false[(i, j)] = ans

        return ans



print(Solution().cnttrue('T|F') == 1)
print(Solution().cnttrue('T|F|T^F|T|F|T|T') == 401)
