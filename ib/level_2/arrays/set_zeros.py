'''
Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

Do it in place.

Example

Given array A as

1 0 1
1 1 1 
1 1 1
On returning, the array A should be :

0 0 0
1 0 1
1 0 1
Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity.
'''

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        n = len(A)
        m = len(A[0])

        zero_is = set()
        zero_js = set()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    zero_is.add(i)
                    zero_js.add(j)

        for i in zero_is:
            for j in range(m):
                A[i][j] = 0

        for j in zero_js:
            for i in range(n):
                A[i][j] = 0

        return A

def print_ll(ll):
    for l in ll:
        print(l)

if __name__ == '__main__':
    ll = [[0, 0],
          [1, 1]]
    print_ll(ll)

    Solution().setZeroes(ll)

    print('')
    print_ll(ll)

    # ------------    
    ll = [[1, 1, 1],
          [0, 1, 1],
          [1, 1, 1]]

    print_ll(ll)

    Solution().setZeroes(ll)

    print('')
    print_ll(ll)


    # ------------

            


