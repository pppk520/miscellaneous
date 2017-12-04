# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        length = self.get_ll_length(A)

        n1 = A
        n2 = A
        count = length / 2
        while count > 0:
            n2 = n2.next
            count -= 1

        n2 = self.reverse_ll(n2)

        node = n1
        next_node = n2
        while node:
            tmp = node.next
            node.next = next_node
            next_node = tmp
            node = node.next

        return n1

    def get_ll_length(self, head):
        node = head
        n = 0
        while node:
            n += 1
            node = node.next

        return n


    def reverse_ll(self, head):
        prev = None
        node = head
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        return prev

ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)

Solution().reorderList(ll)

node = ll
while node:
    print(node.val)    
    node = node.next

