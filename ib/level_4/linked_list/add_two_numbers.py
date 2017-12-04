# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        p1 = A
        p2 = B

        head = ListNode(-1)
        c = 0
        p = head

        while p1 and p2:            
            val = (p1.val + p2.val + c) % 10
            c = (p1.val + p2.val + c) / 10
            p.next = ListNode(val)
            p = p.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            val = (p1.val + c) % 10
            c = (p1.val + c) / 10
            p.next = ListNode(val)
            p1 = p1.next
            p = p.next

        while p2:
            val = (p2.val + c) % 10
            c = (p2.val + c) / 10
            p.next = ListNode(val)
            p2 = p2.next
            p = p.next

        if c:
            p.next = ListNode(c)

        # remove training 0s
        p = head
        zero_pre = None
        while p.next:
            if p.next.val == 0:
                zero_pre = p
            else:
                zero_pre = None

            p = p.next

        if zero_pre:
            zero_pre.next = None

        return head.next


'''
head_1 = ListNode(2)
head_1.next = ListNode(4)
head_1.next.next = ListNode(3)
head_1.next.next.next = ListNode(0)

head_2 = ListNode(5)
head_2.next = ListNode(6)
head_2.next.next = ListNode(4)

head = Solution().addTwoNumbers(head_1, head_2)
node = head
while node:
    print(node.val)
    node = node.next
'''

head_1 = ListNode(1)

head_2 = ListNode(9)
head_2.next = ListNode(9)
head_2.next.next = ListNode(9)

head = Solution().addTwoNumbers(head_1, head_2)
node = head
while node:
    print(node.val)
    node = node.next
