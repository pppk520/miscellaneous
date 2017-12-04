class Solution:
    # @param A : list of integers
    # @return an integer
    def countInversions(self, A):
        self.inv = 0
        self.ms(A)

        return self.inv

    def ms(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.ms(arr[:mid])
        right = self.ms(arr[mid:])

        i = 0
        j = 0      
        k = 0  

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                self.inv += mid - i

            k += 1

        while i < mid:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr
        


print(Solution().countInversions([2, 4, 1, 3, 5]) == 3)
print(Solution().countInversions([84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60]) == 290)
