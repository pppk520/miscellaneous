class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        need_switch = 0

        count = 0
        for v in A:
            if v == need_switch:
                count += 1
                need_switch = 1 if need_switch == 0 else 0
        
        return count

print(Solution().bulbs([0,1,0,1]) == 4)
