class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        arr = [[0 for _ in range(A)] for _ in range(A)]

        direction = 0
        val = 1
        
        i = 0
        j = 0
        items = A

        while items > 0:
            count = items

            while count > 0:
                arr[i][j] = val

                if direction == 0:
                    j += 1
                elif direction == 1:
                    i += 1
                elif direction == 2:
                    j -= 1
                else:
                    i -= 1

                val += 1
                count -= 1

            if direction == 0:
                items -= 1
                j -= 1
                i += 1
            elif direction == 1:
                i -= 1
                j -= 1
            elif direction == 2:
                j += 1
                i -= 1
                items -= 1
            else:
                i += 1
                j += 1

            # update direction                
            direction = (direction + 1) % 4            

        return arr


for row in Solution().generateMatrix(1):
    print(row)
