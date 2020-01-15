# -*- coding:utf-8 -*-
# @time :2019/12/9
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root: return False

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0

        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)

        return left or right