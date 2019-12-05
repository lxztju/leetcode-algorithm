# -*- coding:utf-8 -*-
# @time :2019/11/30
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 删除链表中等于给定值 val 的所有节点。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        pre = ListNode(None)
        pre.next = head
        head1 = pre

        while head:
            if head.val == val:
                pre.next = head.next
                # print(pre.next)

            else:
                pre = pre.next
            head = head.next
        # print(pre.next)
        # print(head1)
        return head1.next