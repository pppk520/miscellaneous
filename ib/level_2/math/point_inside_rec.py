class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @return an integer
    def solve(self, A, B, C, D):
        a = (A[0], B[0])
        b = (A[1], B[1])
        c = (A[2], B[2])
        d = (A[3], B[3])

        ab = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
        ad = ((a[0] - d[0]) ** 2 + (a[1] - d[1]) ** 2) ** 0.5

        area = ab * ad

        epsilon = 0.000001
        count = 0
        for i in range(len(C)):
            p = (C[i], D[i])

            t1 = self.get_triangle_area(a, p, b)
            t2 = self.get_triangle_area(b, p, c)
            t3 = self.get_triangle_area(d, c, p)
            t4 = self.get_triangle_area(a, d, p)

#            print('area = %s, %s, %s, %s, %s' %(area, t1, t2, t3, t4))

            if abs(t1) < epsilon or abs(t2) < epsilon or abs(t3) < epsilon or abs(t4) < epsilon:
                continue

#            print('%s' %(abs(t1 + t2 + t3 + t4 - area)))

            if abs(t1 + t2 + t3 + t4 - area) < epsilon:
                count += 1

        print(count)
        return count        

    def get_triangle_area(self, a, b, c):
        return abs(a[0] * (b[1] - c[1]) + 
                   b[0] * (c[1] - a[1]) +
                   c[0] * (a[1] - b[1])) / 2.0

'''
print(Solution().solve([0, -2, 2, 4], 
                       [0, 2, 6, 4],
                       [1, 2, 1, 5, -3],
                       [3, 4, 2, 5, 1]) == 3)

print(Solution().solve([0, 6, 6, 0],
                       [0, 0, 8, 8],
                       [1, 2, 0, -1, 4],
                       [1, 4, 2, 5, 10]) == 2)
'''

print(Solution().solve([757806, 870553, 1208794, 1096047],
                       [750581, 637834, 976075, 1088822],
                       [-960840, -955568, -948123, -944567, -932689, -909006, -899213, -872499, -816231, -815487, -745458, -733965, -731767, -724160, -674483, -668124, -638622, -626199, -601653, -558231, -555957, -545997, -544386, -543614, -535798, -534548, -515867, -476700, -475144, -469624, -458175, -438328, -417182, -381407, -371638, -337506, -329494, -310312, -294120, -293259, -286345, -239709, -236737, -226459, -101763, -95015, -92985, -45365, -39041, -16265, 14345, 20699, 43223, 59858, 80467, 155882, 178162, 185280, 219005, 232976, 270563, 279358, 282342, 289593, 290780, 317859, 329292, 341423, 361695, 393776, 422139, 433328, 444707, 470220, 508399, 509636, 516573, 532007, 537797, 541645, 542654, 606489, 609080, 614672, 617072, 619918, 626655, 690373, 721697, 723175, 750776, 763166, 771255, 814811, 829093, 887413, 898447, 908990, 923037, 935731],
                       [-567401, -305898, -133127, 306804, -128699, 994624, -618554, -827823, 67682, 259449, 256638, 675439, 866179, 202790, -859640, -46451, -328534, 750143, 256970, -520372, -873728, 298573, -830382, 539967, -142881, 886848, -43491, -1859, -229702, 300055, 848590, -694308, -545489, 779474, 916511, -624980, 677863, 377492, 341491, -486602, 414689, 760790, 740840, -294549, -257631, -180968, -361856, -703029, -309178, -15868, -881165, 339541, -137928, -453872, -68725, -569599, -504392, 997206, -545062, 145377, -865567, 666039, -194872, 436167, 835283, -168730, 877227, 663200, -7680, -368684, -566371, 497670, -258796, 29626, -969593, 30447, -419927, -205084, -428907, -854872, 327835, -75951, -465094, -474657, 805466, 874210, 473763, -956825, -188138, -425076, -899816, 588745, -56595, 342698, 305541, 610272, -930175, 175954, 735343, 679916]) == 5)
