class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        arr = A

        for i in range(9):
            if not self.is_valid_block(arr, i):
                return 0

        for r in range(9):
            seen = set()

            for c in range(9):
                if arr[r][c] == '.':
                    continue

                if arr[r][c] in seen:
                    return 0

                seen.add(arr[r][c])

        for c in range(9):
            seen = set()

            for r in range(9):
                if arr[r][c] == '.':
                    continue

                if arr[r][c] in seen:
                    return 0

                seen.add(arr[r][c])


        return 1
        
    def is_valid_block(self, arr, block_id):
        r = (block_id / 3) * 3
        c = (block_id % 3) * 3

        seen = set()
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if arr[i][j] == '.':
                    continue

                if arr[i][j] in seen:
                    return False
                
                seen.add(arr[i][j])

        return True


arr1 = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
arr2 = ["..5.....6", "....14...", ".........", ".....92..", "5....2...", ".......3.", "...54....", "3.....42.", "...27.6.." ]

print(Solution().isValidSudoku(arr1) == 1)
print(Solution().isValidSudoku(arr2) == 1)
