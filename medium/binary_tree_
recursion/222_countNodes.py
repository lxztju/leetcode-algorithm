# -*- coding:utf-8 -*-
# @time :2019/12/9
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
# 并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点


##时间复杂度太高，打败8%
class Solution:
    def __init__(self):
        self.res = 0

    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def count(root):
            if root != None:
                self.res += 1
            else:
                return 0
            count(root.left)
            count(root.right)

        count(root)
        return self.res

##打败97%
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        return countNodes(root.left) + countNodes(root.right) + 1


