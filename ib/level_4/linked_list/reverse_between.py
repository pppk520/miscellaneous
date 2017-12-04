# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if m == n: return A

        head = A
        m_node = head
        m_prev = None

        while m > 1:
            m_prev = m_node
            m_node = m_node.next
            m -= 1            
            n -= 1

        prev = None
        node = m_node
        
        while n > 0:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            n -= 1

        # x -> x -> m_prev [ m_node <- x <- x <- prev ] node -> x -> None
        
        # link the first part to the start of reversed part
        if m_prev: 
            m_prev.next = prev

        # link the reversed part
        m_node.next = node
        
        # the first part is empty
        # the new head is the head of reversed part
        if m_node == head:
            head = prev
            
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
#head.next.next.next = ListNode(4)
#head.next.next.next.next = ListNode(5)

#Solution().reverseBetween(head, 2, 4)
head = Solution().reverseBetween(head, 1, 2)

node = head
while node:
    print(node.val)
    node = node.next


