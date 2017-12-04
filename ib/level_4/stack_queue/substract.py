# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        n = self.get_len(A)
        target_idx = n / 2

        if n % 2 != 0:
            target_idx += 1

        node = A
        count = 1
        while count != target_idx:
            node = node.next
            count += 1

        tmp = node.next
        new_head = self.reverse_list(node.next)

        p1 = A
        p2 = new_head

        while p1 and p2:
            p1.val = p2.val - p1.val
            p1 = p1.next
            p2 = p2.next

        # reverse back
        new_head = self.reverse_list(new_head)

        return A

       
    def get_len(self, head):
        node = head
        length = 0

        while node:
            length += 1
            node = node.next

        return length

    def reverse_list(self, head):
        node = head
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        # new head
        return prev


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next  = ListNode(4)
#head.next.next.next.next = ListNode(5)

Solution().subtract(head)

node = head
while node:
    print(node.val) 
    node = node.next

 

