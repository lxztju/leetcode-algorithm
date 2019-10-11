# -*- coding:utf-8 -*-
# @time :2019.10.10
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju

# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去

class Solution:
    def mySqrt(self, x: int) -> int:

        target = x
        left = 0
        right = x // 2 + 1
        while left <= right:
            mid = (left + right) // 2
            square1 = mid ** 2
            square2 = (mid + 1) ** 2

            if square1 < target and square2 > target or square1 == target:
                return mid
            if square2 == target:
                return mid + 1

            if square2 < target:
                left = mid + 1
            else:
                right = mid