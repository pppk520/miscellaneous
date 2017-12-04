# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder : list of integers denoting inorder traversal
    # @param postorder : list of integers denoting postorder traversal
    # @return the root node in the tree
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None

        root_v = postorder[-1]
        root = TreeNode(root_v)

        idx = inorder.index(root_v)
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])

        return root


def print_tree(root):
    if root == None:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

root = Solution().buildTree([2,1,3], [2,3,1])
print_tree(root)




