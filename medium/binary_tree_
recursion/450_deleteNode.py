# -*- coding:utf-8 -*-
# @time :2019/12/14
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:return None
        #到左子树里搜索
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        #到右子树里搜索
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
        # 存在的子树代替根节点
            if not root.left or not root.right:
                root = root.left if root.left else root.right
            else:
                temp = root.right
                # 找到右子树的最小（最左）节点
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                # 继续在右子树里递归
                root.right = self.deleteNode(root.right, temp.val)

        return root