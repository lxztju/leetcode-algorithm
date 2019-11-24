# -*- coding:utf-8 -*-
# @time :2019/11/24
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j
# 使得 nums [i] 和 nums [j] 的差的绝对值最大为 t
# 并且 i 和 j 之间的差的绝对值最大为 ķ。

#滑窗（超时）
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
#
#         num_set = set()
#         for i in range(len(nums)):
#
#             diff1 = nums[i] - t
#             diff2 = nums[i] + t
#
#             num_list = list(num_set)
#
#             for j in range(len(num_list)):
#                 if num_list[j] <= diff2 and num_list[j] >= diff1:
#                     return True
#
#             num_set.add(nums[i])
#
#             if len(num_set) == k + 1:
#                 num_set.discard(nums[i - k])
#
#         return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:

        length = len(nums)
        record = set()

        for i in range(length):
            if t==0:
                if nums[i] in record:
                    return True
            else:
                for v in record:
                    if abs(nums[i]-v)<=t:
                        return True
            record.add(nums[i])
            if len(record) == k+1:
                record.remove(nums[i-k])
        return False


s = Solution()
nums =[1,2,3,1]
t = 0
k = 3
res = s.containsNearbyAlmostDuplicate(nums, k, t)
print(res)