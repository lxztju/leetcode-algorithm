# -*- coding:utf-8 -*-
# @time :2020/1/15
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



##回溯法
class Solution:
    def __init__(self):
        self.res = []


    def combine(self, n: int, k: int) -> List[List[int]]:

        self.dfs(n, k, 1, [])
        return self.res

    def dfs(self, n, k, start, get):

        if k == 0:
            self.res.append(get)
            return

        for i in range(start, n+1):
            self.dfs(n, k-1, i+1, get + [i] )
        return


#回溯法剪枝

class Solution:
    def __init__(self):
        self.res = []


    def combine(self, n: int, k: int) -> List[List[int]]:

        self.dfs(n, k, 1, [])
        return self.res

    def dfs(self, n, k, start, get):

        if k == 0:
            self.res.append(get)
            return

        for i in range(start, n + 1):
            if n+1 - start < k: continue
            self.dfs(n, k-1, i+1, get + [i] )
        return