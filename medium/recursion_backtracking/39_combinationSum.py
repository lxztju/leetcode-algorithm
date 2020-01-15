# -*- coding:utf-8 -*-
# @time :2020/1/15
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



##回溯法，优化一部分
class Solution:

    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.dfs(candidates, target, [])
        return self.res

    def dfs(self, nums, target, get):

        if target == 0:
            self.res.append(get)
            return
        if target < 0:
            return

        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], get + [nums[i]])
        return

##回溯法，继续剪枝
class Solution:

    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.dfs(candidates, target, [])
        return self.res

    def dfs(self, nums, target, get):

        if target == 0:
            self.res.append(get)
            return
        if target < 0:
            return

        for i in range(len(nums)):
            if nums[i] > target: continue
            self.dfs(nums[i:], target - nums[i], get + [nums[i]])
        return
