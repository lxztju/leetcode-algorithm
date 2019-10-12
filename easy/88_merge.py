# -*- coding:utf-8 -*-
# @time :2019.10.12
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju

# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #利用双指针指向两个数组元素的末尾，然后从末尾填入元素

        p1 = m - 1  # 指向p1的末尾
        p2 = n - 1  # 指向p2的末尾

        p3 = m + n - 1
        # print(nums1)

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]

                p1 -= 1
            else:
                nums1[p3] = nums2[p2]

                p2 -= 1
            p3 -= 1
        if (p2 >= 0):
            nums1[: p3 + 1] = nums2[: p2 + 1]
        # print(nums1)


nums1 = [0]
m = 0
nums2 = [8]
n=1
s = Solution()
s.merge(nums1, m, nums2, n)