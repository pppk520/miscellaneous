class Solution:
    # @param n : integer
    # @param k : integer
    # @return a strings
    def getPermutation(self, n, k):
        ret = self.get_permu([_ for _ in range(1, n + 1)], k)
        return ''.join(map(str, ret))
        
    def get_permu(self, arr, k):
        import math

        if k == 1:
            return arr

        v = math.factorial(len(arr) - 1)
        idx = 0
        while k > v:
            idx += 1
            k -= v

        arr_left = arr[:]
        del arr_left[idx]

        ret = [arr[idx]]
        ret += self.get_permu(arr_left, k)

        return ret


print(Solution().getPermutation(3, 4) == "231")
print(Solution().getPermutation(11, 1) == "1234567891011")
