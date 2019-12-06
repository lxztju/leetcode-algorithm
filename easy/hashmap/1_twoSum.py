# -*- coding:utf-8 -*-
# @time :2019.11.20
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# 给定一个整数数组和一个目标值，返回数组中和为目标值的索引
# 假设有惟一的解

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


###利用查找表
#循环搜索元素v，在v之前的元素放入查找表中，然后在查找表中进行查找，找到即可返回
# 没找到将现有的元素放入查找表，继续搜索
class Solution:
    def twoSum(self, nums, target):

        record = {}
        for i,v in enumerate(nums):

            diff_v = target - v

            if diff_v in record.keys():
                return [record[diff_v], i]
            else:
                record[v] = i

        raise Exception("there is no number for this target.")


s = Solution()

nums = [2,7,11,15]
target = 18
print(s.twoSum(nums,target))
