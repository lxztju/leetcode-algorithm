# -*- coding:utf-8 -*-
# @time :2019/12/6
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）


####利用第102题的思路，先求出结果再反转结果
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res

        def helper(node, depth):
            if not node: return
            if len(res)==depth:
                res.append([])
            res[depth].append(node.val)
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)

        helper(root,0)
        return res[::-1]
