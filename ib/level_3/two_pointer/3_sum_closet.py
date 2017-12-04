class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()

        closest = 99999999999
        ret = 0
        for i in range(len(A)):
            j = i + 1
            k = len(A) - 1

            while j < k:
                s = A[i] + A[j] + A[k]
                if abs(s - B) < closest:
                    closest = abs(s - B)
                    ret = s
       
                if s > B:
                    k -= 1
                elif s < B:
                    j += 1
                else:
                    return B 

        return ret

print(Solution().threeSumClosest([-1,2,1,-4], 1) == 2)
