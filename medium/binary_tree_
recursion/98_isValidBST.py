# -*- coding:utf-8 -*-
# @time :2019/12/13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

####第一种就是直接递归搜索所有的节点，效率较低
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def left_dfs(root, node):
            if not root: return True
            return root.val < node.val and left_dfs(root.left, node) and left_dfs(root.right, node)

        def right_dfs(root, node):
            if not root: return True
            return root.val > node.val and right_dfs(root.left, node) and right_dfs(root.right, node)

        if not root: return True
        l = left_dfs(root.left, root)
        r = right_dfs(root.right, root)

        return l and r and self.isValidBST(root.left) and self.isValidBST(root.right)




class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
