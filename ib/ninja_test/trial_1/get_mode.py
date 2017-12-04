class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def getMode(self, A, B):
        d = {}

        for v in A:
            if not v in d:
                d[v] = 1
            else:
                d[v] += 1

        ret = []

        for idx, new_val in B:
            old_val = A[idx - 1]
            A[idx - 1] = new_val

            d[old_val] -= 1
            if not new_val in d:
                d[new_val] = 1
            else:
                d[new_val] += 1            

            if d[old_val] == 0:
                del d[old_val]
 
            ret.append(self.mode(d))

        return ret

    def mode(self, d):
        m = None        
        count = None

        for k in d:
            if not m:
                m = k
                count = d[k]

            if d[k] == count:
                if k < m:
                    m = k
                    count = d[k]
            elif d[k] > count:
                m = k
                count = d[k]
                

        return m


arr = [2, 2, 2, 3, 3]
updates = [[1, 3],
           [5, 4],
           [2, 4] ]

print(Solution().getMode(arr, updates))
