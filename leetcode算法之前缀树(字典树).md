今天来盘一盘 **前缀树(字典树) ** 这类题目



使用**python**刷题分类整理的笔记,请参考:  [https://github.com/lxztju/leetcode-algorithm/tree/v1](https://github.com/lxztju/leetcode-algorithm/tree/v1)


## 前缀树(字典树)
前缀树是用来存储字符串的。前缀树的每一个节点代表一个字符串（前缀）。每一个节点会有多个子节点，通往不同子节点的路径上有着不同的字符。子节点代表的字符串是由节点本身的原始字符串 ，以及通往该子节点路径上所有的字符组成的。

前缀树的一个重要的特性是，节点所有的后代都与该节点相关的字符串有着共同的前缀。


* 208 实现 Trie (前缀树)（medium）
* 211 添加与搜索单词 - 数据结构设计(medium)


#### 208 实现 Trie (前缀树)
```c++
class Trie {

private:
    bool isEnd;
    Trie* nextNode[26];

public:
    /** Initialize your data structure here. */
    Trie() {
        isEnd = false;
        memset(nextNode, 0, sizeof(nextNode));
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Trie* node = this;
        for (char c : word){
            if (node->nextNode[c - 'a'] == nullptr)
                node->nextNode[c - 'a'] = new Trie();
            node = node->nextNode[c - 'a'];
        }
        node->isEnd = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Trie* node = this;
        for (char c: word){
            node = node->nextNode[c - 'a'];
            if (node == nullptr) return false;
        }
        return node->isEnd;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Trie* node = this;
        for (char c: prefix){
            node = node->nextNode[c - 'a'];
            if (node == nullptr) return false;
        }
        return true;        
    }
};
```

#### 211 添加与搜索单词 - 数据结构设计

```c++
class WordDictionary {

private:
    bool isEnd;
    WordDictionary* nextNode[26];
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        isEnd = false;
        memset(nextNode, 0, sizeof(nextNode));
    }
    
    void addWord(string word) {
        WordDictionary* node = this;
        for (char c : word){
            int index = c - 'a';
            if (node->nextNode[index] == nullptr)
                node->nextNode[index] = new WordDictionary();
            node = node->nextNode[index];
        }
        node->isEnd = true;

    }
    
    bool search(string word) {
        auto node = this;
        return match(word, node, 0);
    }
    bool match(string word, WordDictionary* node, int start){
        if (node == nullptr) return false;
        if (start == word.size()) return node->isEnd;

        auto ch = word[start];
        if (ch != '.'){
            int index = ch - 'a';
            if (node->nextNode[index] == nullptr)
                return false;
            node = node->nextNode[index];
            return match(word, node, start + 1);
        }
        else{
            for (auto ch = 'a'; ch <= 'z'; ch++){
                int index = ch - 'a';
                if (match(word, node->nextNode[index], start + 1))
                    return true;
            }
        }
        return false;
    }
};
```



## 更多分类刷题资料

* 微信公众号： 小哲AI

  ![wechat_QRcode](https://img-blog.csdnimg.cn/20210104185413204.jpg)

* GitHub地址： [https://github.com/lxztju/leetcode-algorithm](https://github.com/lxztju/leetcode-algorithm)
* csdn博客： [https://blog.csdn.net/lxztju](https://blog.csdn.net/lxztju)
* 知乎专栏： [小哲AI](https://www.zhihu.com/column/c_1101089619118026752)
* AI研习社专栏：[小哲AI](https://www.yanxishe.com/column/109)

