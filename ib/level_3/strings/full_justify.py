# -*- coding: utf-8 -*-
'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]

L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''

class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        ret = []
    
        count = 0
        last_i = 0
        for i in range(len(A)):
            s = A[i]

            if len(s) + count > B:
                ret.append(self.insert_space_evenly(A[last_i:i], B))
                last_i = i
                count = len(s) + 1
            elif len(s) + count == B:
                ret.append(self.insert_space_evenly(A[last_i:i+1], B))
                last_i = i + 1
                count = 0
            else:
                count += len(s)
                count += 1 # space

        if last_i < len(A):
            last = []
            for i in range(last_i, len(A)):
                last.append(A[i])
                last.append(' ')

            space = B - sum([len(x) for x in last])
            last.append(' ' * space)

            ret.append(''.join(last))

        return ret


    def insert_space_evenly(self, arr, max_len):
        space_len = max_len - sum([len(x) for x in arr])

        space_used = 0
        slot_count = len(arr) - 1

        result = []
        for s in arr[:-1]:
            result.append(s)

            space = (space_len - space_used) / slot_count
            if space * slot_count < (space_len - space_used):
                space += 1

            result.append(' ' * space)
            space_used += space
            slot_count -= 1

        result.append(arr[-1])

        result.append(' ' * (max_len - sum([len(x) for x in result])))

        return ''.join(result)

if __name__ == '__main__':
#    print(Solution().fullJustify(["glu", "muskzjyen", "ahxkp", "t", "djmgzzyh", "jzudvh", "raji", "vmipiz", "sg", "rv", "mekoexzfmq", "fsrihvdnt", "yvnppem", "gidia", "fxjlzekp", "uvdaj", "ua", "pzagn", "bjffryz", "nkdd", "osrownxj", "fvluvpdj", "kkrpr", "khp", "eef", "aogrl", "gqfwfnaen", "qhujt", "vabjsmj", "ji", "f", "opihimudj", "awi", "jyjlyfavbg", "tqxupaaknt", "dvqxay", "ny", "ezxsvmqk", "ncsckq", "nzlce", "cxzdirg", "dnmaxql", "bhrgyuyc", "qtqt", "yka", "wkjriv", "xyfoxfcqzb", "fttsfs", "m"], 144))
#    print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
#    print(Solution().fullJustify(["What", "must", "be", "shall", "be."], 12))
    print(Solution().fullJustify(["am", "fasgoprn", "lvqsrjylg", "rzuslwan", "xlaui", "tnzegzuzn", "kuiwdc", "fofjkkkm", "ssqjig", "tcmejefj", "uixgzm", "lyuxeaxsg", "iqiyip", "msv", "uurcazjc", "earsrvrq", "qlq", "lxrtzkjpg", "jkxymjus", "mvornwza", "zty", "q", "nsecqphjy"], 14))


