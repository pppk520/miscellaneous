# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        self.balanced = True

        self.get_depth(A)

        return self.balanced

    def get_depth(self, root):
        if root == None:
            return 0

        left = self.get_depth(root.left)
        right = self.get_depth(root.right)

        if abs(left - right) > 1:
            self.balanced = False

        return max(left, right) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(Solution().isBalanced(root) == True)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)

print(Solution().isBalanced(root) == False)




