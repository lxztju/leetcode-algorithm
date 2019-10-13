# -*- coding:utf-8 -*-
# @time :2019.10.12
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

## 方法1： 使用通用基础的排序算法

# class Solution:
    # def sortColors(self, nums) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """

## 方法二：计数排序
#统计0,1,2的数目，并放入数组中

# class Solution:
#     def sortColors(self, nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         count = [0, 0, 0]
#
#         for i in nums:
#             if i == 0:
#                 count[0] += 1
#             elif i == 1:
#                 count[1] += 1
#             else:
#                 assert i == 2
#                 count[2] += 1
#         mid = count[0] + count[1]
#
#         for i in range(len(nums)):
#
#             if i < count[0]:
#                 nums[i] = 0
#             elif i < mid:
#                 nums[i] = 1
#             else:
#                 nums[i] = 2


## 方法三： 三路快排
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = -1 # 第一个指针,指示0区域的头部
        two = len(nums)  # 第二个指针，指示2区域的尾部
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                i += 1
                continue
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1



