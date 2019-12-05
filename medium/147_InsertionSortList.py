# -*- coding:utf-8 -*-
# @time :2019/12/2
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


#链表实现插入排序

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        dummy = ListNode(None)

        # 循环往后扫描遍历
        while head:

            ##待比较元素的下一个元素
            nex = head.next

            # 将待比较的元素从头开始比较，找寻待插入的点
            # 待插入节点的上一个节点为pre
            pre = dummy
            # print(dummy)
            while pre.next and pre.next.val < head.val:
                # 待查如节点的位置
                pre = pre.next
                # 进行节点的插入
            head.next = pre.next
            pre.next = head
            ##从下一个元素继续
            head = nex

        return dummy.next