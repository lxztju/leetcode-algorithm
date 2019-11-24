# -*- coding:utf-8 -*-
# @time :2019/11/20
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d 
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。


#利用排序加双指针法,转换为三数之和

class Solution:
    def fourSum(self, nums, target: int):

        result = []
        #输入列表长度小于4,直接返回
        if not nums or len(nums) < 4:
            return result

        nums.sort()  # 将列表进行排序


        #第一层循环，遍历排序后的列表
        for i in range(len(nums)):

            #如果前4个数之和大于目标值，直接返回结果
            if sum(nums[i:i+4])>target:
                break

            #第一个数与最大的三个数子和小于目标，直接将i后移
            if nums[i] + sum(nums[-3:]) < target:
                continue

            #去除相等的元素
            if i > 0 and nums[i - 1] == nums[i]:
                continue  # 去除相等的元素


            ##第二层循环，想当与在子序列nums[i:]来进行三数之和的操作
            for j in range(i+1 ,len(nums)):

                ##同样如果前几个数数之和大于目标值，直接返回
                if nums[i] + sum(nums[j:j+3]) > target:
                    break

                #同样，前几个数与最大的几个数之和小于目标值，将j后移
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue

                #在子序列中去除相等的元素
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                #左右指针
                left = j + 1
                right = len(nums) - 1

                while left < right:

                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    #如果四数之和小于目标值，将左指针后移，
                    if four_sum < target:
                        left += 1

                    #如果四数之和大于目标值，将右指针左移
                    elif four_sum > target:
                        right -= 1

                    #如果刚好等于目标值，找到四个列表元素
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        #去掉相同的元素
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1

                        while left < right and nums[left + 1] == nums[left]:
                            left += 1

                        right -= 1
                        left += 1
        return result

s = Solution()
nums = [1, 0, -1, 0, -2, 2]
print(s.fourSum(nums,10))