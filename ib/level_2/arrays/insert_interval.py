'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
'''

# Definition for an interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        if self.start == other.start and self.end == other.end:
            return True
      
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '(%s, %s)' %(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        curr_end = 0

        new_intervals = []
        for i, interval in enumerate(intervals):
            if new_interval.start > interval.end:
                new_intervals.append(interval)
                continue
            elif new_interval.end < interval.start:
                new_intervals.append(new_interval)

                for j in range(i, len(intervals)):
                    new_intervals.append(intervals[j]) # add remain
                
                return new_intervals
            else:
                # extend new_interval
                new_interval.start = min(interval.start, new_interval.start)
                new_interval.end = max(interval.end, new_interval.end)

        new_intervals.append(new_interval)

        return new_intervals


def is_lists_the_same(list_1, list_2):
    for int in list_1:
        print('list_1: ', int.start, int.end)

    for int in list_2:
        print('list_2: ', int.start, int.end)

    if len(list_1) != len(list_2):
        return False

    for idx, val in enumerate(list_1):
        if list_2[idx] != val:
            return False

    return True

def print_result(result):
    for item in result:
        print(item)

if __name__ == '__main__':
    '''
    intervals = [ (1, 2), (8, 10) ]
    new_interval = (3, 6)
    result = Solution().insert([Interval(li[0], li[1]) for li in intervals], Interval(new_interval[0], new_interval[1]))
    assert(is_lists_the_same(result, [Interval(1,2), Interval(3,6), Interval(8,10)]))

    intervals = [ (3, 6), (8, 10) ]
    new_interval = (1, 2)
    result = Solution().insert([Interval(li[0], li[1]) for li in intervals], Interval(new_interval[0], new_interval[1]))
    assert(is_lists_the_same(result, [Interval(1,2), Interval(3,6), Interval(8,10)]))

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,9]
    result = Solution().insert([Interval(li[0], li[1]) for li in intervals], Interval(new_interval[0], new_interval[1]))
    assert(is_lists_the_same(result, [Interval(li[0], li[1]) for li in [1,2],[3,10],[12,16]]))
    
    intervals = [ (31935139, 38366404), (54099301, 76986474), (87248431, 94675146) ]
    new_interval = (43262807, 68844111)
    result = Solution().insert([Interval(li[0], li[1]) for li in intervals], Interval(new_interval[0], new_interval[1]))
    assert(is_lists_the_same(result, [Interval(li[0], li[1]) for li in [(31935139, 38366404),(43262807, 76986474),(87248431, 94675146)]]))
    '''

    intervals = [ (137207, 1734370), (5057723, 5365773), (6997657, 7282669), (7992707, 8945780), (13205169, 13286380), (13478080, 14361199), (14648047, 16875188), (17296166, 19089625), (20424412, 20617334), (21947854, 23077086), (24901000, 26346402), (26650724, 27196856), (28896156, 29975691), (30071726, 31373629), (32397799, 33159528), (33305337, 35470848), (35720431, 37452993), (39147629, 40818780), (40930468, 41652526), (41938404, 44430212), (48114813, 48611161), (50335149, 51023917), (51878891, 52987379), (53902725, 54359910), (56661881, 58671175), (59326619, 61927945), (63215257, 63817507), (64968095, 65653303), (66634969, 67941460), (69980615, 71436951), (71564309, 74681566), (75530199, 76592769), (76988511, 77454928), (77665838, 78087358), (78229841, 79535243), (81250676, 82624050), (83142364, 84255671), (84379892, 84668384), (84954893, 85392199), (87804458, 90457067), (90760520, 91607160), (92361716, 92692045), (95399553, 97983139), (99776803, 99818745) ]
    new_interval = (108785977, 16197462)
    result = Solution().insert([Interval(li[0], li[1]) for li in intervals], Interval(new_interval[0], new_interval[1]))
    assert(is_lists_the_same(result, [Interval(li[0], li[1]) for li in [(137207, 1734370), (5057723, 5365773), (6997657, 7282669), (7992707, 8945780), (13205169, 13286380), (13478080, 14361199), (14648047, 108785977)]]))









