# -*- coding:utf-8 -*-
# @time :2019/12/9
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。


####利用递归实现DFS，进行搜索
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root == None:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return max(left_height, right_height) + 1