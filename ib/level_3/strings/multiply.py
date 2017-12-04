# -*- coding: utf-8 -*-
'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
For example, 
given strings "12", "10", your answer should be “120”.

NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ). 
We will retroactively disqualify such submissions and the submissions will incur penalties.
'''

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        if len(A.strip().lstrip('0')) == 0: return '0'
        if len(B.strip().lstrip('0')) == 0: return '0'

        if len(B) > len(A): 
            A, B = B, A

        num_1 = [int(x) for x in A.strip()][::-1]
        num_2 = [int(x) for x in B.strip()][::-1]

        ret_arr = [0] * (len(num_1) + len(num_2))
        for i in range(len(num_2)):
            arr = self.multiply_v(num_1, num_2[i])
        
            for j in range(i):
                arr.insert(0, 0)
        
            ret_arr = self.sum_arr(ret_arr, arr)

        return ''.join([str(x) for x in ret_arr[::-1]]).lstrip('0')

    def multiply_v(self, num_arr, v):
        c = 0
        new_arr = []
        for i in range(len(num_arr)):
            result = num_arr[i] * v + c
            new_arr.append(result % 10)
            c = result / 10

        while c:
            new_arr.append(c % 10)
            c /= 10

        return new_arr

    def sum_arr(self, arr_1, arr_2):
        if len(arr_2) > len(arr_1):
            arr_1, arr_2 = arr_2, arr_1

        new_arr = []
        c = 0
        for i in range(len(arr_2)):
            result = arr_1[i] + arr_2[i] + c
            new_arr.append(result % 10)
            c = result / 10

        for j in range(len(arr_2), len(arr_1)):
            new_arr.append(arr_1[j] + c)
            c = 0

        return new_arr

if __name__ == '__main__':
    assert(Solution().multiply('12', '0') == '0')
    assert(Solution().multiply('12', '10') == '120')
    assert(Solution().multiply('99999', '99999') == '9999800001')


