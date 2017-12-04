class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        all_set = set()
        checked = set()

        for v in A:
            all_set.add(v)

        longest_count = 0
        for v in A:
            if v in checked:
                continue

            lv = v
            rv = v

            count = 1
            while (lv - 1) in all_set and not (lv - 1) in checked:
                count += 1
                checked.add(lv - 1)
                lv -= 1
            
            while (rv + 1) in all_set and not (rv + 1) in checked:
                count += 1
                checked.add(rv + 1)
                rv += 1

            longest_count = max(longest_count, count)               
 
        return longest_count


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
print(Solution().longestConsecutive([100, 999, 200, 1000, 1001, 2, 3, -1, 5]) == 3)
print(Solution().longestConsecutive([100, 999, -1, -2, 1001, 2, 3, -4, -3]) == 4)
