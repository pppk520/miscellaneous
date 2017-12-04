# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        self.d = {}

        self.recur(A, 0, 0)

        ret = []
        for key in sorted(self.d):
            ret.append([x[1] for x in sorted(self.d[key], key=lambda x: x[0])])

        return ret

    def recur(self, root, col, row):
        if not root:
            return

        if not col in self.d:
            self.d[col] = []

        self.d[col].append((row, root.val))

        self.recur(root.left, col - 1, row + 1)
        self.recur(root.right, col + 1, row + 1)


root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.right = TreeNode(9)

print(Solution().verticalOrderTraversal(root))


