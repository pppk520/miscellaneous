'''
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3
'''

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        # keep B longer
        if len(A) > len(B):
            A, B = B, A

        if len(A) == 0:
            if len(B) % 2 == 1:
                return B[len(B) / 2]
            else:
                return (B[len(B) / 2] + B[len(B) / 2 - 1]) / 2.0

        ret = self.find_mid(A, B)

        return ret

    def find_mid(self, arr1, arr2):        
        m = len(arr1)
        n = len(arr2)

        total_middle = (m + n + 1) / 2
        is_odd = (m + n) % 2 == 1

        lo = 0
        hi = m

        while True:
            i = (lo + hi) / 2
            j = total_middle - i

            print('i = %s, j = %s' %(i, j))

            if i == 0:                
                if is_odd:
                    if arr1[0] > arr2[j - 1]:
                        return arr2[j - 1]
                    else:
                        return max(arr1[0], arr2[j - 2])
                else:
                    if arr1[0] > arr2[j - 1]:
                        return (min(arr1[i], arr2[j]) + arr2[j - 1]) / 2.0
                    else:
                        return (max(arr1[0], arr2[j - 2]) + arr2[j - 1]) / 2.0                        
            elif i < 0:
                j += i

                if is_odd:
                    return max(arr1[0], arr2[j - 1])
                else:
                    return (min(arr1[0], arr2[j - 1]) + min(arr1[0], arr2[j])) / 2.0
            elif i == m:
                if is_odd:
                    return max(arr1[m - 1], arr2[j - 1])
                else:
                    return (max(arr1[m - 1], arr2[j - 1]) + max(arr1[m - 1], arr2[j])) / 2.0

            if arr2[j - 1] > arr1[i]:
                lo = i + 1
            elif arr1[i - 1] > arr2[j]:
                hi = i - 1
            else:
                if is_odd:
                    return max(arr1[i - 1], arr2[j - 1])
                else:
                    return (max(arr1[i - 1], arr2[j - 1]) + min(arr1[i], arr2[j])) / 2.0

        

if __name__ == '__main__':
    assert(Solution().findMedianSortedArrays([ -3, -2, 1, 15], [-31, -11]) == -2.5)
    assert(Solution().findMedianSortedArrays([35], [1, 26, 35, 49]) == 35)
    assert(Solution().findMedianSortedArrays([16, 19], [-46, -15, -9, -7, -2, 24, 40]) == -2.0)
    assert(Solution().findMedianSortedArrays([-43, -25, -18, -15, -10, 9, 39, 40], [-2]) == -10.0)
    assert(Solution().findMedianSortedArrays([-50, -47, -36, -35, 0, 13, 14, 16], [-31, 1, 9, 23, 30, 39]) == 5.0)
    assert(Solution().findMedianSortedArrays([-26], [-49, 33, 35, 42]) == 33)
    assert(Solution().findMedianSortedArrays([-41, -33, -24, -21, -20, 27, 48], [-9]) == -20.5)
    assert(Solution().findMedianSortedArrays([-37, -10, -5, 5, 17, 34, 39], [-30, -27, -21, -21, 41]) == -7.5)
    assert(Solution().findMedianSortedArrays([0, 23], []) == 11.5)
    assert(Solution().findMedianSortedArrays([], [0, 23]) == 11.5)
    assert(Solution().findMedianSortedArrays([-49, 33, 35, 42], [-26]) == 33)
    assert(Solution().findMedianSortedArrays([], [20]) == 20)
    assert(Solution().findMedianSortedArrays([1,4,5], [2,3]) == 3)
    assert(Solution().findMedianSortedArrays([2,3], [1,4,5]) == 3)
    assert(Solution().findMedianSortedArrays([2,3], [1,4]) == 2.5)
    assert(Solution().findMedianSortedArrays([1,4], [2,3]) == 2.5)
    

