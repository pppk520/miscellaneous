# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        arr = []

        node = A
        while node:
            arr.append(node.val)
            node = node.next

        return self.build_tree(arr, 0, len(arr))

    def build_tree(self, arr, start, end):
        n = end - start

        if n == 1:
            return TreeNode(arr[start])

        if n == 0:
            return None

        mid = start + n / 2
        root = TreeNode(arr[mid])
        root.left = self.build_tree(arr, start, mid)
        root.right = self.build_tree(arr, mid + 1, end)

        return root


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

root = Solution().sortedListToBST(head)

def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)

inorder(root)
