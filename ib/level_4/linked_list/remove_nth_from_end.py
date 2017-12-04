# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        node = A
        while B and node:
            node = node.next
            B -= 1

        # target is the head
        if not node:
            head = A.next
            return head

        target = A
        prev = None
        while node:
            node = node.next
            prev = target
            target = target.next

        prev.next = prev.next.next

        return A


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = Solution().removeNthFromEnd(head, 100)
node = head
while node:
    print(node.val)
    node = node.next

