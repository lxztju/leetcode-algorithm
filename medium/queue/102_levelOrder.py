# -*- coding:utf-8 -*-
# @time :2019/12/6
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

#######迭代法，使用BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []
        if not root:
            return res

        cur_level = [root]
        while cur_level:
            temp = []
            next_level = []
            for node in cur_level:
                temp.append(node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            cur_level = next_level
            res.append(temp)

        return res


##############递归法（类似于前序遍历，DFS）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return res
