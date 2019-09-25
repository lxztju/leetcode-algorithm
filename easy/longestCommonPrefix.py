# -*- coding:utf-8 -*-
# @time :2019.09.25
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res