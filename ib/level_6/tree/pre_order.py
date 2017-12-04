# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        self.ll = []

        self.preorder(A)

        return self.ll

    def preorder(self, root):   
        if root == None:
            return
     
        self.ll.append(root.val)   
        self.preorder(root.left)
        self.preorder(root.right)

if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(4)
    print(Solution().preorderTraversal(root))  # 01324
