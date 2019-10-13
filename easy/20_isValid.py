# -*- coding:utf-8 -*-
# @time :2019.09.26
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。



class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack_l = []
        for i, s1 in enumerate(s):
            if s1 in ['(', '[', '{']:
                stack_l.append(s1)
            else:
                try:
                    s2 = stack_l.pop()
                    if dic[s2] == s1:
                        continue
                    else:
                        return False
                except:
                    return False
        if len(stack_l) == 0:

            return True
        else:
            return False