class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def get_left_height(self, root):
        node = root

        h = 0
        while node:
            h += 1
            node = node.left

        return h

    def count_nodes(self, root):
        if not root:
            return 0

        l_height = self.get_left_height(root.left)
        r_height = self.get_left_height(root.right)

        count = 0
        if l_height == r_height:
            # left is full complete
            return (1 << l_height) + self.count_nodes(root.right)

        # right is full complete
        return (1 << r_height) + self.count_nodes(root.left)



