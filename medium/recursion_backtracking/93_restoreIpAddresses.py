# -*- coding:utf-8 -*-
# @time :2020/1/14
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju




# 利用回溯法
class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def findip(s, flag, ip):
            """
            s: 待分割的字符串
            flag: 分割为四部分
            ip: 得到的分离后的ip
            """
            if flag == 4:
                if s == '':
                    res.append(ip[:-1])
                return
            for i in range(1, 4):
                if i > len(s): continue

                if int(s[:i]) <= 255:
                    findip(s[i:], flag + 1, ip + s[:i] + '.')
                    if s[0] == '0': break

            return

        findip(s, 0, '')
        return res


