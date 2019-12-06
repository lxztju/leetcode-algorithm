# -*- coding:utf-8 -*-
# @time :2019.09.12
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

#Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.
#text consists of lowercase English letters.

#返回按字典顺序排列的最小字串

#使用堆栈和字典
#利用字典找到每个字母最大的索引，然后依次将字符推入堆栈
#由于按照字典顺序排列，因此当后边的推入的字符小于堆栈中最后一个字符，并且这个字符在后边是依然存在的，那么就弹出字符

class Solution:
    def smallestSubsequence(self, text: str) -> str:
        dict={}
        for i in range(len(text)):
            dict[text[i]]=i
        stack=[]
        for i in range(len(text)):
            if text[i] in stack:
                continue
            while stack and stack[-1]>text[i] and dict[stack[-1]]>i:
                stack.pop()
            if text[i] not in stack:
                stack.append(text[i])
        return ''.join(stack)