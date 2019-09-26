# -*- coding:utf-8 -*-
# @time :2019.09.25
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju


# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"


# class Solution:
#     def longestCommonPrefix(self, strs):
#         if not strs: return ""
#         ss = list(map(set, zip(*strs)))
#         res = ""
#         for i, x in enumerate(ss):
#             x = list(x)
#             if len(x) > 1:
#                 break
#             res = res + x[0]
#         return res


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s = strs[0]
        if s == "": return ""
        result = ""
        for i in range(len(s)):
            for j in range(len(strs)):
                try:
                    if s[i] != strs[j][i]:
                        result = s[:i]
                        return result

                except:
                    result = s[:i]
                    return result
        result = s
        return result