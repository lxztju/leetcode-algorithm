# -*- coding:utf-8 -*-
# @time :2019/12/9
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 计算给定二叉树的所有左叶子之和

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0

        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)

        return left + right