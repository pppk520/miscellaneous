'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
'''

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        N = len(A)

        for i in range(N):
            A[i] += (A[A[i]] % N) * N

        for i in range(N):
            A[i] /= N


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4]

    print(arr)
    Solution().arrange(arr)
    # [0, 1, 2, 3, 4]
    print(arr)  # arr[0] -> arr[arr[0]]

    arr = [1, 0, 2, 4, 3]
    print(arr)
    Solution().arrange(arr)
    # [0, 1, 2, 3, 4]
    print(arr)  # arr[0] -> arr[arr[0]]

    arr = [1, 4, 3, 0, 2]
    print(arr)
    Solution().arrange(arr)
    # [4, 2, 0, 1, 3]
    print(arr)  # arr[0] -> arr[arr[0]]

    arr = [4, 0, 2, 1, 3]
    print(arr)
    Solution().arrange(arr)
    # [3 4 2 0 1]
    print(arr)  # arr[0] -> arr[arr[0]]

