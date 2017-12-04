# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        import heapq

        h = []

        for idx in range(len(A)):
            if A[idx]:
                heapq.heappush(h, (A[idx].val, idx))
                A[idx] = A[idx].next

        val, idx = heapq.heappop(h)
        head = ListNode(val)
        head_ptr = head

        if A[idx]:
            heapq.heappush(h, (A[idx].val, idx))
            A[idx] = A[idx].next

        while len(h) > 0:
            val, idx = heapq.heappop(h)
            new_node = ListNode(val)
            head_ptr.next = new_node
            head_ptr = new_node

            if A[idx]:
                heapq.heappush(h, (A[idx].val, idx))
                A[idx] = A[idx].next

        return head

def print_by_head(head):
    node = head
    while node:
        print(node.val)
        node = node.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(10)
    l1.next.next = ListNode(20)
#    print_by_head(l1)
    
    l2 = ListNode(4)
    l2.next = ListNode(11)
    l2.next.next = ListNode(13)
#    print_by_head(l2)

    l3 = ListNode(3)
    l3.next = ListNode(8)
    l3.next.next = ListNode(9)
#    print_by_head(l3)

    print_by_head(Solution().mergeKLists([l1, l2, l3]))


    



