# -*- coding:utf-8 -*-
# @time :2019.10.11
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序



class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        p1 = 0  # 第一个指针

        p2 = 0  # 第二个指针

        while p2 < len(nums):

            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
