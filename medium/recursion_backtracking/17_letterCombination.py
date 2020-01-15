# -*- coding:utf-8 -*-
# @time :2019/12/15
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

##利用递归构建树形结构的深度优先搜索
class Solution:
    def __init__(self):
        self.num_char = [
            ' ',
            '',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz',
        ]
        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1: return []
        self.find_path(digits, 0, '')
        return self.res

    def find_path(self, digits, index, s):
        #搜索深度优先搜索的所有路径

        if index >= len(digits):
            self.res.append(s)
            return

        characters = self.num_char[int(digits[index])]
        for char in characters:
            self.find_path(digits, index + 1, s + char)

        return