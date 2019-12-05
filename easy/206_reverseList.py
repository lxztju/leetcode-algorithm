# -*- coding:utf-8 -*-
# @time :2019/11/29
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 反转一个单链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        #定义三个指针
        pre = None
        cur = head
        nex = head.next
        # print(nex)

        while cur is not None:
            # print(nex)
            # print(cur)
            cur.next = pre
            pre = cur
            cur = nex
            if nex is not None:
                nex = nex.next
            else:
                break
        return pre