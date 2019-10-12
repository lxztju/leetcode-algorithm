# -*- coding:utf-8 -*-
# @time :2019.10.12
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju


# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。


class Solution:
    def findKthLargest(self, nums, k: int) -> int:

        nums = sorted(nums)

        return nums[-1 * k]
