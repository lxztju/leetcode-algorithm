# -*- coding:utf-8 -*-
# @time :2019/12/3
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        # 将链表成环，然后找出头尾节点即可
        # 类似于第19题，找出倒数第k个节点即为头节点，倒数第k+1个几点即为尾节点
        # 本体即为找出倒数第k+1个头节点
        if not head:
            return head

        dummy = head
        num = 0
        while head:
            num += 1
            head = head.next
        # 从头数第m个节点为尾节点
        head = dummy

        m = abs(num - (k % num))
        if m == num:
            return dummy

        for i in range(m - 1):
            head = head.next
        tail = head

        head_new = tail.next

        pre = tail

        while pre.next:
            pre = pre.next

        tail.next = None
        pre.next = dummy
        # print(head_new)

        return head_new

