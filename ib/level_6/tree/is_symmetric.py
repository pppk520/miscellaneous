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
        queue = [A]

        while True:
            tmp_queue = []        

            while len(queue) > 0:
                node = queue.pop(0)

                if node.left != None:
                    tmp_queue.append(node.left)

                if node.right != None:
                    tmp_queue.append(node.right)

            if len(tmp_queue) % 2 != 0:
                return False

            for i in range(len(tmp_queue) / 2):
                if tmp_queue[i].val != tmp_queue[len(tmp_queue) - 1 - i].val:
                    return False

            if len(tmp_queue) == 0:
                return True

            queue = tmp_queue        


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

