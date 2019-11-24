# -*- coding:utf-8 -*-
# @time :2019/10/20
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1
# 也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

##使用集合
# 计算平方和，然后存入集合，计算下一个平方和是否存在于集合中，如果存在并且为1,返回true，如果不存在返回false

class Solution:
    def isHappy(self, n: int) -> bool:

        lookup = set()
        n_sum = n

        while n_sum not in lookup:
            lookup.add(n_sum)
            n_sum = sum([int(val) ** 2 for val in str(n_sum)])

        if n_sum == 1:
            return True
        else:
            return False

s = Solution()
print(s.isHappy(19))
