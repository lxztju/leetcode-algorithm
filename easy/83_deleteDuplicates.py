# -*- coding:utf-8 -*-
# @time :2019/11/30
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head
        head_pre = head

        while head:
            if not head.next:
                break
            while head and head.next and head.val == head.next.val:
                head.next =head.next.next
            if head:
                head = head.next
        return head_pre


