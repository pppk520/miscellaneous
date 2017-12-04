class Solution:
    def sorted_list_to_bst(self, head):
        return self.recur(head, None)

    def recur(self, head, tail):
        if not head or head == tail:
            return None

        if head.next == tail:
            return TreeNode(head.val)

        fast = head
        slow = head

        while (fast != tail and fast.next != tail):
            fast = fast.next.next
            slow = slow.next

        # now slow is at middle
        root = TreeNode(slow.val)
        root.left = self.recur(head, slow)
        root.right = self.recur(slow.next, tail)

        return root




