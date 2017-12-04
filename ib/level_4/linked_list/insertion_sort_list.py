'''
Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head = A
        h1 = head
        h2 = head.next

        h1_prev = None
        h2_prev = head

        while h2 != None:
            while h1.val <= h2.val and h1 != h2:
                h1_prev = h1
                h1 = h1.next

            if h1 == h2:
                # nothing happened
                h2_prev = h2
                h2 = h2.next
            else:
                # insert
                h2_prev.next = h2.next

                if h1_prev != None:
                    h1_prev.next = h2
                else:
                    head = h2

                h2.next = h1
                h2 = h2_prev.next

            h1_prev = None
            h1 = head
            
        return head

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)

head = Solution().insertionSortList(head)

node = head
while node:
    print(node.val)
    node = node.next
