# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def cntMatrix(self, A, B):
        self.count = 0
        self.possible = True

        self.recur(A, B, A.val, 999999999999999999)

        if not self.possible:
            return -1

        return self.count

    def recur(self, root_1, root_2, rmin, rmax):
        if not root_2:
            return

        if (root_1.left and not root_2.left) or (root_1.right and not root_2.right):
            self.possible = False
            return

        if root_2.left:
            if not root_1.left:
                # free to insert anything
                self.count += self.get_node_count(root_2.left)
            else:
                self.recur(root_1.left, root_2.left, rmin, root_1.val)

        if root_2.right:
            if not root_1.right:
                root_1.right = TreeNode(root_1.val + 1)
                self.count += 1 # inserted root_1.right

            self.recur(root_1.right, root_2.right, root_1.val + 1, rmax)

    def get_node_count(self, root):
        if not root:
            return 0

        count = 1
        count += self.get_node_count(root.left)
        count += self.get_node_count(root.right)

        return count


root_1 = TreeNode(10)
root_1.left = TreeNode(9)
root_1.right = TreeNode(20)
root_1.right.right = TreeNode(21)

root_2 = TreeNode(5)
root_2.left = TreeNode(2)
root_2.right = TreeNode(7)
root_2.left.left = TreeNode(1)

print(Solution().cntMatrix(root_1, root_2) == -1)

root_1 = TreeNode(10)
root_1.left = TreeNode(9)
root_1.right = TreeNode(20)

root_2 = TreeNode(5)
root_2.left = TreeNode(2)
root_2.right = TreeNode(7)
root_2.left.left = TreeNode(1)

print(Solution().cntMatrix(root_1, root_2) == 1)


