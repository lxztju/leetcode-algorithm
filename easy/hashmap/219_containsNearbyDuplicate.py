# -*- coding:utf-8 -*-
# @time :2019/11/24
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j
# 使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

#滑动窗口法(超时）
# class Solution:
#     def containsNearbyDuplicate(self, nums, k: int) -> bool:
#
#         from collections import defaultdict
#
#         if not nums or len(nums)<2 or k < 1:
#             return False
#
#         for i in range(len(nums)):
#
#             hashmap = defaultdict(int)
#             l = i
#             while l < len(nums) and l <= i + k:
#                 hashmap[nums[l]] += 1
#                 l += 1
#             # print(hashmap)
#             for v in hashmap.values():
#                 if v > 1:
#                     return True
#
#         return False


###滑动窗口法2
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:


        if not nums or len(nums)<2 or k < 1:
            return False

        l = 0

        num_set = set()
        while l <len(nums):
            if nums[l] not in num_set:
                num_set.add(nums[l])
                l += 1
            else:
                return True
            # print(num_set)
            if len(num_set)== k + 1:
                num_set.discard(nums[l-k-1])
        return False


s = Solution()
nums = [1,2,3,1,2,3]
k = 2
res = s.containsNearbyDuplicate(nums,k)
print(res)