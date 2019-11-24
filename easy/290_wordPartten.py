# -*- coding:utf-8 -*-
# @time :2019/10/20
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

#双hash
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        def make_dict(s):
            s_dict = {}
            for i, val in enumerate(s):
                if val not in s_dict.keys():
                    s_dict[val] = [i]
                else:
                    s_dict[val].append(i)
            return s_dict

        s = str.split(" ")
        if len(s) != len(pattern): return False
        s_dict = make_dict(s)
        p_dict = make_dict(pattern)
        # print(s_dict.values())
        # print(p_dict.values())
        if list(s_dict.values()) == list(p_dict.values()):
            return True
        else:
            return False


s = Solution()
pattern = "bbaa"
str1 = "cat cat dog dog"
print(s.wordPattern(pattern, str1))