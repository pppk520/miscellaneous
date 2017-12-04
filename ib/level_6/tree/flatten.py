# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def print_right_trace(root):
    if root == None:
        return

    print('right_trace -> %s, left = %s' %(root.val, root.left))
    print_right_trace(root.right)

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        self.flat(A)
        return A

    def flat(self, root):
        if not root:
            return

        if not root.left and not root.right:
            return root

        rlast = self.flat(root.right)    
        llast = self.flat(root.left)

        tmp = root.right

        if root.left:
            root.right = root.left
            root.left = None

        if llast:
            llast.right = tmp

        if rlast:
            return rlast
        else:
            return llast

if __name__ == '__main__':
    root = TreeNode(47)
    root.left = TreeNode(42)
    root.right = TreeNode(52)
    root.left.left = TreeNode(41)
    root.left.right = TreeNode(44)
    root.right.left = TreeNode(50)
    root.right.right = TreeNode(64)
    root.left.left.left = TreeNode(40)
    root.left.right.left = TreeNode(43)
    root.left.right.right = TreeNode(45)
    
    print_right_trace(Solution().flatten(root))

