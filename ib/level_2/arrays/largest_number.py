'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = sorted(A, cmp=self.my_compare, reverse=True)

        ret = ''.join(map(str, A)).lstrip('0')

        if len(ret) == 0:
            ret = '0'

        return ret

    def my_compare(self, x, y):
        v1 = int('%s%s' %(x, y))
        v2 = int('%s%s' %(y, x))

        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0



if __name__ == '__main__':
    assert(Solution().largestNumber([ 931, 94, 209, 448, 716, 903, 124, 372, 462, 196, 715, 802, 103, 740, 389, 872, 615, 638, 771, 829, 899, 999, 29, 163, 342, 902, 922, 312, 326, 817, 288, 75, 37, 286, 708, 589, 975, 747, 743, 699, 743, 954, 523, 989, 114, 402, 236, 855, 323, 79, 949, 176, 663, 587, 322 ]) == '9999899759549499493192290390289987285582981780279771757477437437407167157086996636386155895875234624484023893737234232632332231229288286236209196176163124114103')
    assert(Solution().largestNumber([ 12, 121 ]) == '12121')
    assert(Solution().largestNumber([ 9, 99, 999, 9999, 9998 ]) == '99999999999998')
    assert(Solution().largestNumber([ 0, 0, 0, 0, 0 ]) == '0')
    assert(Solution().largestNumber([ 472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412 ]) == '9648527226766636354854724412368319')
    assert(Solution().largestNumber([ 782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357, 261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298, 470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905 ]) == '99197494093090589587787286882579979879178278077273570968668667867566465335024704093953663633573372982927126124019124113')


