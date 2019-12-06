# -*- coding:utf-8 -*-
# @time :2019/12/6
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值

#########类似于102题的思路，先层次遍历，然后返回每一层的最后一个值
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

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
        return [res[i][-1] for i in range(len(res))]



###########不利用递归，利用BFS迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        res = []
        if not root: return res
        # 根节点入队列
        cur_level = [root]

        while cur_level:
            temp = []
            next_level = []

            # 遍历每一层
            for node in cur_level:
                temp.append(node.val)
                # 将下一层的节点入队列
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            cur_level = next_level
            res.append(temp[-1])

        return res