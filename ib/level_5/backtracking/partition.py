'''
Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]
'''

class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        self.ret = []

        self.partition_internal(A, 0, [])
        return self.ret

    def is_palin(self, s):
        return s == s[::-1]

    def partition_internal(self, s, start, pre):
        if start == len(s):
            self.ret.append(pre)
            return

        if start == len(s) - 1:
            self.ret.append(pre + [s[-1]])
            return

        for i in range(start + 1, len(s) + 1):
            if self.is_palin(s[start:i]):
                self.partition_internal(s, i, pre + [s[start:i]])


print(Solution().partition('aab'))
print(Solution().partition('efe'))
