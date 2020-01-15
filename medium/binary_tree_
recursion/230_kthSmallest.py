# -*- coding:utf-8 -*-
# @time :2019/12/14
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


#求第k小的元素
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        # 二叉搜索树中序遍历是排序数组

        if not root: return None

        def dfs(root):
            if not root: return None

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
            return res
        res = []
        res = dfs(root)
        return res[k-1]