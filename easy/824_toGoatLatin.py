# -*- coding:utf-8 -*-
# @time :2019.09.11
# @IDE : pycharm
# @author :lxztju
# @github : https://github.com/lxztju

###English desciption
# A sentence S is given. composed of words separated by space.
# Each words only consists of lowercase and Uppercase.
# change this sentence to another format.
#if the word in S is started with vowel(a,e,i,o,u), added 'ma' to the end
#Otherwise, move the first letter of thw world to the end of the word and add 'ma'
#Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1

##中文描述
# 给定一个句子，句子中仅由大小写英文字母组成，并由空格分割
# 如果句子中的单词以元音字母开头，在这个单词结尾加上‘ma’
# 如果单词开头不是元音字母，将开头字母移至结尾，然后加上‘ma’
# 按照句子中单词的索引顺序，每个单词后边加上字母‘a’，a的数目与索引相同，从一开始


###solution
class Solution(object):
    def toGoatLatin(self, S):
        def convert(word):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[:1]
            return word + 'ma'

        return " ".join(convert(word) + 'a' * i
                        for i, word in enumerate(S.split(), 1))


S = Solution()
print(S.toGoatLatin('I am a chinese people'))