# -*- coding:utf-8 -*-
# @time :2019.10.11
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju

# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成

# 双指针法，第一个指针作为慢指针，第二个指针作为快指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        p1 = 0
        p2 = 1

        while p2 < len(nums):

            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
            p2 += 1
        return p1 + 1