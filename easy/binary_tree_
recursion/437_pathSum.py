# -*- coding:utf-8 -*-
# @time :2019/12/13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        if not root: return 0
        # root存在于路径中
        res = self.findpath(root, sum)

        # root不存在路径中
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res

    def findpath(self, root, sum):
        # pathsum1的解题思路
        # 路径之和为sum的路径的个数
        if not root: return 0
        res = 0
        if sum == root.val:
            res += 1
        res += self.findpath(root.left, sum - root.val)
        res += self.findpath(root.right, sum - root.val)

        return res