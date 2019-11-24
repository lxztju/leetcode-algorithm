# -*- coding:utf-8 -*-
# @time :2019/10/16
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定两个数组，编写一个函数来计算它们的交集。
# 说明:
#
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。

# 利用集合
# 集合的插入元素：s.add( x )
#             s.update( x )，参数可以是列表，元组，字典等
#
# 集合删除： s.remove( x )，元素不存在发生错误
#         s.discard( x ) ， 元素不存在不发生错误
#             s.pop()   随机删除
# 查找判断元素是否在集合中：   x in s

#
# 集合长度： len(s)
#
# 清空集合：s.clear()

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res1 = set()
        res = []
        set1 = set(nums1)
        for val in nums2:
            if val in set1:
                res1.add(val)

        res = list(res1)
        return res





