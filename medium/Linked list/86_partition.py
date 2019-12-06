# -*- coding:utf-8 -*-
# @time :2019/11/30
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        ##创建两个链表，第一个指向小于x的元素，第二个指向大于x的元素


        inf = ListNode(0)
        sup = ListNode(0)
        sup_head = sup
        inf_head = inf

        while head:
            if head.val < x:
                inf.next = head
                inf = inf.next
            else:
                sup.next = head
                sup = sup.next
            head = head.next

        #创建结束节点
        sup.next = None
        inf.next = sup_head.next

        return inf_head.next


