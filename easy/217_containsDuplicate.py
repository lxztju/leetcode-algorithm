# -*- coding:utf-8 -*-
# @time :2019/11/24
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。



class Solution:
    def containsDuplicate(self, nums) -> bool:

        if not nums or len(nums) < 1:
            return False


        num_set = set()



        for num in nums:

            if num not in num_set:
                num_set.add(num)
            else:
                return True

        return False