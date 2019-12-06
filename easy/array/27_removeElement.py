# -*- coding:utf-8 -*-
# @time :2019.10.11
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

class Solution:
    def removeElement(self, nums, val):
        i = 0

        while i < len(nums):
            if val == nums[i]:
                nums.remove(val)
            else:
                i += 1

        return len(nums)


nums = [0,1,2,2,3,0,4,2]

val = 2

s = Solution()
print(s.removeElement(nums, val), nums)

# 首尾两个指针，等于val的元素交换移至数组的末尾，然后释放
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        p1 = 0
        length = len(nums)
        p2 = length - 1
        count = 0

        while p1 <= p2:
            if nums[p2] != val:
                if nums[p1] == val:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    count += 1
                    p2 -= 1
                    p1 += 1
                else:
                    p1 += 1

            else:
                p2 -= 1
        nums = nums[0: p1]
        return len(nums)