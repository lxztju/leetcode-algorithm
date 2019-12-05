# -*- coding:utf-8 -*-
# @time :2019/12/4
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


# 根据逆波兰表示法，求表达式的值。
#
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        char = ['+', '-', '*', '/']

        for s in tokens:
            if s in char:
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(eval(str(num2) + s + str(num1)))
                stack.append(res)

            else:
                stack.append(s)
        return stack[-1]