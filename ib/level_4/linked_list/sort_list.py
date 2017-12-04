'''
Sort a linked list in O(n log n) time using constant space complexity.

Example :

Input : 1 -> 5 -> 4 -> 3

Returned list : 1 -> 3 -> 4 -> 5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head):
    node = head
    while node:
        print('%s -> ' %node.val)
        node = node.next

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        return self.sort_internal(A, 9999999999)

    def sort_internal(self, head, stop_n):
        n = self.get_ll_length(head, stop_n)

        if n <= 1:
            head.next = None
            return head

        if n == 2:
            if head.val < head.next.val:
                head.next.next = None
                return head
            else:
                tmp = head.next
                head.next = tmp.next
                tmp.next = head
                head.next = None
                return tmp

        middle = self.to_nth(head, n / 2)
        n1 = self.sort_internal(head, n / 2)
        n2 = self.sort_internal(middle, n - n / 2)

        # merge
        if n1.val > n2.val:
            new_head = n2
            n2 = n2.next
        else:
            new_head = n1
            n1 = n1.next

        prev = new_head
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

        return new_head

    def to_nth(self, head, n):
        count = n
        node = head
        while count > 0 and node:
            node = node.next
            count -= 1

        return node

    def get_ll_length(self, head, stop_n):
        node = head
        count = 0
        while node:
            count += 1

            if count == stop_n:
                break

            node = node.next

        return count

ll = ListNode(1)
ll.next = ListNode(3)
ll.next.next = ListNode(8)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(2)

Solution().sortList(ll)

node = ll
while node:
    print(node.val)
    node = node.next


