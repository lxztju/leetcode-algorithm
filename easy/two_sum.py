# -*- coding:utf-8 -*-
# @time :2019.09.08
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# 给定一个整数数组和一个目标值，返回数组中和为目标值的索引
# 假设有惟一的解

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

#1、利用暴力法，直接两遍循环进行处理，时间复杂度为n2
#2、利用哈希表，在python中可以使用字典

##方法一（暴力法）：
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            second_num = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] ==second_num:
                    return [i,j]










####方法二（利用字典）：
class Solution:
    def twoSum(self, nums, target):
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                return [hash_dict[nums[i]], i]
            else:
                hash_dict[target - nums[i]] = i
