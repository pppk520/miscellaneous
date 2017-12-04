class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        occupied = []
        for i in range(len(A)):
            if A[i] == 'x':
                occupied.append(i)

        if len(occupied) == 0:
            return 0

        mean = occupied[len(occupied) // 2]

        j1 = self.get_jumps(A, range(mean, -1, -1), -1)
        j2 = self.get_jumps(A, range(mean + 1, len(A)), 1)

        j3 = self.get_jumps(A, range(mean, len(A)), 1)
        j4 = self.get_jumps(A, range(mean - 1, -1, -1), -1)

        return min(j1 + j2, j3 + j4) % 10000003

    def get_jumps(self, A, iters, direction):
        pos = -1

        count = 0
        for i in iters:
            if A[i] == '.':
                if pos == -1:
                    pos = i
            else:
                if pos == -1:
                    continue

                count += abs(pos - i)
                pos += direction

        return count

if __name__ == '__main__':
    assert(Solution().seats('....') == 0)
    assert(Solution().seats('............x.x') == 1)
    assert(Solution().seats('xx..xxxx...x.......x.x.x.xxxxxxxx.') == 96)
    assert(Solution().seats('x') == 0)
    assert(Solution().seats('x.x.xx.x.xxx.......x..x.xxx..x.xxx') == 102)
    assert(Solution().seats('xxxx..xx...x..') == 9)
    assert(Solution().seats('....x..xx...x..') == 5)

