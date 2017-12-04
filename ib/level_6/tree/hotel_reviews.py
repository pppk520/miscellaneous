class TrieNode:
    def __init__(self, x):
        self.word = None
        self.children = [None] * 26

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        words = A.split('_')
        root = self.build_trie(None, words)

        buckets = [[] for _ in range(len(words) + 1)]

        for i, sent in enumerate(B):
            words = sent.split('_')
            count = 0
            for word in words:
                if self.in_trie(root, word):
                    count += 1

            buckets[count].append(i)


        ret = []
        for bucket in buckets[::-1]:
            for idx in bucket:
                ret.append(idx)

        return ret


    def in_trie(self, root, word):
        for w in word:
            ordinal = ord(w) - ord('a')
            if root.children[ordinal]:
                root = root.children[ordinal]   
            else:
                return False

        if root.word == word:
            return True

        return False

    def build_trie(self, root, words):
        if not root:
            root = TrieNode(None)

        for word in words:
            node = root
            for w in word:
                node = self.add_w(node, w)

            node.word = word

        return root

    def add_w(self, root, w):
        ordinal = ord(w) - ord('a')

        if root.children[ordinal] == None:
            root.children[ordinal] = TrieNode(w)
            return root.children[ordinal]
        else:
            return root.children[ordinal]


print(Solution().solve("cool_ice_wifi", ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"])) # [2,0,1]


