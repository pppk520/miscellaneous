# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        return self.recur(A, None, None)        

    def recur(self, root, min_val, max_val):
        if not root:
            return True

        if min_val is not None and root.val <= min_val:
            return False

        if max_val is not None and root.val >= max_val:
            return False

        return self.recur(root.left, min_val, root.val) and \
               self.recur(root.right, root.val, max_val)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(Solution().isValidBST(root) == True)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(Solution().isValidBST(root) == False)
