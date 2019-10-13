# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。



##对撞指针
# 两个指针分别指向首尾，然后向中间遍历

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        vowels = list('aeiouAEIOU')

        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            if s[p1] in vowels and s[p2] in vowels:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1

            elif s[p2] not in vowels:
                p2 -= 1

            else:
                p1 += 1
        return ''.join(s)