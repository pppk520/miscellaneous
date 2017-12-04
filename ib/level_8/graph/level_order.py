# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        queue = [A]

        ret = []

        while len(queue) > 0:
            tmp_queue = []

            level = []
            while len(queue) > 0:
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    tmp_queue.append(node.left)
            
                if node.right:
                    tmp_queue.append(node.right)

            ret.append(level)
            queue = tmp_queue

        return ret


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().levelOrder(root))



