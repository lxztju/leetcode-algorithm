# -*- coding:utf-8 -*-
# @time :2019.10.12
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

import time

# 双指针操作
# 定义两个指针，一个为慢指针p1,一个为快指针p2, p1指向写入的位置，p2指向数组遍历的元素
# 利用p2遍历数组，p1控制写入的位置
# p2向后遍历数组的元素，当p2指向的元素与p1相等时，将p1向后移动一步，并将p2指向的元素赋值给p1
# 如果相等的元素超过了两个，不执行赋值操作，p2向后继续遍历数组
# 当二者不相等时，将p1向后移动，然后进行赋值操作

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
                if p1 != p2:
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