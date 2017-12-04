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
        ll = []
        stack = [A]
        
        while len(stack) > 0:
            node = stack.pop()

            if node == None:
                continue

            ll.append(node.val)

            stack.append(node.right)
            stack.append(node.left)

        return ll

if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(4)
    print(Solution().preorderTraversal(root))  # 01324
