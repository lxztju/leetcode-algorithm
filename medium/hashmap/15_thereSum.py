# -*- coding:utf-8 -*-
# @time :2019/11/20
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c
# 使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

# 考虑解法：利用排序加上双指针

class Solution:
    def threeSum(self, nums):


        result = []
        if len(nums) < 3:
            return result

        nums.sort() #将列表进行排序

        for i in range(len(nums)):

            if nums[i] > 0:
                return result   #已经排序完成，第一个数大于零后后边的数均大于零，不可能再有相加为0

            if i > 0 and nums[i-1] == nums[i]:
                continue  #去除相等的元素

            left = i + 1
            right = len(nums) - 1

            while left < right:


                three_sum = nums[i] +nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -=1
                else:
                    result.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

                    while left < right and nums[left + 1] == nums[left]:
                        left += 1

                    right -= 1
                    left += 1
        return result





s = Solution()
nums = [1, 0, -1, 0, -2, 2]
print(s.threeSum(nums))






