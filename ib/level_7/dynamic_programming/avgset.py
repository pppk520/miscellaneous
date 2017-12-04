class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def avgset(self, A):
        arr = sorted(A)

        total_sum = float(sum(arr))
        total_size = len(arr)

        self.cache = {}

        for target_size in range(total_size):
            target_sum = (total_sum * target_size) / total_size

            ret = self.get_size_sum(arr, 0, target_size, target_sum)
            if ret:
                ret = map(int, ret)
                compliment = self.get_compliment(arr, ret)

                if len(ret) > len(compliment):
                    return [compliment, ret]
                elif len(ret) < len(compliment):
                    return [ret, compliment]
                else:
                    return sorted([ret, compliment])

        return []

    def get_compliment(self, arr, target_arr):
        ret = []
        target = target_arr[:]

        for v in arr:
            if v not in target:
                ret.append(v)
            else:
                target.remove(v)

        return ret

    def get_size_sum(self, arr, start, target_size, target_sum):
        if target_sum < 0:
            return

        if target_size == 0 or target_size > len(arr) - start:
            return

        if target_size == 1:
            if target_sum in arr[start:]:
                return [target_sum]
            else:
                return

        # include current
        key = (start + 1, target_size - 1, target_sum - arr[start])
        if not key in self.cache:
            ret = self.get_size_sum(arr, start + 1, target_size - 1, target_sum - arr[start])
            self.cache[key] = ret
           
        if self.cache[key]:
            return [arr[start]] + self.cache[key]

        # not include current
        key = (start + 1, target_size, target_sum)
        if not key in self.cache:
            ret = self.get_size_sum(arr, start + 1, target_size, target_sum)
            self.cache[key] = ret
           
        if self.cache[key]:
            return self.cache[key]

        return 

if __name__ == '__main__':
    print(Solution().avgset([36, 19, 49, 1, 18, 41, 9, 13, 19, 31, 11, 16, 47, 27, 8, 11, 33, 0, 0, 35, 12, 25]))
    print(Solution().avgset([31, 8, 11, 36, 6, 17, 41, 9, 36, 49, 1, 42, 34, 27, 27, 44, 30, 5, 23, 18, 42, 26, 7, 43]))

#    print(Solution().get_sum_size(sorted([16, 42, 18, 48, 26, 45, 46, 26, 25, 7, 7, 48, 30, 10, 10, 3, 1, 11, 33, 14, 21, 15]), 0, float(251), 11))

    # [1 3 7 7 10 10 26 45 46 48 48 ] [11 14 15 16 18 21 25 26 30 33 42 ] 
    print(Solution().avgset([16, 42, 18, 48, 26, 45, 46, 26, 25, 7, 7, 48, 30, 10, 10, 3, 1, 11, 33, 14, 21, 15]))
    
#    print(Solution().get_sum_size(sorted([28, 10, 2, 44, 33, 31, 39, 46, 1, 24, 32, 31, 28, 9, 13, 40, 46, 1, 16, 18, 39, 13, 48, 5]), 199, 8))

    # [1 1 2 16 39 46 46 48 ] [5 9 10 13 13 18 24 28 28 31 31 32 33 39 40 44 ] 
    print(Solution().avgset([28, 10, 2, 44, 33, 31, 39, 46, 1, 24, 32, 31, 28, 9, 13, 40, 46, 1, 16, 18, 39, 13, 48, 5]))
    '''
    print(Solution().avgset([47, 14, 30, 19, 30, 4, 32, 32, 15, 2, 6, 24]))
    print(Solution().avgset([18, 29, 0, 47, 0, 41, 40, 28, 7, 1]))
    print(Solution().avgset([19, 5, 38, 22, 44, 12, 17, 35 ]))
    print(Solution().avgset([1, 7, 15, 29, 11, 9]))
    '''


