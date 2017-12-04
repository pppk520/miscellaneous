class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return 0

        d = {}
        md_map = {}

        for i, v in enumerate(A):
            if v not in d:
                d[v] = []

            d[v].append(i)
            md_map[i] = 0

        root_i = d[-1][0]

        for i in range(len(A)):
            if i not in d: # leaf                
                depth = 0
                while i != root_i:
                    md_map[i] = max(md_map[i], depth)
                    depth += 1
                    i = A[i]  # update index


        mpath = 0
        for i in d:
            md = -1 # if there is only one child
            for child_i in d[i]:
                mpath = max(mpath, md_map[child_i] + md + 2)
                md = max(md, md_map[child_i])

        return mpath

#print(Solution().solve([-1, 0, 0, 0, 3]) == 3)
#print(Solution().solve([-1, 0]) == 1)
print(Solution().solve([-1]) == 0)
