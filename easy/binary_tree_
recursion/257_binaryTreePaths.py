# -*- coding:utf-8 -*-
# @time :2019/12/10
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
#
# 说明: 叶子节点是指没有子节点的节点。


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        res = []
        def dfs(root, tmp):
            if not root.left and not root.right:res.append(tmp + [str(root.val)])
            if root.left:dfs(root.left, tmp + [str(root.val)])
            if root.right:dfs(root.right, tmp + [str(root.val)])
        dfs(root, [])
        return ["->".join(a) for a in res]


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths
