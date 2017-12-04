'''
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        i = 0
        j = 0
        k = 0

        min_val = 9999999999
        while i < len(A) and j < len(B) and k < len(C):
            min_tmp = min(A[i], B[j], C[k])
            min_val = min(min_val, abs(max(A[i], B[j], C[k]) - min_tmp))
        
            if i < len(A) - 1:
                if A[i] == min_tmp:
                    i += 1
                    continue
            else:
                if B[j] < C[k]:
                    if j < len(B) - 1:
                        j += 1
                        continue
                    else:
                        k += 1
                        continue
                else:
                    if k < len(C) - 1:
                        k += 1
                        continue
                    else:
                        j += 1
                        continue

            if j < len(B) - 1:
                if B[j] == min_tmp:
                    j += 1
                    continue
            else:
                if A[i] < C[k]:
                    if i < len(A) - 1:
                        i += 1
                        continue
                    else:
                        k += 1
                        continue
                else:
                    if k < len(C) - 1:
                        k += 1
                        continue
                    else:
                        i += 1
                        continue

            if k < len(C) - 1:
                if C[k] == min_tmp:
                    k += 1
                    continue
            else:
                if A[i] < B[j]:
                    if i < len(A) - 1:
                        i += 1
                        continue
                    else:
                        j += 1
                        continue
                else:
                    if j < len(B) - 1:
                        j += 1
                        continue
                    else:
                        i += 1
                        continue

        return min_val





print(Solution().solve([1, 4, 5, 8, 10], [6, 9, 15], [2, 3, 6, 6]) == 1)
print(Solution().solve([1, 4, 5, 8, 10], [1, 6, 9, 15], [100, 200, 300, 400]) == 200)
