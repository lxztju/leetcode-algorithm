# -*- coding:utf-8 -*-
# @time :2019/12/1
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        #定义虚拟的头节点
        dummy = ListNode(None)
        dummy.next = head

        p = dummy
        # print(node1,node2)

        while p.next and p.next.next:
            #设置交换节点
            node1 = p.next
            node2 = node1.next

            #交换节点的指针指向
            node1.next = node2.next
            node2.next = node1
            p.next = node2

            #更新节点的值
            p = node1

        return dummy.next