# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        if not A:
            return True

        return self.is_symmetric(A.left, A.right)   

    def is_symmetric(self, n1, n2):
        if not n1 or not n2:
            return n1 == n2

        return n1.val == n2.val \
               and self.is_symmetric(n1.left, n2.right) \
               and self.is_symmetric(n1.right, n2.left) 
               

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    assert(Solution().isSymmetric(root) == 1)
    root.right.right.right = TreeNode(3)
    assert(Solution().isSymmetric(root) == 0)
    root.left.left.left = TreeNode(3)
    assert(Solution().isSymmetric(root) == 1)

