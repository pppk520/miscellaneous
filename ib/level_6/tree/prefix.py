
class TrieNode:
    def __init__(self):
        self.word = False
        self.children_count = 0
        self.children = [None] * 26

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        root = TrieNode()

        for word in A:
            self.add_word(root, word)

        ret = []
        for word in A:
            ret.append(self.get_repr(root, word))

        return ret

    def get_repr(self, root, word):
        repr = []

        for w in word:
            repr.append(w)

            idx = ord(w) - ord('a')
            root = root.children[idx]

            if root.children_count == 1:
                return ''.join(repr)

        return word            

    def add_word(self, root, word):
        for w in word:
            idx = ord(w) - ord('a')

            if not root.children[idx]:
                root.children[idx] = TrieNode()

            root = root.children[idx]            
            root.children_count += 1

        root.word = True


print(Solution().prefix(['zebra', 'dog', 'duck', 'dove'])) # z, dog, du, dov

