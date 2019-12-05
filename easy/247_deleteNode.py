# -*- coding:utf-8 -*-
# @time :2019/12/2
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



#仅仅给定结点，山海醋链表中的节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next


