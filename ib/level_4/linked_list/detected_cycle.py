'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        p1 = A
        p2 = A

        meet = False
        while p1 and p2:
            p1 = p1.next

            if meet:
                p2 = p2.next
            else: 
                # double steps
                p2 = p2.next
                if not p2:
                    return None

                p2 = p2.next

            if p1 == p2:
                if meet:
                    return p1

                # has cycle
                meet = True
                p1 = A


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next= head.next.next

print(Solution().detectCycle(head).val)
