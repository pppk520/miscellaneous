# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        org_root = root

        while True:
            node = root

            last = None
            while node:
                if node.left:
                    if last:
                        last.next = node.left

                    node.left.next = node.right

                if node.right:
                    last = node.right
            
                node = node.next

            if root:
                root = root.left
            else:
                return org_root

root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.left.left = TreeLinkNode(3)
root.left.right = TreeLinkNode(4)
root.right = TreeLinkNode(5)
root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)

Solution().connect(root)

node = root
while node:
    level_node = node
    levels = []
    while level_node:
        levels.append(str(level_node.val))
        level_node = level_node.next

    print(' -> '.join(levels))
    node = node.left











