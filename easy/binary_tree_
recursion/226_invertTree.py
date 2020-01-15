# -*- coding:utf-8 -*-
# @time :2019/12/9
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 翻转一棵二叉树。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root