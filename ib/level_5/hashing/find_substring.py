'''
You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
'''

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        if not A or not B:
            return []

        word_len = len(B[0])
        d = {}
        for w in B:
            if not w in d:
                d[w] = 1
            else:
                d[w] += 1

        idxs = []
        for i in range(len(A) - word_len*len(B) + 1):
            td = d.copy()
            j = i

            while True:
                key = A[j:j + word_len]
                if key in td and td[key] > 0:
                    td[key] -= 1
                    j += word_len

                    if self.all_zero(td):
                        idxs.append(i)
                        break
                else:
                    break

        return idxs

    def all_zero(self, d):
        for key in d:
            if d[key] != 0:
                return False

        return True


print(Solution().findSubstring("cacbbcabbacccacacaacacbbaccaabcbcbbcabbacc", ["b", "a", "b", "a", "c", "a", "b"])) # []
print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])) # [0,9]
print(Solution().findSubstring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aaa", "aaa", "aaa", "aaa", "aaa"])) # [0 ... 98]
