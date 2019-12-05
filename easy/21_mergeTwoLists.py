# -*- coding:utf-8 -*-
# @time :2019/11/30
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode(None)
        res = dummy

        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next

        if l1:
            dummy.next = l1
        else:
            dummy.next = l2

        return res.next


