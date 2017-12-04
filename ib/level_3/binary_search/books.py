'''
N number of books are given. 
The ith book has Pi number of pages. 
You have to allocate books to M number of students so that maximum number of pages alloted to a student is minimum. A book will be allocated to exactly one student. Each student has to be allocated at least one book. Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.

NOTE: Return -1 if a valid assignment is not possible

Input:
 List of Books M number of students 

Your function should return an integer corresponding to the minimum number.

Example:

P : [12, 34, 67, 90]
M : 2

Output : 113

There are 2 number of students. Books can be distributed in following fashion : 
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113. 

'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if len(A) < B:
            return -1
        
        hi = sum(A) 
        lo = 0

        while lo < hi:
            mid = (lo + hi) / 2

            if self.is_possible(B, mid, A):
                hi = mid 
            else:
                lo = mid + 1

        return lo

    def is_possible(self, painter_num, max_t, board):
        t = 0
        p = 1
        min_val = max(board)

        if min_val > max_t:
            return False

        for i in range(len(board)):
            tmp_t = t + board[i]  

            if tmp_t > max_t:
                p += 1
                t = board[i] 
                continue

            t = tmp_t

        if p > painter_num:
            return False

        if t > max_t:
            return False

        return True
        



if __name__ == '__main__':
    assert(Solution().books([31, 14, 19, 75], 12) == -1)
    assert(Solution().books([12, 34, 67, 90], 2) == 113)
    assert(Solution().books([1,6,54,32,90,12,23,14], 5) == 90)

