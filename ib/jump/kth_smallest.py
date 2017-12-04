'''
Find the kth smallest element in an unsorted array of non-negative integers.

Definition of kth smallest element

 kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based ) 
NOTE
You are not allowed to modify the array ( The array is read only ). 
Try to do it using constant extra space.

Example:

A : [2 1 4 3 2]
k : 3

answer : 2
'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, k):
        lo = min(A)
        hi = max(A)

        while lo <= hi:
            mid = (lo + hi) / 2
            c_less = 0
            c_eq = 0

            for v in A:
                if v < mid:
                    c_less += 1
                elif v == mid:
                    c_eq += 1
            
            if c_less < k and k <= c_less + c_eq:
                return mid
            elif c_less >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        

print(Solution().kthsmallest((2,1,4,3,2), 3) == 2)
print(Solution().kthsmallest((1,2,3,100,150,300, 9999999), 4) == 100)
