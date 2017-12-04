# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []

        self.push_left(root)

    def push_left(self, node):
        if node == None:
            return

        self.stack.append(node)

        while node.left:
            node = node.left
            self.stack.append(node)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        self.push_left(node.right)

        return node.val

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.right.right = TreeNode(8)
root.right.left = TreeNode(3.5)

i = BSTIterator(root)
while i.hasNext():
    print i.next()


