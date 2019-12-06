# -*- coding:utf-8 -*-
# @time :2019.10.08
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



# 给定一个二叉树，找到最长的路径，
# 这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

#管解递归程序
#利用递归向下遍历二叉树，利用arrow_length查找当前跟节点的左子树与右子树的最长的路径
# 当左子树与右子树均与跟节点相同时，将最长的路径赋值为二者之和
class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans

