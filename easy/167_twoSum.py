# -*- coding:utf-8 -*-
# @time :2019.10.12
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju

# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2



####方法1：暴力算法
# class Solution:
#     def twoSum(self, numbers, target: int):

        # for i, num in enumerate(numbers):
        #     val = target - num
        #     for j in range(i+1, len(numbers)):
        #         if numbers[j] == val:
        #             # if i <j :
        #             #     return [i,j]
        #             # else:
        #             #     return [j,i]
        #             return [i, j] if i < j else [j,i]


####方法二：对撞指针
class Solution:
    def twoSum(self, numbers, target: int):

        p1 = 0  # 第一个指针，指向头部
        p2 = len(numbers) - 1

        while p1 < p2:
            _sum = numbers[p1] + numbers[p2]
            if _sum == target:
                return [p1 + 1, p2 + 1]
            elif _sum < target:
                p1 += 1
            else:
                p2 -= 1

        return None




numbers = [7,2,11,15]
target = 9
s = Solution()
print(s.twoSum(numbers, target))

