# -*- coding: utf-8 -*-
'''
You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available and you are also given how much time a painter takes to paint 1 unit of board. You have to get this job done as soon as possible under the constraints that any painter will only paint contiguous sections of board.

2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.
Return the ans % 10000003

Input :
K : Number of painters
T : Time taken by painter to paint 1 unit of board
L : A List which will represent length of each board

Output:
     return minimum time to paint all boards % 10000003
Example

Input : 
  K : 2
  T : 5
  L : [1, 10]
Output : 50
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        max_time = sum(C) * B * 2

        low = 0
        high = max_time
        last_possible_time = max_time
        while low <= high:
            target = (high + low) / 2
            
            if self.is_possible(A, target, C, B):
                high = target - 1
                last_possible_time = target
            else:
                low = target + 1

        return last_possible_time % 10000003

    def is_possible(self, painter_num, max_t, board, unit_t):
        t = 0
        p = 1
        min_val = max(board) * unit_t

        if min_val > max_t:
            return False

        for i in range(len(board)):
            tmp_t = t + board[i] * unit_t

            if tmp_t > max_t:
                p += 1
                t = board[i] * unit_t
                continue

            t = tmp_t

        if p > painter_num:
            return False

        if t > max_t:
            return False

        return True

if __name__ == '__main__':
    assert(Solution().paint(1, 1000000, [1000000, 1000000]) == 9400003)
    assert(Solution().paint(6, 10, [762, 798, 592, 899, 329]) == 8990)
    assert(Solution().paint(2, 3, [1,2,8,10]) == 33)
    assert(Solution().paint(3, 3, [1,2,8,10]) == 30)
    assert(Solution().paint(2, 5, [1,10]) == 50)
    assert(Solution().paint(2, 3, [7,2,1,8]) == 27)
    assert(Solution().paint(2, 3, [1,2,7,8]) == 30)


