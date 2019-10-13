# -*- coding:utf-8 -*-
# @time :2019.09.24
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 题目描述：给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 解题思路：利用滑窗
# 将字符串存入一个队列中，如果新拿到的字符在队列中，就将队列最左边的元素弹出，最终扫描一遍
# 在扫描过程中保存最长的字符串序列


class Solution:
    def lengthOfLongestSubstring(self, s):
        max_set_length = 0
        current_set_length = 0
        min_set=set()
        left = 0
        for i , character in enumerate(s):

            while (character in min_set):
                min_set.remove(s[left])
                left += 1
                current_set_length -= 1
            min_set.add(character)
            current_set_length +=1

            if current_set_length>max_set_length:
                max_set_length =  current_set_length
        return max_set_length