# -*- coding:utf-8 -*-
# @time :2020/1/15
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju




##回溯法，找到所有的并剔除掉已经存在的
class Solution:
    def __init__(self):
        self.res = []
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, get):

        if not nums:
            if get not in self.res:
                self.res.append(get)
            return

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], get + [nums[i]])
        return


##回溯法，已经扫描存在的节点，后边直接跳过
class Solution:
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, get):

        if not nums:
            self.res.append(get)
            return

        for i in range(len(nums)):
            if nums[i] in nums[:i]: continue
            self.dfs(nums[:i] + nums[i + 1:], get + [nums[i]])
        return
