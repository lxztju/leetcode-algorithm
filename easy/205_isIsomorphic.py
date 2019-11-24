# -*- coding:utf-8 -*-
# @time :2019/10/20
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定两个字符串 s 和 t，判断它们是否是同构的。
#
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
#
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。


## 方法1： 双哈希 类似于290

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def make_dict(s):
            s_dict = {}
            for i, val in enumerate(s):
                if val not in s_dict.keys():
                    s_dict[val] = [i]
                else:
                    s_dict[val].append(i)
            return s_dict

        if len(s) != len(t): return False
        s_dict = make_dict(s)
        t_dict = make_dict(t)

        if list(s_dict.values()) == list(t_dict.values()):
            return True
        else:
            return False

##方法2： 单hash
# 出现一对多，或者多对一时，返回False
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t) : return False
        #定义映射字典
        map_dict = {}

        for i, val in enumerate(s):

            if map_dict.get(val):
                # 多对一
                if t[i] != map_dict[val]:
                    return False

            else:
                # 一对多
                if t[i] in map_dict.values():
                    return False

            map_dict[val] = t[i]

        return True


