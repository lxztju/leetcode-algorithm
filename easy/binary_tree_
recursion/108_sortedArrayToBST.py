# -*- coding:utf-8 -*-
# @time :2019/12/14
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 构建二叉搜索树
# 将排序数组构建为二叉搜索树
# 递归实现

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if len(nums) < 1:
            return None
        #构建树采用递归的方法
        mid = len(nums) // 2

        node = TreeNode(nums[mid])

        left = nums[:mid]
        right = nums[mid+1:]
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)
        return node