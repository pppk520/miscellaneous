class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        import heapq

        h = []
        for v in B:
            heapq.heappush(h, -v)

        ret = 0
        while A > 0:
            v = heapq.heappop(h) * -1
            ret += v

            heapq.heappush(h, (v/2) * -1)
            A -= 1

        return int(ret) % (10**9 + 7)


print(Solution().nchoc(3, [6, 5]) == 14)
print(Solution().nchoc(10, [2147483647, 2000000014, 2147483647]) == 284628164)
