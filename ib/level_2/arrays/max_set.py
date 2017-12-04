'''
A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_sub = []
        max_sum = 0
        max_len = 0

        start = 0
        for i in range(len(A)):
            if A[i] < 0:
                start += 1
            else:
                break        

        curr_sum = 0
        for i in range(start, len(A)):
            if A[i] < 0:
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    max_sub = A[start:i]
                    max_len = i - start
                elif curr_sum == max_sum:
                    if (i - start) > max_len:
                        max_sub = A[start:i] 
                        max_len = i - start
            
                start = i + 1
                curr_sum = 0
            else:
                curr_sum += A[i]

        # last sub
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_sub = A[start:]
        elif curr_sum == max_sum:
           if (len(A) - start) > max_len:
               max_sub = A[start:]

        return max_sub

print(Solution().maxset([-54961, 3510, -50805, -82137, -39096, -47421]))
print(Solution().maxset([-1, -1, -1, -1, -1]))
print(Solution().maxset([1, 2, 3, -7, 1, 1, 1, 3]))
print(Solution().maxset([0, 0, -1, 0]))
print(Solution().maxset([0, 0, -1, 0, 0, 0]))
print(Solution().maxset([0, 0, 0, -1, 0, 0]))
print(Solution().maxset([1, -1, 0, 1, 2]))
print(Solution().maxset([-7]))
print(Solution().maxset([1, 2, 5, -7, 2, 3]))
print(Solution().maxset([1, 2, 5, -7, 3, 4, 2, 3]))   
