# -*- coding:utf-8 -*-
# @time :2019/11/23
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串
# 说明：
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。

###利用字典进行字典计数

class Solution:
    def groupAnagrams(self, strs):

        res = []
        if not strs and len(strs) ==0:
            return res

        dic_character = {}
        from collections import defaultdict
        res_dict = defaultdict(list)
        for j in range(len(strs)):


            for i in range(ord('a'),ord('z')+1):
                dic_character[chr(i)] = 0
            for k in range(len(strs[j])):
                dic_character[strs[j][k]] += 1
            # print(dic_character.values())

            res_dict[tuple(dic_character.values())].append(strs[j])
            # print(res_dict)
        res = res_dict.values()

        return res


s = Solution()
strs =["eat", "tea", "tan", "ate", "nat", "bat"]
res = s.groupAnagrams(strs)
print(res)
