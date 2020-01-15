# -*- coding:utf-8 -*-
# @time :2019/12/9
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。


###利用递归实现DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        left_height = self.minDepth(root.left)

        right_height = self.minDepth(root.right)

        if left_height == 0 or right_height == 0:
            return left_height + right_height + 1

        return min(left_height, right_height) + 1