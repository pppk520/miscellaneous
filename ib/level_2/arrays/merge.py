# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __cmp__(self, other):
        if self.start < other.start:
            return -1
        elif self.start > other.start:
            return 1
        else:
            return 0

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals or len(intervals) == 0:
            return []

        intervals = sorted(intervals)

        start = intervals[0].start
        end = intervals[0].end
        ret = []

        for interval in intervals[1:]:
            if interval.start > end:
                ret.append(Interval(start, end))
                start = interval.start
                end = interval.end
            else:
                end = max(end, interval.end)

        ret.append(Interval(start, end))

        return ret

intervals = [Interval(1, 3),
             Interval(8, 10),
             Interval(2, 6),
             Interval(15, 18)]


for interval in Solution().merge(intervals):
    print('(%s, %s)' %(interval.start, interval.end))



