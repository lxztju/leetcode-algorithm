# -*- coding:utf-8 -*-
# @time :2019/11/23
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) 
# 使得 A[i] + B[j] + C[k] + D[l] = 0。
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500
# 所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1

#方法1：暴力法

# class Solution:
#     def fourSumCount(self, A, B, C, D) -> int:
#
#         a = len(A)
#         b = len(B)
#         c = len(C)
#         d = len(D)
#         res = 0
#         if a != b or b!=c or c!=d or d!=a:
#             raise Exception('the length of A,B,C,D must be equal.')
#
#         for i in range(a):
#             for j in range(b):
#                 for m in range(c):
#                     for n in range(d):
#                         if A[i] + B[j] + C[m] +D[n] ==0:
#                             res += 1
#
#         return res



#####方法2：将A+B 与C+D的所有可能的值放置在查找表中，进行计算
class Solution:
    def fourSumCount(self, A, B, C, D) -> int:

        a = len(A)
        b = len(B)
        c = len(C)
        d = len(D)
        res = 0
        if a != b or b!=c or c!=d or d!=a:
            raise Exception('the length of A,B,C,D must be equal.')

        from collections import defaultdict
        ab_dict = defaultdict(int)
        cd_dict = defaultdict(int)

        for i in range(a):
            for j in range(b):
                _sum = A[i] + B[j]
                ab_dict[_sum] += 1

        for i in range(c):
            for j in range(d):
                _sum = C[i] + D[j]
                cd_dict[_sum] += 1

        for k, v in ab_dict.items():
            target = 0 - k
            if target in cd_dict.keys():
                res += v * cd_dict[target]

        return res






s = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
res = s.fourSumCount(A,B, C, D)
print(res)