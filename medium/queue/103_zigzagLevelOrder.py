# -*- coding:utf-8 -*-
# @time :2019/12/6
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。


###用102题的思路先计算后反转

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

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
        result = res
        for i in range(len(res)):
            if i%2 ==0:
                result[i] = res[i]
            else:
                result[i] = res[i][::-1]
        return result