# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串

##采用对撞指针
# 利用两个指针，头尾往中间遍历
class Solution:
    def isPalindrome(self, s: str) -> bool:

        p1 = 0  #头部指针
        p2 = len(s) - 1  #尾部指针

        while p1 < p2:

            if s[p1].isalnum():
                if s[p2].isalnum():
                    if s[p1].lower() == s[p2].lower():
                        p1 += 1
                        p2 -= 1
                        continue
                    else:
                        return False
                else:
                    p2 -= 1
            else:
                p1 += 1
        return True