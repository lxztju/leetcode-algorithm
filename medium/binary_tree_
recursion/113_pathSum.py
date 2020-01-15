# -*- coding:utf-8 -*-
# @time :2019/12/13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        res = []

        def dfs(root, tmp, sum):
            if not root: return

            if not root.left and not root.right and sum - root.val == 0:
                tmp += [str(root.val)]
                return res.append(tmp)

            left = dfs(root.left, tmp + [str(root.val)], sum - root.val)
            right = dfs(root.right, tmp + [str(root.val)], sum - root.val)

            return res

        dfs(root, [], sum)
        return res