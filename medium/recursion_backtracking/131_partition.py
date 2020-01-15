# -*- coding:utf-8 -*-
# @time :2020/1/14
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


###回溯法

class Solution:
    def __init__(self):
        self.res = []

    def partition(self, s: str) -> List[List[str]]:
        self.dfs(s, [])
        return self.res

    def dfs(self, s, char):

        if not s:
            self.res.append(char)
            return

        for i in range(1, len(s) + 1):
            if s[:i] != s[:i][::-1]: continue
            self.dfs(s[i:], char + [s[:i]])
        return
