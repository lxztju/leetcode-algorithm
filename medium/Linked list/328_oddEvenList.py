# -*- coding:utf-8 -*-
# @time :2019/11/30
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head:
            return head

        odd = ListNode(0)
        even = ListNode(0)
        odd_head = odd
        even_head = even
        # print(odd)

        f = 0
        # print(f)
        while head:
            # print(head)
            if f == 0:
                odd.next = head
                f = 1
                odd = odd.next
                # print(odd)
            # break
            else:
                even.next = head
                f = 0
                even = even.next
            head = head.next
            # print(odd,even)
            # break

        even.next = None
        odd.next = even_head.next

        return odd_head.next
