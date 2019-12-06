# -*- coding:utf-8 -*-
# @time :2019/12/3
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        #双索引
        #等到快指针找到None时，慢指针就在n节点的前一个节点处
        dummy = ListNode(None)
        dummy.next = head

        fast = head
        slow = dummy

        #快慢指针之间间隔为n
        #慢指针指向待删除节点的前一个元素
        for i in range(n):
           if fast:
                fast =  fast.next

        #当fast指向最后一个节点的None时，slow指向待删除节点的前一个节点
        # print(fast)
        while fast:
            fast = fast.next
            slow = slow.next
        # print(slow)

        slow.next = slow.next.next

        return dummy.next

