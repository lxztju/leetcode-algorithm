# -*- coding:utf-8 -*-
# @time :2019/11/21
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数
# 使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案


#使用排序加上双指针类似于三数之和

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:


        if not nums or len(nums)<3:
            raise Exception("error")

        nums.sort()
        n = len(nums)
        closest = float('inf')

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = n - 1

            while l < r:


                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum < target:
                    diff = target-three_sum
                    if closest >diff:
                        closest  = diff
                        result = three_sum
                    l += 1


                elif three_sum > target:
                    diff = three_sum-target
                    if closest > diff:
                        closest = diff
                        result = three_sum
                    r -= 1

                else:
                    result = three_sum
                    return result
        return result


s = Solution()
nums = [1,2,4,8,16,32,64,128]
print(s.threeSumClosest(nums,82))