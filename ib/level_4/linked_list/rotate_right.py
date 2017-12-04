# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if not A:
            return None

        node = A
        n = 0
        while node:
            n += 1
            node = node.next

        k = B % n

        if k == 0:
            return A

        p1 = A
        p1_prev = None
        p2 = A
        p2_prev = None
        while k:
            p2 = p2.next
            k -= 1

        while p2:
            p1_prev = p1
            p1 = p1.next
            p2_prev = p2
            p2 = p2.next

        p1_prev.next = None
        head = p1

        p2_prev.next = A

        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = Solution().rotateRight(head, 4)
node = head
while node:
    print(node.val)
    node = node.next
