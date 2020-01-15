# -*- coding:utf-8 -*-
# @time :2019/12/9
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。


##暴力法
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def length(root):
            if not root: return 0
            left_length = length(root.left)
            right_length = length(root.right)
            return max(left_length, right_length) + 1

        if not root: return True
        left_l = length(root.left)
        right_l = length(root.right)

        return abs(left_l - right_l) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)



