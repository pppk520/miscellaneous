class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        if len(A) == 0:
            return []

        letter_map = {'0': '0',
                      '1': '1',
                      '2': 'abc',
                      '3': 'def',
                      '4': 'ghi',
                      '5': 'jkl',
                      '6': 'mno',
                      '7': 'pqrs',
                      '8': 'tuv',
                      '9': 'wxyz'}

        return self.recur(A[1:], letter_map, list(letter_map[A[0]]))

    def recur(self, remain, letter_map, curr):
        if len(remain) == 0:
            return curr

        result = []
        for s in curr:
            for nc in letter_map[remain[0]]:
                result.append(s + nc)

        return self.recur(remain[1:], letter_map, result)

# ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(Solution().letterCombinations("23"))
print(Solution().letterCombinations("123"))
print(Solution().letterCombinations("01579"))
