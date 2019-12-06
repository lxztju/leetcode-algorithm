# -*- coding:utf-8 -*-
# @time :2019/12/5
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


#实现二叉树的前序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        ##用递归实现
        res = []
        def dfs(node):
            if not node: return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
