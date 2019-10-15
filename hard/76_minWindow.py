# -*- coding:utf-8 -*-
# @time :2019/10/14
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
# 说明：
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。


##滑动窗口法
# 滑动窗口尾部指针后移向后扫描，直到找到一个满足条件的窗口
# 然后左指针向后移动，直到第一个不满足条件的窗口出现，此时将右指针后移，直到再次满足条件
# 判断一个窗口是否满足条件，就是采用一个目标字符串等长的counter来标志，每次扫描到一个元素就将counter减1
# 当counter为0,说明这个窗口满足条件，然后将左指针后移，当左指针扫描到目标字符串中的字符时，将counter加一
# 右指针后移去找寻这一个元素

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0  #窗口左指针
        r = 0  #窗口右指针

        min_len = float("inf") # 记录最短字串的长度
        res = ""    #存储对应的最短子串
        counter = len(t)  # 计数器，记录剩余待扫描的字符串的个数

        from collections import defaultdict
        find = defaultdict(int)   #defaultdict（int） 当键值不存在时返回0

        for val in t:
            find[val] += 1

        while r < len(s) and l <= r:
            # 如果键值为s[r]的字符存在于原始目标字串中，将对应的counter减1
            if find[s[r]] > 0:
                counter -= 1

            #不存在于目标字串中的元素的值将会变为负值，保证后边判断左指针指向的元素是否是目标字串中的字符，提供了方便
            find[s[r]] -= 1

            # 当窗口包含全部字符时，将左指针后移直到窗口不满足条件
            while counter ==0:
                #存储最短字串
                if r-l+1 < min_len:
                    min_len =  r - l + 1
                    res = s[l : r+1]

                ##如果窗口左指针再次右移已经不满足条件，说明检测到一个字符，
                # 就counter += 1，然后另右指针去找寻这一个元素
                if find[s[l]] == 0:
                    counter += 1

                find[s[l]] += 1
                l += 1

            r += 1
        return res



# from collections import defaultdict
#
# find = defaultdict(int)
#
# print(find['c'] == 0)
#





s = Solution()
s1 = "cabwefgewcwaefgcf"
p = "cae"
result = s.minWindow(s1, p)
print(result)


