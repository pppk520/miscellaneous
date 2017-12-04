# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        self.all_sum = 0

        self.sum_internal(A, 0)
        return self.all_sum % 1003

    def sum_internal(self, root, pre_sum):
        if not root:
            return 0

        # leaf
        if not root.left and not root.right:
            self.all_sum += pre_sum + root.val
            return

        pre_sum += root.val
        self.sum_internal(root.left, pre_sum * 10)
        self.sum_internal(root.right, pre_sum * 10)
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(Solution().sumNumbers(root) == 25)

