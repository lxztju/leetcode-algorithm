# -*- coding:utf-8 -*-
# @time :2019/10/14
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
#
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。


class Solution:
    def findAnagrams(self, s: str, p: str):

        result = []
        len_p, len_s = len(p), len(s)
        if len_p >len_s : return []
        p_dict = {}
        s_dict = {}

        for val in p:
            p_dict[val] = p_dict.get(val,0) + 1

        for i in range(len_p):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1

        for i in range(len_s-len_p):
            if p_dict == s_dict:
                result.append(i)

            s_dict[s[i]] -= 1

            if s_dict[s[i]] == 0:
                del s_dict[s[i]]

            if s_dict.get(s[i+len_p]) is None:
                s_dict[s[i+len_p]] = s_dict.get(s[i+len_p], 0) + 1
            else:
                s_dict[s[i+len_p]] += 1
        if p_dict == s_dict:
            result.append(len_s-len_p)

        return result



s = Solution()
s1 = "cbaebabacd"
p = "abc"
result = s.findAnagrams(s1,p)
print(result)
