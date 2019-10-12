# -*- coding:utf-8 -*-
# @time :2019.09.14
# @IDE : pycharm
# @autor :lxztju
# @github : https://github.com/lxztju

#Given a binary tree, each node has value 0 or 1.
# Each root-to-leaf path represents a binary number starting with the most significant bit.
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
#For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
#Return the sum of these numbers.

#DFS(depth first serach)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        path = None

        def dfs(root, path):
            if path == None:
                path = ''
            if root:
                path += str(root.val)
                if root.left or root.right:
                    return dfs(root.left, path) + dfs(root.right, path)
                else:
                    return int(path, 2)
            else:
                return 0

        number = dfs(root, path)

        return number
