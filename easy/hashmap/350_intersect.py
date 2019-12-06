# -*- coding:utf-8 -*-
# @time :2019/10/16
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定两个数组，编写一个函数来计算它们的交集
#
# 说明：
#
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。

##利用字典

# 字典的长度：len(dict)
#
# 删除字典内所有元素：dict.clear()
#
# 删除字典或者键值对： del dict[key] 或者del dict
#
# 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值：dict.fromkeys(seq[, val])
#
# 返回指定键的值，如果值不在字典中返回default值：dict.get(key, default=None)

# 遍历字典  for k,v in dict.items()     for k, in dict.keys()

class Solution:
    def intersect(self, nums1, nums2):

        dict1 = dict.fromkeys(nums1, 0)
        res = dict.fromkeys(nums2, 0)
        result = []

        for val1 in nums1:
            dict1[val1] += 1

        for val2 in nums2:
            if dict1.get(val2) is not None and dict1[val2] > 0:
                res[val2] += 1
                dict1[val2] -= 1
        for k, v in res.items():
            for i in range(v): result.append(k)
        return result


s = Solution()
nums1 = [9,4,9,8,4]
nums2 = [4,9,5]
print(s.intersect(nums1,nums2))