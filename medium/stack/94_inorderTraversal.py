# -*- coding:utf-8 -*-
# @time :2019/12/5
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



##实现二叉树的中序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        res = []

        #用递归实现中序遍历
        def dfs(node):
            if not node: return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res
