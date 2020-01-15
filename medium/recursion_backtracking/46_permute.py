# -*- coding:utf-8 -*-
# @time :2020/1/15
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



##回溯法

class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, get):

        if not nums:
            self.res.append(get)
            return

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], get + [nums[i]])
        return
