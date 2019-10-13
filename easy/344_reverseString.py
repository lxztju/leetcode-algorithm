# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题


##对撞指针
# 两个指针分别指向首尾，交换两个指针指向的元素
# 然后将两个指针向中间靠拢

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1