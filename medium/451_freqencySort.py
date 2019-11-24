# -*- coding:utf-8 -*-
# @time :2019/10/20
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

class Solution:
    def frequencySort(self, s: str) -> str:

        ## 建立hash表统计字符出现的频率
        from collections import defaultdict
        s_dict = defaultdict(int)
        res = []
        #统计字符出现的频率
        for val in s:
            s_dict[val] += 1

        #赋值返回值
        for k, v in s_dict.items():
            for i in range(v):
                res.append(k)

        return ''.join(res)
