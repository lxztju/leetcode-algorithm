# -*- coding:utf-8 -*-
# @time :2019/11/30
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        function:  add two number and return the result
        :param l1: listnode, the first number for the operation of add
        :param l2: listnode, the second number for the operationof add
        :return:  listnode
        """
        s1 = []
        s2 = []
        r = []   ###construct three stack to reverse three linknode of l1,l2 and result
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        reminder = 0
        # print(s1)
        # print(s2)
        while (s1 or s2 or (reminder !=0)):
            s11 = s1.pop() if (len(s1) !=0 ) else 0
            s22 = s2.pop() if (len(s2) !=0 ) else 0
            r.append((s11+s22+reminder)%10)
            reminder = (s11+s22+reminder)//10
        l3 = ListNode(r.pop())
        l4 = l3
        for i in range(len(r)):
            l3.next = ListNode(r.pop())
            l3 = l3.next
        return l4