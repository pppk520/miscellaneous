class Solution:
    # @param root, a tree node
    # @return nothing
    def level_order(self, root):
        queue = [root]

        while len(queue) > 0:
            tmp_queue = []

            while len(queue) > 0:
                node = queue.pop(0)

                if node.left:
                    tmp_queue.append(node.left)

                if node.right:
                    tmp_queue.append(node.right)

            queue = tmp_queue

        return root

def print_tree(root):
    if not root:
        return

    if root.next:
        print('%s --> %s' %(root.val, root.next.val))
    else:
        print('%s --> %s' %(root.val, None))

    print_tree(root.left)
    print_tree(root.right)

root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left = TreeLinkNode(4)
root.left.right = TreeLinkNode(5)
root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)

print_tree(root)
print('-' * 10)
root = Solution().connect(root)
print_tree(root)


