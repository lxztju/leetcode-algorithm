# -*- coding:utf-8 -*-
# @time :2019/12/13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



###二叉搜索树的查找
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
# 最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root: return None

        if p.val > root.val and q.val > root.val:
            res = self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            res = self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

        return res