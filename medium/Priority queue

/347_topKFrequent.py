# -*- coding:utf-8 -*-
# @time :2019/12/7
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


class Solution:
    def topKFrequent(self, nums, k):

        from collections import Counter
        import heapq
        count = Counter(nums)
        # print(count)
        return heapq.nlargest(k, count.keys(), key=count.get)