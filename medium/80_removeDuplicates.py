# -*- coding:utf-8 -*-
# @time :2019.10.12
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju

# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

import time
class Solution:
    def removeDuplicates(self, nums) -> int:

        p1 = 0
        p2 = 1
        count = 1
        if len(nums) == 0: return 0
        t1 = time.time()

        while p2 < len(nums):
            #print(nums)

            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
                count = 1
            elif count >= 2:
                p2 += 1
                continue
            else:
                p1 += 1
                if p1 != p2 :
                    nums[p1] = nums[p2]
                count += 1
            p2 += 1
            print(nums)
        t2 = time.time()
        print(t2-t1)
        return p1 + 1

nums = [0,0,1,1,1,1,2,3,3]
s =  Solution()

print(s.removeDuplicates(nums))