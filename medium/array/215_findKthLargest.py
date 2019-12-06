# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。


# class Solution:
#     def findKthLargest(self, nums, k: int) -> int:
#
#         nums = sorted(nums)
#
#         return nums[-1 * k]


#利用快排操作
# 但是仅仅需要对与一边的序列进行重排
# class Solution:
#     def findKthLargest(self, nums, k: int) -> int:
#
#
#         def quick_sort(array, l, r):
#
#             p = partition(array, l, r)
#
#             if (len(nums)- p ) == k:
#                 return array[p]
#             elif (len(nums)- p ) > k:
#                 quick_sort(array, p+1, r)
#             else:
#                 quick_sort(array, l, p-1)
#
#         def partition(array, l, r):
#
#             x = array[l]
#             i = r + 1
#
#             for j in range(r, l-1, -1):
#
#                 if array[j] > x:
#                     i -= 1
#                     array[i], array[j] = array[j], array[i]
#             array[i-1], array[l] = array[l], array[i-1]
#
#             return i-1
#
#         quick_sort(nums, 0, len(nums)-1)
#         return nums[-1 * k]
import random
class Solution:
    def findKthLargest(self, nums, k: int) -> int:

        def partition(array, l, r):
            a = random.randint(l, r)
            array[a], array[l] = array[l], array[a]
            x = array[l]

            i = r + 1

            for j in range(r, l - 1, -1):

                if array[j] > x:
                    i -= 1
                    array[i], array[j] = array[j], array[i]
            array[i - 1], array[l] = array[l], array[i - 1]
            p = i - 1
            if (len(nums) - p) == k:
                return array[p]
            elif (len(nums) - p) > k:
                return partition(array, p + 1, r)
            else:
                return partition(array, l, p - 1)

        return partition(nums, 0, len(nums) - 1)


nums = [2,1]
s = Solution()
print(s.findKthLargest(nums,k=2))