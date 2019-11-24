# -*- coding:utf-8 -*-
# @time :2019/10/20
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

#利用查找表进行操作

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 判断二者长度不一样直接返回false
        if len(s) != len(t): return False

        # 将t做为字典形式
        from collections import defaultdict
        t_dict = defaultdict(int)

        for val in t:
            t_dict[val] += 1

        for val in s:
            #如果不在t_dict中返回false
            if t_dict[val] < 1:
                return False
            else:
                t_dict[val] -= 1
        return True


s = Solution()
s1 = " "
t = " "
print(s.isAnagram(s1,t))