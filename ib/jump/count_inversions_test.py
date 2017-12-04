class Solution:
    # @param A : list of integers
    # @return an integer
#    def countInversions(self, A):
    def countInversions(self, a):
      res = 0
      counts = [0]*(len(a)+1)
      rank = { v : i+1 for i, v in enumerate(sorted(a)) }

      print(a)
      for key in rank:
          print('%s: %s' %(key, rank[key]))

      for x in reversed(a):
        i = rank[x] - 1
        while i:
          res += counts[i]
          i -= i & -i
        i = rank[x]
        while i <= len(a):
          counts[i] += 1
          i += i & -i

        print('x = %s' %x)
        print(counts)

      return res

#print(Solution().countInversions([2, 4, 1, 3, 5]) == 3)
print(Solution().countInversions([84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60]) == 290)
