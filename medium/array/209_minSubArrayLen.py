# -*- coding:utf-8 -*-
# @time :2019/10/14
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。


# class Solution:
#     def minSubArrayLen(self, s: int, nums:list) -> int:
#         """
#         滑动窗口法
#         :param s: 子数组的和
#         :param nums: 输入的数组
#         :return: 满足条件的最短子数组的和
#         """
        # p1 = -1
        # p2 = 0
        #
        # length = float("inf")
        # if len(nums) < 1: return 0
        # _sum = nums[0]
        # while _sum >= s or p2 < len(nums)-1:
        #
        #
        #     if _sum < s :
        #         p2 += 1
        #         _sum += nums[p2]
        #         continue
        #
        #     else:
        #         if length >= p2 - p1:
        #             length = p2 - p1
        #         p1 += 1
        #         _sum -= nums[p1]
        # length = 0 if length == float("inf") else length
        # return length

##第二种写法
class Solution:
    def minSubArrayLen(self, s: int, nums:list) -> int:

        length = float("inf")
        if len(nums) < 1: return 0
        _sum = 0
        i = -1

        for j in range(len(nums)):
            _sum += nums[j]
            if _sum < s:
                pass
            else:
                while _sum >= s:
                    i += 1
                    _sum -= nums[i]
                if length > j - i + 1:
                    length = j - i +1
        length = 0 if length == float("inf") else length
        return length


s = Solution()
nums = [2,3,1,2,4,3,8,3,4,5,6]
k = 12
l = s.minSubArrayLen(k, nums)
print(l)




