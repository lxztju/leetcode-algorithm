# -*- coding:utf-8 -*-
# @time :2019/12/13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
#
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
#
# 计算从根到叶子节点生成的所有数字之和。
#
# 说明: 叶子节点是指没有子节点的节点

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0

        def dfs(root, tmp):
            if not root: return res

            if not root.left and not root.right:
                tmp += str(root.val)
                res.append(tmp)
                return res

            left = dfs(root.left, tmp + str(root.val))
            right = dfs(root.right, tmp + str(root.val))
            return res

        res = []
        res = dfs(root, '')

        result = 0
        for i in res:
            result += int(i)
        return result