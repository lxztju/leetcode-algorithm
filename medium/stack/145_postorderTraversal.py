# -*- coding:utf-8 -*-
# @time :2019/12/5
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


#实现二叉树的后序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        ##用递归实现
        res = []
        def dfs(node):
            if not node: return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res
