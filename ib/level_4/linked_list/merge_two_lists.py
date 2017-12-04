# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        n1 = A
        n2 = B

        if not n1:
            return n2
        elif not n2:
            return n1

        head = None

        if n1.val > n2.val:
            head = n2
            n2 = n2.next
        else:
            head = n1
            n1 = n1.next

        prev = head
        while n1 and n2:
            if n1.val > n2.val:
                prev.next = n2
                prev = n2
                n2 = n2.next
            else:
                prev.next = n1
                prev = n1
                n1 = n1.next

        if n1:
            prev.next = n1
        elif n2:
            prev.next = n2

        return head


head_1 = ListNode(5)
head_1.next = ListNode(8)
head_1.next.next = ListNode(20)

head_2 = ListNode(4)
head_2.next = ListNode(11)
head_2.next.next = ListNode(15)

head = Solution().mergeTwoLists(head_1, head_2)
node = head
while node:
    print(node.val)
    node = node.next
