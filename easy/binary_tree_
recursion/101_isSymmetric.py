# -*- coding:utf-8 -*-
# @time :2019/12/9
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个二叉树，检查它是否是镜像对称的


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root: return True

        def match(r_left, r_right):

            if not r_left and not r_right:
                return True

            if not r_left or not r_right:
                return False

            return r_left.val == r_right.val and match(r_left.left, r_right.right) and match(r_left.right, r_right.left)

        return match(root.left, root.right)