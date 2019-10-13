# -*- coding:utf-8 -*-
# @time :2019.10.13
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju


##基数排序
# 桶排序的一种扩展
# 仅仅使用10个桶，标号为0-9
# 分别对待排序数组，个位，十位， ... 分别进行桶排序
# 时间复杂度：平均O(n*k), 最坏O(n*k), 最好O(n*k)
# 稳定

def RadixSort(numbers):
    """
    基数排序
    :param numbers:输入待排序数组
    :return:
    """
    bucket_count = 10 ##桶的数目
    div = 1  # 除数，去除数组中的元素，得到相应的位数
    loop_count = len(str(max(numbers))) #最大数字的位数决定了循环的次数

    #创建bucket_count个空桶
    buckets = [[] for i in range(bucket_count)]

    while bucket_count:
        # 将数据存入桶中
        for num in numbers:
            buckets[num // div % bucket_count].append(num)

        #将数据依次取出
        i = 0  # 待排序数组numbers的索引
        for bucket in buckets:
            while bucket:
                numbers[i] = bucket.pop(0)  # 依次取出
                i += 1

        div *= 10
        bucket_count -= 1

if __name__ == "__main__":
    numbers = [12, 321, 432, 5, 43, 6, 45, 765, 7, 65, 876, 8, 67, 98, 679, 87, 987, 9]
    RadixSort(numbers)
    print(numbers)








