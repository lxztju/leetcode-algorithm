# -*- coding:utf-8 -*-
# @time :2019/12/2
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju



# 请判断一个链表是否为回文链表。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # 双指针
        # 中点开始之后与从头开始的一样
        ##第一遍扫描找到中点的指针位置

        if head == None:
            return True

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 找到中点
        if fast:
            mid = slow.next
        else:
            mid = slow

        ##将后一部分的链表反转

        pre = None
        cur = mid
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        ##比较两段数组
        while pre and head:
            if head.val != pre.val:
                return False
            head, pre = head.next, pre.next
        return True






