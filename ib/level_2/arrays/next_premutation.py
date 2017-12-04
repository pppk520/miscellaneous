class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        idx = None

        '''
            1 2 3 7 6 5 4
                  ^ 
            1 2 4 3 4 5 6
        '''
        for i in range(len(A) - 1, 0, -1):
            if A[i] > A[i - 1]:
                idx = i
                break

        if not idx:
            A.sort()
            return A

        apd_i = -1
        for i in range(1, idx + 1):
            if A[-i] > A[idx - 1]:
                apd_i = -i
                break


        snd_part = sorted(A[idx - 1:])
        snd_part.remove(A[apd_i])

        ll = A[:idx - 1] + [A[apd_i]] + snd_part

        return ll




print(Solution().nextPermutation([444, 994, 508, 72, 125, 299, 181, 238, 354, 223, 691, 249, 838, 890, 758, 675, 424, 199, 201, 788, 609, 582, 979, 259, 901, 371, 766, 759, 983, 728, 220, 16, 158, 822, 515, 488, 846, 321, 908, 469, 84, 460, 961, 285, 417, 142, 952, 626, 916, 247, 116, 975, 202, 734, 128, 312, 499, 274, 213, 208, 472, 265, 315, 335, 205, 784, 708, 681, 160, 448, 365, 165, 190, 693, 606, 226, 351, 241, 526, 311, 164, 98, 422, 363, 103, 747, 507, 669, 153, 856, 701, 319, 695, 52])) # 444 994 508 72 125 299 181 238 354 223 691 249 838 890 758 675 424 199 201 788 609 582 979 259 901 371 766 759 983 728 220 16 158 822 515 488 846 321 908 469 84 460 961 285 417 142 952 626 916 247 116 975 202 734 128 312 499 274 213 208 472 265 315 335 205 784 708 681 160 448 365 165 190 693 606 226 351 241 526 311 164 98 422 363 103 747 507 669 153 856 701 695 52 319

print(Solution().nextPermutation([1,2,3])) # 1,3,2
print(Solution().nextPermutation([20,50,113])) # 20, 113, 50
print(Solution().nextPermutation([1,1,5])) # 1,5,1
