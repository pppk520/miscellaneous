class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive = sorted(arrive)
        depart = sorted(depart)

        i = 0
        j = 0
        count = 0
        need_rooms = 0

        while i < len(arrive) and j < len(depart):
            if arrive[i] < depart[j]:
                count += 1
                i += 1
                need_rooms = max(need_rooms, count)
            else:
                count -= 1
                j += 1

        return need_rooms <= K            



print(Solution().hotel([1,3,5],
                       [2,6,8], 1) == 0)
